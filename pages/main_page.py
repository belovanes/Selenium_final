from .base_page import BasePage
from selenium.webdriver.common.by import By
#from mylib.py import myprint
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        print('Method login_link click from Main page')
        login_link.click()
        assert '/login' in self.browser.current_url, 'Opened not login page from main page'


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"