import pytest
import random
import string

from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
registration_link = "http://selenium1py.pythonanywhere.com/accounts/login/"

class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.letters = string.ascii_lowercase
        self.rand_email = ''.join(random.choice(self.letters) for i in range(8)) + '@gmail.com'
        self.rand_password = ''.join(random.choice(self.letters) for i in range(9))
        self.registration_page = LoginPage(browser, registration_link)
        self.registration_page.open()
        self.registration_page.register_new_user(self.rand_email, self.rand_password)
        self.registration_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.test_guest_cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_cart_button()
        page.click_add_to_cart_button()
        page.check_product_name_on_page_and_product_name_in_cart()
        page.check_product_price_on_page_and_product_price_in_cart()

@pytest.mark.need_review
@pytest.mark.parametrize('promo_link', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                         "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6",
                         pytest.param("?promo=offer7", marks=pytest.mark.xfail(reason="bug on a temporary promo page")),
                         "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo_link):
    url = link + promo_link
    page = ProductPage(browser, url)
    page.open()
    page.should_be_add_to_cart_button()
    page.click_add_to_cart_button()
    page.solve_allert_quiz()
    page.check_product_name_on_page_and_product_name_in_cart()
    page.check_product_price_on_page_and_product_price_in_cart()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.click_add_to_cart_button()
    page.test_guest_cant_see_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.click_add_to_cart_button()
    page.test_success_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_about_empty_basket()
