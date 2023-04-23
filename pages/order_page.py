from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.order_page_locators import name_field, order_title, \
    surname_field, address_field, station_field, phone_field, \
    next_button, date_field, duration_field, duration_item_field_locator, \
    order_button, order_modal_title, order_modal_button


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_open_modal_window(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(order_modal_title))

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(order_title))

    def check_successful_order(self):
        title = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(order_modal_title))
        assert 'Заказ оформлен' in title.text

    def full_order_form(self, order_one):
        self.driver.find_element(*name_field).send_keys(order_one['name'])
        self.driver.find_element(*surname_field).send_keys(order_one['surname'])
        self.driver.find_element(*address_field).send_keys(order_one['address'])
        self.driver.find_element(*station_field).send_keys(order_one['station'])
        self.driver.find_element(*phone_field).send_keys(order_one['phone'])
        self.driver.find_element(*next_button).click()
        date = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(date_field))
        date.send_keys(order_one['date'])
        actions = ActionChains(self.driver)
        actions.move_to_element(duration_field).click_and_hold(duration_field).perform()