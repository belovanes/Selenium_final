from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement as WE
from .locators import BasePageLocators
import math


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        print(f'Opening page {self.url}')
        self.browser.get(self.url)

    def is_element_present(self, by_method, css_selector) -> WE:
        """if element present on page - return element, else False"""
        try:
            element = self.browser.find_element(by_method, css_selector)
        except NoSuchElementException:
            return False    # да, тут наперекор правилам возвращаем не тот тип, но так надо
        return element #True

    def is_not_element_present(self, by_method, css_selector):
        """ if element NOT present on page - return True, else False"""
        try:
            wait = WebDriverWait(self.browser, 4)
            wait.until(EC.presence_of_element_located((by_method, css_selector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, by_method, css_selector, timeout=4):
        """ ожидание, что элемент (by_method, css_selector) должен пропасть в течение timeout секунд """
        try:
            wait = WebDriverWait(self.browser, timeout, 1, TimeoutException)
            wait.until_not(EC.presence_of_element_located((by_method, css_selector)))
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        """if element login_link is present - return element, else - return False"""
        print('Try to find login link...', end='')
        element = self.is_element_present(*BasePageLocators.LOGIN_LINK)
        assert element, "Login link is not presented"
        print('Ok, login link found')
        return element

    def should_be_basket_link(self):
        """if element basket_link is present - return element, else - return False"""
        print('Try to find link to basket...', end='')
        element = self.is_element_present(*BasePageLocators.BASKET_LINK)
        assert element, "Basket link is not presented"
        print('Ok, basket link found')
        return element

    def should_be_authorized_user(self):
        print('Try to find icon user...', end='')
        assert self.is_element_present(*BasePageLocators.USER_ICON),\
            "User icon is not presented, probably unauthorised user"
        print('Ok, icon found. Authorised user')

    def url_should_contain(self, strparam:str):
        """проверка, что browser.current_url содержит в себе <strparam>"""
        print(f'Verify that current URL contain "{strparam}"...', end='')
        assert strparam in self.browser.current_url, \
            f'Opened wrong page from link:{self.url}. Page link not contain "{strparam}"'
        print('Ok')

    def go_to_login_page(self):
        login_link = self.should_be_login_link()
        print(f'Running method login_link.click from page {self.url}')
        login_link.click()
        assert '/login' in self.browser.current_url, f'Opened not login page from link:{self.url}.'

    def go_to_basket_page(self):
        basket_link = self.should_be_basket_link()
        print(f'Running method basket_link.click from page {self.url}')
        basket_link.click()
        self.url_should_contain('/basket/')

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
