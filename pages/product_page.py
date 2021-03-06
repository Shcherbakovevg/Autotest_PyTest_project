from .base_page import BasePage
from selenium.webdriver.common.by import By

from .locators import ProductPageLocators

class ProductPage(BasePage):

    def check_product_name_on_page_and_product_name_in_cart(self):
        self.should_be_product_name()
        self.should_be_product_name_in_cart()
        self.should_equal_product_names()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name not found"

    def should_be_product_name_in_cart (self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_CART_NAME), "Product name added to cart not found"

    def should_equal_product_names(self):
        Product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        Product_name_in_cart = self.browser.find_elements(*ProductPageLocators.PRODUCT_IN_CART_NAME)
        assert Product_name == Product_name_in_cart[0].text, "Product name not equal"

    def check_product_price_on_page_and_product_price_in_cart(self):
        self.should_be_product_price()
        self.should_be_product_price_in_cart()
        self.should_equal_product_price()    

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price not found"

    def should_be_product_price_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRICE), "Cart price not found"

    def should_equal_product_price(self):
        Product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        Cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert Product_price == Cart_price, "Product price not equal" 

    def click_add_to_cart_button(self):
        assert self.click_element(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button can't click"

    def solve_allert_quiz(self):
        assert self.solve_quiz_and_get_code(), "Allert code not found"

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button not found"

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_ITEM_MESSAGE), "Success message is present, but should not be"

    def test_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADDED_ITEM_MESSAGE), "Success message don't desappeared"