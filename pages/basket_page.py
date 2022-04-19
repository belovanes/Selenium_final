from .base_page import BasePage
from .locators import BasketPageLocators
class BasketPage(BasePage):
    def should_be_empty_basket(self):
        print('TEST: Basket should be empty')
        self.should_be_basket_url()
        self.should_be_no_item_in_basket()
        self.should_be_empty_basket_message()

    def should_be_basket_url(self):
        self.url_should_contain('/basket/')

    def should_be_no_item_in_basket(self):
        print('Verify that no items in basket...', end='')
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET),\
            f'Opened basket_page from link {self.url}, and found some item in it. But should be empty.'
        print('Ok')

    def should_be_empty_basket_message(self):
        print('Verify "Empty basket message"...', end='')
        message_empty_basket = self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert message_empty_basket,\
            f'Message "Empty basket" not found. Tried to find {BasketPageLocators.EMPTY_BASKET_MESSAGE}'
        print(f'Ok, found message "{message_empty_basket.text}"')
