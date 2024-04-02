from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from faker import Faker


class CustomerInfoPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    faker = Faker('en_US')
    customer_name = faker.first_name()
    customer_lastname = faker.last_name()
    customer_postalcode = faker.postcode()

    # Locators
    name = '#first-name'
    lastname = '#last-name'
    postcode = '#postal-code'
    continue_button = '#continue'
    checkout_final_step_url = 'https://www.saucedemo.com/checkout-step-two.html'

    # Getters

    def get_continue_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.continue_button)))

    def get_name_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.name)))

    def get_lastname_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.lastname)))

    def get_postcode_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.postcode)))

    # Actions
    def enter_name(self):
        self.get_name_field().send_keys(self.customer_name)
        print('Name entered')

    def enter_lastname(self):
        self.get_lastname_field().send_keys(self.customer_lastname)
        print('Lastname entered')

    def enter_postcode(self):
        self.get_postcode_field().send_keys(self.customer_postalcode)
        print('Postal code entered')

    def checkout_click_continue_button(self):
        self.get_continue_button().click()
        print('Proceed checkout final step')

    # Methods
    def checkout_continue(self):
        self.enter_name()
        self.enter_lastname()
        self.enter_postcode()
        self.checkout_click_continue_button()
        self.assert_url(self.checkout_final_step_url)
        self.get_screenshot()
