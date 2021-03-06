from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import random

""" Cmd for run tests: pytest -v -s --browser_name=hchrome --tb=line --language=en -m need_review"""

LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    product_name = page.should_be_product_name()
    product_price = page.should_be_product_price()
    add_button = page.should_be_add_2_basket_button()
    print('Click button "Add to basket"')
    add_button.click()
    #page.solve_quiz_and_get_code()
    added_product = page.should_be_success_add_message(product_name)
    print(f'Added "{added_product}" to basket')
    added_product_price = page.should_be_correct_price(product_price)
    print(f'Price of added "{added_product}" is {added_product_price}')

@pytest.mark.xfail(reason='Success message must be after add to basket')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    product_name = page.should_be_product_name()
    add_button = page.should_be_add_2_basket_button()
    add_button.click()
    #page.solve_quiz_and_get_code()
    page.should_not_be_success_message(product_name)

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    product_name = page.should_be_product_name()
    page.should_not_be_success_message(product_name)

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    print(f'Now go to "basket" from product page {browser.current_url}')
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        registration_page = LoginPage(browser, browser.current_url)
        registration_page.should_be_login_page()
        email = str(random.randint(1, 999))+'user'+str(random.randint(1, 999))+'@mail.dot.com'
        password = 'AsDfGh!2#4%'
        registration_page.register_new_user(email, password)
        registration_page.should_not_be_registration_error_messages()


    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_be_authorized_user()
        product_name = page.should_be_product_name()
        page.should_not_be_success_message(product_name)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_be_authorized_user()
        product_name = page.should_be_product_name()
        product_price = page.should_be_product_price()
        add_button = page.should_be_add_2_basket_button()
        print('Click button "Add to basket"')
        add_button.click()
        added_product = page.should_be_success_add_message(product_name)
        print(f'Added "{added_product}" to basket')
        added_product_price = page.should_be_correct_price(product_price)
        print(f'Price of added "{added_product}" is {added_product_price}')
