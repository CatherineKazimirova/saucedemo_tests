import pytest
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.checkout_finish_page import CheckoutFinishPage
from pages.customer_info_page import CustomerInfoPage
from pages.login_page import LoginPage
from pages.burger_menu import BurgerMenu
from utilities.userdata import users
import utilities.locators
import utilities.urls


@pytest.mark.skip()
def test_standard_order_3_items(set_up):
    driver = set_up
    for i in range(len(utilities.locators.products)):
        login = LoginPage(driver)
        login.authorization(users[1])

        catalog_page = CatalogPage(driver)
        catalog_page.add_item_from_product_page(item=utilities.locators.products[i][0],
                                                item_url=utilities.locators.products[i][1],
                                                item_name_cart=utilities.locators.products[i][2])

        cart = CartPage(driver)
        cart.checkout_move_to_customer_page()

        customer_info = CustomerInfoPage(driver)
        customer_info.checkout_continue()

        finish_order = CheckoutFinishPage(driver)
        finish_order.checkout_finish()

        logout = BurgerMenu(driver)
        logout.logout()


@pytest.mark.run(order=1)
def test_standard_order_one_item(set_up):
    driver = set_up
    login = LoginPage(driver)
    login.authorization(users[1])

    catalog_page = CatalogPage(driver)
    catalog_page.add_item_from_product_page(item=utilities.locators.products[0][0],
                                            item_url=utilities.locators.products[0][1],
                                            item_name_cart=utilities.locators.products[0][2])

    cart = CartPage(driver)
    cart.checkout_move_to_customer_page()

    customer_info = CustomerInfoPage(driver)
    customer_info.checkout_continue()

    finish_order = CheckoutFinishPage(driver)
    finish_order.checkout_finish()

    logout = BurgerMenu(driver)
    logout.logout()

