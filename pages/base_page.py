from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math
""" run with cmd: pytest -v -s --tb=line --language=en test_main_page.py"""

class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by_method, css_selector):
        """if element present on page - return element, else False"""
        try:
            element = self.browser.find_element(by_method, css_selector)
        except NoSuchElementException:
            return False
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
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
            login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
            print(f'Running method login_link.click from page {self.url}')
            login_link.click()
            assert '/login' in self.browser.current_url, f'Opened not login page from link:{self.url}.'

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