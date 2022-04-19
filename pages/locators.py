from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REG_FORM = (By.CSS_SELECTOR, 'form#register_form')
    REG_LOGIN = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    REG_MESSAGE_ERROR = (By.CSS_SELECTOR, '.alert-danger')


class BasketPageLocators():
    ITEM_IN_BASKET = (By.CSS_SELECTOR, 'div.basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')

class AddingToBasket():
    ADD2BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div .product_main .price_color')
    ADDED_PRODUCT_MESSAGE = (By.CSS_SELECTOR, 'div#messages :nth-child(1) .alertinner strong')
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, 'div#messages :nth-child(3) .alertinner strong')