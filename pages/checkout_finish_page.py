from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CheckoutFinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    finish_button = '#finish'
    checkout_order_confirm_url = 'https://www.saucedemo.com/checkout-complete.html'

    # Getters

    def get_finish_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.finish_button)))

    # Actions
    def click_finish_button(self):
        self.get_finish_button().click()
        print('Finish order button clicked')

    # Methods
    def checkout_finish(self):
        self.click_finish_button()
        self.assert_url(self.checkout_order_confirm_url)


