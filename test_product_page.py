import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('promo_link', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
 "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, promo_link):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/" + promo_link
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.check_product_name_on_page_and_product_name_in_cart()
    page.check_product_price_on_page_and_product_price_in_cart()