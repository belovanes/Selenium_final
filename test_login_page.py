from .pages.base_page import BasePage
from .pages.login_page import LoginPage

import pytest

LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

@pytest.mark.reg_new_user
def test_register_new_user(self, browser):
    page = LoginPage(browser, LINK)
    page.open()
    page.should_be_register_form()
    page.register_new_user('a5serrt@maillo.com', 'Asdf^%ddff2')
    page.should_not_be_registration_error_messages()
    page.should_be_authorized_user()
