from selenium.webdriver import ActionChains

from ..locators.order_page_locators import *
from ..locators.base_page_locators import *

from ..pages.main_page import MainPage
from ..pages.base_page import BasePage

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(self.driver)
        self.main_page = MainPage(self.driver)

    def wait_for_open_modal_window(self):
        self.base_page.wait_for_element_visibility(order_modal_title)

    def wait_for_load_order_page(self):
        self.base_page.wait_for_element_visibility(order_title)

    def check_successful_order(self):
        title = self.base_page.wait_for_element_visibility(order_modal_title)
        return 'Заказ оформлен' in title.text

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
        self.base_page.wait_for_element_visibility(station_item_button).click()
        ActionChains(self.driver).move_to_element(self.base_page.wait_for_element_clickability(next_button)).click().perform()
        self.base_page.wait_for_element_visibility(date_field).send_keys(order.date)
        ActionChains(self.driver).move_to_element(self.base_page.wait_for_element_visibility(date_item)).click().perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element(*duration_field)).click().perform()
        self.base_page.wait_for_element_visibility((By.XPATH, duration_item_field_locator.format(value=order.duration))).click()
        ActionChains(self.driver).move_to_element(self.driver.find_element(*order_button)).click().perform()

    def check_test_order_flow(self, order):
        self.wait_for_load_order_page()
        self.full_order_form(order)
        self.wait_for_open_modal_window()
        self.click_on_modal_yes_button()

        return self.check_successful_order()

    def check_redirect_to_main_page_after_order(self):
        self.click_on_show_order_button()
        self.base_page.click_on_element(scooter_link)

        return self.main_page.wait_for_load_main_page()