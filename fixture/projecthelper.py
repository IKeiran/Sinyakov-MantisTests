import time
from selenium.webdriver.support.ui import Select
from model import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('Manage').click()

    def open_project_manage_page(self, password):
        wd = self.app.wd
        self.open_manage_page()
        wd.find_element_by_link_text('Manage Projects').click()
        try:
            if wd.find_elements_by_name('password').isDisplayed():
                self.app.session.input_password(password)
                self.app.submit_button_click()
            else:
                pass
        except:
            pass

    def create_button_click(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()

    def fill_project_name(self, project_name):
        self.app.session.send_text('name', project_name)

    def set_combobox_value(self, selector, value):
        wd = self.app.wd
        if value is not None:
            Select(wd.find_element_by_name(selector)).select_by_index(value)

    def fill_status(self, status):
        self.set_combobox_value('status', status)

    def fill_view_status(self, status):
        self.set_combobox_value('view_state', status)

    def fill_description(self, project_name):
        self.app.session.send_text('description', project_name)

    def fill_inherit_global_categiries(self, enable):
        if not enable:
            wd = self.app.wd
            wd.find_element_by_name('inherit_global').click()

    def add_project_button_click(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Add Project"]').click()

    def create(self, user_password, project):
        time.sleep(500)
        wd = self.app.wd
        self.open_project_manage_page(password=user_password)
        self.create_button_click()
        self.fill_project_name(project.name)
        self.fill_status(project.status)
        self.fill_inherit_global_categiries(project.inherit_global_categiries)
        self.fill_view_status(project.view_status)
        self.fill_description(project.description)
        self.add_project_button_click()
        time.sleep(500)
