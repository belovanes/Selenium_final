from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

#LINK = "http://selenium1py.pythonanywhere.com/de/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
#LINK = "http://selenium1py.pythonanywhere.com/de/catalogue/the-shellcoders-handbook_209/"
LINK = "http://selenium1py.pythonanywhere.com/ru"


class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    print(f'Now go to basket from main page {browser.current_url}')
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
