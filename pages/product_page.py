from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def should_be_product_price(self):
            assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_basket_product_name(self):
        product_name_alerts = self.browser.find_elements(*ProductPageLocators.BASKET_PRODUCT_NAME)
        return product_name_alerts[0].text

    def get_basket_product_price(self):
        product_price_alert = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE)
        return product_price_alert.text

    def check_basket_product_price(self, product_price, basket_product_price):
        assert product_price == basket_product_price, "Wrong amount in basket"

    def check_basket_product_name(self, product_name, basket_product_name):
        assert product_name == basket_product_name, "Wrong product name in basket"



