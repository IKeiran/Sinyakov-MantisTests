import time
from selenium.webdriver.support.ui import Select
from model.project import Project
from selenium.common.exceptions import NoSuchElementException


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('Manage').click()

    def open_project_manage_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/manage_proj_page.php")):
            self.open_manage_page()
            wd.find_element_by_link_text('Manage Projects').click()

    def create_button_click(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()

    def fill_project_name(self, project_name):
        self.app.session.send_text('name', project_name)

    def set_combobox_value_by_index(self, selector, index):
        wd = self.app.wd
        if index is not None:
            Select(wd.find_element_by_name(selector)).select_by_index(index)

    def set_combobox_value_by_text(self, selector, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(selector)).select_by_visible_text(text)

    def fill_status(self, status):
        self.set_combobox_value_by_text('status', status)

    def fill_view_status(self, status):
        self.set_combobox_value_by_text('view_state', status)

    def fill_description(self, project_name):
        self.app.session.send_text('description', project_name)

    def fill_inherit_global_categories(self, enable):
        if not enable:
            wd = self.app.wd
            wd.find_element_by_name('inherit_global').click()

    def add_project_button_click(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Add Project"]').click()

    def create(self, project):
        self.open_project_manage_page()
        self.create_button_click()
        self.fill_project_name(project.name)
        self.fill_status(project.status)
        self.fill_inherit_global_categories(project.inherit_global_categories)
        self.fill_view_status(project.view_status)
        self.fill_description(project.description)
        self.add_project_button_click()

    def get_project_list_table(self):
        try:
            result = self.app.wd.find_elements_by_css_selector("table[class='width100']")[1]
        except:
            result = list()
        return result

    def get_project_id(self, cell):
        id = cell.find_element_by_css_selector('a').get_attribute('href')
        id = id[id.find('=')+1:]
        return id

    def get_project_list(self):
        self.open_project_manage_page()
        table = self.get_project_list_table()
        projects = list()
        for row in table.find_elements_by_css_selector('tr')[2:]:
            cells = row.find_elements_by_css_selector('td')
            project_id = self.get_project_id(cells[0])
            project_name = cells[0].text
            project_status = cells[1].text
            project_view_status = cells[3].text
            project_description = cells[4].text
            project = Project(id=project_id, name=project_name, status=project_status,
                              view_status=project_view_status, description=project_description)
            projects.append(project)
        return projects

    def get_count(self):
        self.open_project_manage_page()
        table = self.get_project_list_table()
        try:
            count = len(table.find_elements_by_css_selector('tr')) - 2
        except NoSuchElementException:
            count = 0
        return count

    def open_project_edit_page(self, id):
        self.open_project_manage_page()
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s'] " % id).click()

    def delete_button_click(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()

    def delete_by_id(self, id):
        self.open_project_edit_page(id=id)
        self.delete_button_click()
        self.delete_button_click()



