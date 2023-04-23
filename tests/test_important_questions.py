from selenium import webdriver
from ..pages.main_page import MainPage

class TestImportantQuestionsBlock:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_questions_open(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPage(self.driver)

        for number in range(1, main_page.get_accordion_items_count()):
            main_page.click_on_question_item(number)
            main_page.check_if_question_item_open(number)

        main_page.wait_for_load_main_page()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()