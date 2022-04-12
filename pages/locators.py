from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, 'form#register_form')

class AddingToBasket():
    ADD2BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div .product_main .price_color')
    ADDED_PRODUCT_MESSAGE = (By.CSS_SELECTOR, 'div#messages :nth-child(1) .alertinner strong')
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, 'div#messages :nth-child(3) .alertinner strong')