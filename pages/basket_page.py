from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def should_not_be_items_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is noy empty"

	def should_be_message_about_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Message about empty basket not found"
