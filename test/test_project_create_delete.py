import random
from model.project import Project


def test_project_create(app):
    app.session.login_as("administrator", "root")
    old_list = app.soap.get_project_list("administrator", "root")
    new_project = Project.generate_random()
    app.project.create(project=new_project)
    old_list.append(new_project)
    new_list = app.soap.get_project_list("administrator", "root")
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)


def test_project_delete(app):
    app.session.login_as("administrator", "root")
    if app.project.get_count() == 0:
        app.project.create(Project.generate_random())
    old_list = app.soap.get_project_list("administrator", "root")
    project = random.choice(old_list)
    app.project.delete_by_id(project.id)
    new_list = old_list
    new_list.remove(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)

