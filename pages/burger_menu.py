from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.urls import url


class BurgerMenu(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    burger_menu_button = '.bm-burger-button'
    logout_button = '#logout_sidebar_link'
    about_button = '#about_sidebar_link'
    about_url = 'https://saucelabs.com/'

    # Getters

    def get_burger_menu_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.burger_menu_button)))

    def get_logout_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.logout_button)))

    def get_about_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.about_button)))

    # Actions

    def click_burger_menu_button(self):
        self.get_burger_menu_button().click()
        print('Burger menu clicked')

    def click_logout_button(self):
        self.get_logout_button().click()
        print('Logout button clicked')

    def click_about_button(self):
        self.get_about_button().click()
        print('About button clicked')

    # Methods

    def logout(self):
        self.click_burger_menu_button()
        self.click_logout_button()
        self.assert_url(url)

    def about_check(self):
        self.click_burger_menu_button()
        self.click_about_button()
        self.assert_url(self.about_url)
