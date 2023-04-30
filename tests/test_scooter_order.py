import pytest

from ..urls.urls import *
from ..locators.base_page_locators import *

@pytest.mark.usefixtures("firefox_driver_init", "use_base_page", "use_main_page", "use_order_page")
class TestImportantQuestionsBlock:
    def test_order_one_flow_from_header_button(self, order_one):
        self.driver.get(main_page_url)

        self.base_page.click_cookie_button()
        self.base_page.click_on_element(header_order_button)

        assert self.check_test_order_flow(order_one) == True
        assert self.check_redirect_to_main_page_after_order() == True
        assert self.check_redirect_to_yandex_page_after_order() == True
        self.close_yandex_page()

    def test_order_two_flow_from_header_button(self, order_two):
        self.driver.get(main_page_url)
        self.base_page.click_cookie_button()
        self.base_page.click_on_element(header_order_button)

        assert self.check_test_order_flow(order_two) == True
        assert self.check_redirect_to_main_page_after_order() == True
        assert self.check_redirect_to_yandex_page_after_order() == True
        self.close_yandex_page()

    def test_order_one_flow_from_main_page_button(self, order_one):
        self.driver.get(main_page_url)
        self.base_page.click_cookie_button()
        self.main_page.click_on_main_page_order_button()

        assert self.check_test_order_flow(order_one) == True
        assert self.check_redirect_to_main_page_after_order() == True
        assert self.check_redirect_to_yandex_page_after_order() == True
        self.close_yandex_page()

    def test_order_two_flow_from_main_page_button(self, order_two):
        self.driver.get(main_page_url)
        self.base_page.click_cookie_button()
        self.main_page.click_on_main_page_order_button()

        assert self.check_test_order_flow(order_two) == True
        assert self.check_redirect_to_main_page_after_order() == True
        assert self.check_redirect_to_yandex_page_after_order() == True
        self.close_yandex_page()

    def check_test_order_flow(self, order):
        self.order_page.wait_for_load_order_page()
        self.order_page.full_order_form(order)
        self.order_page.wait_for_open_modal_window()
        self.order_page.click_on_modal_yes_button()

        return self.order_page.check_successful_order()

    def check_redirect_to_main_page_after_order(self):
        self.order_page.click_on_show_order_button()
        self.base_page.click_on_element(scooter_link)

        return self.main_page.wait_for_load_main_page()

    def check_redirect_to_yandex_page_after_order(self):
        self.base_page.click_on_element(logo_link)

        return self.base_page.check_yandex_page_open()

    def close_yandex_page(self):
        self.base_page.close_yandex_page()