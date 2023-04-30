import pytest
from ..pages.main_page import MainPage
from ..urls.urls import *

@pytest.mark.usefixtures("firefox_driver_init", "use_main_page")
class TestImportantQuestionsBlock:
    def test_questions_open(self):
        self.driver.get(main_page_url)

        self.main_page = MainPage(self.driver)

        for number in range(1, self.main_page.get_accordion_items_count()):
            self.main_page.click_on_question_item(number)
            assert self.main_page.check_if_question_item_open(number) == True
            assert self.main_page.check_if_question_content_is_right(number) == True

        assert self.main_page.wait_for_load_main_page() == True