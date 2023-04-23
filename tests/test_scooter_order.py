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

    def test_order_flow_from_header_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        base_page = BasePage(self.driver)
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        base_page.click_on_header_order_button()
        order_page.wait_for_load_order_page()
        order_page.full_order_form(order_one)

        main_page.wait_for_load_main_page()

    def test_order_flow_from_main_page_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        main_page.wait_for_load_main_page()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()