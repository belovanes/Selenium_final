from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print('I am test Login Page. Test "login" in current page-URL')
        assert ('/login' in self.browser.current_url), 'URL is not login url!'

    def should_be_login_form(self):
        print('I am test Login Page. Try to find Login form')
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present on Login page'

    def should_be_register_form(self):
        print('I am test Login Page. Try to find Registration form')
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Registration form is not present on Login page'