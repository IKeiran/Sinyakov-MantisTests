import pytest
from fixture.application import Application
import json
import os.path

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--target'))['web']
    if (fixture is None) or (not fixture.is_valid()):
        fixture = Application(browser, web_config["baseUrl"])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)


@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption('--target'))['db']
    db_fixture = DBFixture(host=db_config["host"], name=db_config["name"],
                           user=db_config["user"], password=db_config["password"])

    def stop():
        db_fixture.destroy()
    request.addfinalizer(stop)
    return db_fixture

@pytest.fixture(scope='session')
def orm(request):
    db_config = load_config(request.config.getoption('--target'))['db']
    orm_fixture =ORMFixtue(host=db_config["host"], name=db_config["name"],
                           user=db_config["user"], password=db_config["password"])
    return orm_fixture

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json')