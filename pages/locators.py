from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini>span>a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div[id = 'content_inner']>p")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='registration-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='registration-password1']")
    PASSWORD_REPEAT = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    SUBMIT_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    CART_PRICE = (By.CSS_SELECTOR, "div.alertinner :nth-child(1)>strong")
    PRODUCT_IN_CART_NAME = (By.CSS_SELECTOR, "div.alertinner>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_ADDED_ITEM_MESSAGE = (By.CSS_SELECTOR, "div.alert-success>div.alertinner")

