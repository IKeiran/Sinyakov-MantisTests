from selenium.common.exceptions import NoSuchElementException

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def send_text(self, locator, text):
        wd = self.app.wd
        wd.find_element_by_name(locator).click()
        wd.find_element_by_name(locator).clear()
        wd.find_element_by_name(locator).send_keys(text)

    def input_login(self, login):
        self.send_text("username", login)

    def input_password(self, password):
        self.send_text("password", password)

    def submit_button_click(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def login_as(self, username, password):
        if not self.is_logged_in_as(username):
            self.app.go_to_main_page()
            self.input_login(username)
            self.input_password(password)
            self.submit_button_click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text('Logout')) > 0

    def get_logged_user(self):
        wd = self.app.wd
        try:
            return wd.find_element_by_css_selector("td.login-info-left span").text
        except NoSuchElementException:
            return None

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, userpassword):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login_as(username, userpassword)

