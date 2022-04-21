from .base_page import BasePage
from .locators import AddingToBasket


class ProductPage(BasePage):
    def should_be_add_2_basket_button(self):
        print('Try to find "Add to basket" button...', end='')
        button = self.is_element_present(*AddingToBasket.ADD2BASKET_BUTTON)
        assert button, 'Button add to basket not found!'
        print(f'Ok, button found, text="{button.text}"')
        return button

    def should_be_product_name(self):
        print('Try to find product name...', end='')
        product_name = self.is_element_present(*AddingToBasket.PRODUCT_NAME)
        assert product_name, 'Book name not found on product page!'
        print(f'Ok, found product_name="{product_name.text}"')
        return product_name.text

    def should_be_product_price(self):
        print('Try to find product price...', end='')
        product_price = self.is_element_present(*AddingToBasket.PRODUCT_PRICE)
        assert product_price, 'Price not found on product page!'
        print(f'Ok, found product_price="{product_price.text}"')
        return product_price.text.split()[0]

    def should_be_success_add_message(self, product_name):
        message = self.is_element_present(*AddingToBasket.ADDED_PRODUCT_MESSAGE).text
        if message != product_name:
            print(f'Product name "{product_name}" from product page not equal product "{message}" in basket')
        assert message == product_name, 'Added wrong product name to basket!'
        return message

    def should_be_correct_price(self, product_price):
        price = self.is_element_present(*AddingToBasket.ADDED_PRODUCT_PRICE).text.split()[0]
        assert price == product_price, 'Added product with wrong price!'
        return price

    def should_not_be_success_message(self, product_name):
        print('Try to find success message...', end='')
        assert self.is_not_element_present(*AddingToBasket.ADDED_PRODUCT_MESSAGE), 'Success message found, but not should be!'
        print('Ok, success message not found.')


