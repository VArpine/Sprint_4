import pytest
from ..pages.main_page import MainPage
from ..urls.urls import *


@pytest.mark.usefixtures("firefox_driver_init", "use_main_page")
class TestImportantQuestionsBlock:
    def test_questions_open(self):
        self.driver.get(main_page_url)

        self.main_page = MainPage(self.driver)

        all_passed = False

        for number in range(1, self.main_page.get_accordion_items_count()):
            self.main_page.click_on_question_item(number)
            all_passed = self.main_page.check_if_question_item_open(number) is True and \
                         self.main_page.check_if_question_content_is_right(number) is True

        assert all_passed is True and self.main_page.wait_for_load_main_page() is True
