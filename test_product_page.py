from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.check_product_name_on_page_and_product_name_in_cart()
    page.check_product_price_on_page_and_product_price_in_cart()