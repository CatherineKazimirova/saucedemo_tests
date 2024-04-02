from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkout_button = '#checkout'
    checkout_step_1_url = 'https://www.saucedemo.com/checkout-step-one.html'

    # Getters

    def get_checkout_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.checkout_button)))

    # Actions

    def checkout_click_button(self):
        self.get_checkout_button().click()
        print('Proceed checkout')

    # Methods
    def checkout_move_to_customer_page(self):
        self.checkout_click_button()
        self.assert_url(self.checkout_step_1_url)



