from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from time import sleep
import pytest

LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'

#@pytest.mark.parametrize('num', [*(i for i in range(7)), pytest.param("7", marks=pytest.mark.xfail),'8','9']) #тест с параметром 7 пометим как падающий
def test_guest_can_add_2_basket(browser):
#   cl = f'{LINK}{num}'
#   print(f'Current LINK={cl}')
    page = ProductPage(browser, LINK)
    page.open()
    product_name = page.should_be_product_name()
    product_price = page.should_be_product_price()
    print(f'Page of "{product_name}" book')
    print(f'Book price is {product_price}')
    add_button = page.should_be_add_2_basket_button()
    add_button.click()
    page.solve_quiz_and_get_code()
    sleep(1)
    added_product = page.should_be_sucess_add_message(product_name)
    print(f'Added "{added_product}" to basket')
    added_product_price = page.should_be_correct_price(product_price)
    print(f'Price of added "{added_product}" is {added_product_price}')

@pytest.mark.xfail(reason='Success message must be after add to basket')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    product_name = page.should_be_product_name()
    print(f'Page of "{product_name}" book')
    add_button = page.should_be_add_2_basket_button()
    add_button.click()
    page.solve_quiz_and_get_code()
    sleep(1)
    print(f'Running method should_not_be_success_message')
    page.should_not_be_success_message(product_name)

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    product_name = page.should_be_product_name()
    print(f'Page of "{product_name}" book')
    page.should_not_be_success_message(product_name)

def test_guest_should_see_login_link_on_product_page(browser):
    LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()

def should_be_login_page()_product_page(browser):
    LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    print(f'begining test "should be login page". Browser current URL={browser.current_url}')
    login_page.should_be_login_page()
