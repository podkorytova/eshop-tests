from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Product is presented, but should not be"

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not presented"
