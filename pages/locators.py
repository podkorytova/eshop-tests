from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

#class MainPageLocators():
 #   LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR,".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".col-sm-6.product_main p.price_color")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR,"#messages .alert-success strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR,".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages .alert-success strong")
