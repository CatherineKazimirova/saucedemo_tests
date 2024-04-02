from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import utilities.userdata


class LoginPage(Base):
    url = 'https://www.saucedemo.com/'
    catalog_url = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    username_field = 'user-name'
    password_field = 'password'
    login_button = 'login-button'
    title_locator = "span[class='title']"
    title_text = 'Products'

    # Getters

    def get_username_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, self.username_field)))

    def get_password_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, self.password_field)))

    def get_login_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, self.login_button)))

    def get_title_text(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.title_locator))).text

    # Actions

    def input_username(self, login):
        self.get_username_field().send_keys(login)
        print('Login entered')

    def input_password(self, password):
        self.get_password_field().send_keys(password)
        print('Password entered')

    def click_login_button(self):
        self.get_login_button().click()
        print('Login button clicked')

    # Methods
    def authorization(self, login):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.assert_url(self.url)
        self.input_username(login)
        self.input_password(utilities.userdata.password)
        self.click_login_button()
        self.assert_url(self.catalog_url)
        self.assert_text(self.title_text, self.get_title_text())
