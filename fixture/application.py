# -*- coding: utf-8 -*-

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.projecthelper import ProjectHelper
from fixture.james import JamesHelper

class Application:

    def __init__(self, browser, config):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser =='chrome':
            self.wd = webdriver.Chrome()
        elif browser =='ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.base_url = config['web']["baseUrl"]
        self.config = config
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.project = ProjectHelper(self)
        self.go_to_main_page()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def go_to_main_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()