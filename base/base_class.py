from selenium.webdriver.support.wait import WebDriverWait
import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Getters

    def get_page_url(self):
        return self.driver.current_url

    # Actions

    def assert_url(self, url):
        page_url = self.get_page_url()
        assert url == page_url
        print(f'URL {page_url} is correct')

    def assert_text(self, expected_text, current_text):
        assert current_text == expected_text
        print(f'Text {current_text} is correct')

    def get_screenshot(self):
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')
        screenshot_name = 'screenshot' + current_date +'.png'
        self.driver.save_screenshot('C:\\Users\\Bread\\PycharmProjects\\main_project\\screenshots\\' + screenshot_name)
