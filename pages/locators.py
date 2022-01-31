from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    CART_PRICE = (By.CSS_SELECTOR, "div.alertinner :nth-child(1)>strong")
    PRODUCT_IN_CART_NAME = (By.CSS_SELECTOR, "div.alertinner>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_ADDED_ITEM_MESSAGE = (By.CSS_SELECTOR, "div.alert-success>div.alertinner")

