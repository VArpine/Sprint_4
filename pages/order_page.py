from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.order_page_locators import name_field, order_title, \
    surname_field, address_field, station_field, phone_field, \
    next_button, date_field, duration_field, duration_item_field_locator, \
    order_button, order_modal_title, order_modal_yes_button, \
    station_item_button, date_item, order_show_button


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

    def click_on_show_order_button(self):
        self.driver.find_element(*order_show_button).click()

    def click_on_modal_yes_button(self):
        self.driver.find_element(*order_modal_yes_button).click()

    def full_order_form(self, order):
        self.driver.find_element(*name_field).send_keys(order.name)
        self.driver.find_element(*surname_field).send_keys(order.surname)
        self.driver.find_element(*address_field).send_keys(order.address)
        self.driver.find_element(*phone_field).send_keys(order.phone)
        self.driver.find_element(*station_field).send_keys(order.station)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(station_item_button)).click()
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(next_button))).click().perform()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(date_field)).send_keys(order.date)
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(date_item))).click().perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element(*duration_field)).click().perform()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, duration_item_field_locator.format(value=order.duration)))).click()
        ActionChains(self.driver).move_to_element(self.driver.find_element(*order_button)).click().perform()