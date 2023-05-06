import pytest

from ..urls.urls import *
from ..locators.base_page_locators import *


@pytest.mark.usefixtures("firefox_driver_init", "use_base_page", "use_main_page", "use_order_page")
class TestImportantQuestionsBlock:
    def test_order_one_flow_from_header_button(self, order_one):
        self.driver.get(main_page_url)

        self.base_page.click_cookie_button()
        self.base_page.click_on_element(header_order_button)

        assert self.order_page.check_test_order_flow(order_one) is True and \
               self.order_page.check_redirect_to_main_page_after_order() is True and \
               self.base_page.check_redirect_to_yandex_page_after_order() is True

        self.base_page.close_yandex_page()

    def test_order_two_flow_from_header_button(self, order_two):
        self.driver.get(main_page_url)
        self.base_page.click_cookie_button()
        self.base_page.click_on_element(header_order_button)

        assert self.order_page.check_test_order_flow(order_two) is True and \
               self.order_page.check_redirect_to_main_page_after_order() is True and \
               self.base_page.check_redirect_to_yandex_page_after_order() is True

        self.base_page.close_yandex_page()

    def test_order_one_flow_from_main_page_button(self, order_one):
        self.driver.get(main_page_url)
        self.base_page.click_cookie_button()
        self.main_page.click_on_main_page_order_button()

        assert self.order_page.check_test_order_flow(order_one) is True and \
               self.order_page.check_redirect_to_main_page_after_order() is True and \
               self.base_page.check_redirect_to_yandex_page_after_order() is True

        self.base_page.close_yandex_page()

    def test_order_two_flow_from_main_page_button(self, order_two):
        self.driver.get(main_page_url)
        self.base_page.click_cookie_button()
        self.main_page.click_on_main_page_order_button()

        assert self.order_page.check_test_order_flow(order_two) is True and \
               self.order_page.check_redirect_to_main_page_after_order() is True and \
               self.base_page.check_redirect_to_yandex_page_after_order() is True

        self.base_page.close_yandex_page()
