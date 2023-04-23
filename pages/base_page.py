from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.base_page_locators import header_order_button, \
    logo_link, scooter_link, yandex_search_bar_button, cookie_button

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_header_order_button(self):
        self.driver.find_element(*header_order_button).click()

    def click_on_header_logo_button(self):
        self.driver.find_element(*logo_link).click()

    def click_on_header_scooter_button(self):
        self.driver.find_element(*scooter_link).click()

    def click_cookie_button(self):
        try:
            self.driver.find_element(*cookie_button).click()
        except NoSuchElementException:
            return False
        return True

    def check_yandex_page_open(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('dzen'))
        assert 'dzen' in self.driver.current_url

    def close_yandex_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])