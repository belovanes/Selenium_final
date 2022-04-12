from .base_page import BasePage
from .locators import AddingToBasket

class ProductPage(BasePage):
    def should_be_add_2_basket_button(self):
        assert self.is_element_present(*AddingToBasket.ADD2BASKET_BUTTON), 'Button add to basket not found!'

