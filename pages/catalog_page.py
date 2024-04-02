from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_to_cart_from_page_button = '#add-to-cart'
    cart_button = '#shopping_cart_container'
    item_title = '.inventory_details_name.large_size'

    # Getters

    def get_item(self, item):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, item)))

    def get_item_cart_button(self, item_button):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, item_button)))

    def get_cart_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.cart_button)))

    def get_item_name_from_page(self):
        return self.get_item(self.item_title).text

    def get_item_name_in_cart(self, item_name_cart):
        return self.get_item(item_name_cart).text

    # Actions

    def go_to_item_page(self, item):
        self.get_item(item).click()
        print('Moved to item page')

    def click_add_to_cart_button(self, item_button):
        self.get_item_cart_button(item_button).click()
        print('Item added to cart from page')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Moved to cart')

    # Methods
    def add_item_from_product_page(self, item, item_url, item_name_cart):
        self.go_to_item_page(item)
        title_1 = self.get_item_name_from_page()
        self.assert_url(item_url)
        self.click_add_to_cart_button(self.add_to_cart_from_page_button)
        self.click_cart_button()
        title_2 = self.get_item_name_in_cart(item_name_cart)
        self.assert_text(title_1, title_2)
