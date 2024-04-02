import pytest
from pages.login_page import LoginPage
from pages.burger_menu import BurgerMenu
from utilities.userdata import users


@pytest.mark.run(order=2)
def test_about_link(set_up):
    driver = set_up
    login = LoginPage(driver)
    login.authorization(users[1])

    about = BurgerMenu(driver)
    about.about_check()
