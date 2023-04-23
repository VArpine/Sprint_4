from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.base_page_locators import header_order_button, \
    logo_link, \
    scooter_link

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_header_order_button(self):
        self.driver.find_element(*header_order_button).click()

    def click_on_header_logo_button(self):
        self.driver.find_element(*logo_link).click()

    def click_on_header_scooter_button(self):
        self.driver.find_element(*scooter_link).click()