from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR,"#basket_formset1")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR,"#content_inner>p")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR,".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".col-sm-6.product_main p.price_color")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR,"#messages .alert-success strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR,".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages .alert-success strong")


