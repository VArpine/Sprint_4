from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.base_page_locators import *

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visibility(self, locator):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return element

    def wait_for_element_clickability(self, locator):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return element

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def click_cookie_button(self):
        try:
            self.driver.find_element(*cookie_button).click()
        except NoSuchElementException:
            return False
        return True

    def check_yandex_page_open(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('dzen'))
        return 'dzen' in self.driver.current_url

    def check_redirect_to_yandex_page_after_order(self):
        self.click_on_element(logo_link)

        return self.check_yandex_page_open()

    def close_yandex_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])