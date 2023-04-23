from selenium import webdriver

from ..conftest import order_one
from ..pages.main_page import MainPage
from ..pages.order_page import OrderPage
from ..pages.base_page import BasePage


class TestImportantQuestionsBlock:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_order_one_flow_from_header_button(self, order_one):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        base_page = BasePage(self.driver)
        base_page.click_cookie_button()
        base_page.click_on_header_order_button()

        self.order_test_flow(order_one)

    def test_order_two_flow_from_header_button(self, order_two):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        base_page = BasePage(self.driver)
        base_page.click_cookie_button()
        base_page.click_on_header_order_button()

        self.order_test_flow(order_two)

    def test_order_one_flow_from_main_page_button(self, order_one):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        base_page = BasePage(self.driver)
        base_page.click_cookie_button()

        main_page = MainPage(self.driver)
        main_page.click_on_main_page_order_button()

        self.order_test_flow(order_one)

    def test_order_two_flow_from_main_page_button(self, order_two):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        base_page = BasePage(self.driver)
        base_page.click_cookie_button()

        main_page = MainPage(self.driver)
        main_page.click_on_main_page_order_button()

        self.order_test_flow(order_two)

    def order_test_flow(self, order):
        base_page = BasePage(self.driver)
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        order_page.wait_for_load_order_page()
        order_page.full_order_form(order)
        order_page.wait_for_open_modal_window()
        order_page.click_on_modal_yes_button()
        order_page.check_successful_order()
        order_page.click_on_show_order_button()
        base_page.click_on_header_scooter_button()
        main_page.wait_for_load_main_page()
        base_page.click_on_header_logo_button()
        base_page.check_yandex_page_open()
        base_page.close_yandex_page()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()