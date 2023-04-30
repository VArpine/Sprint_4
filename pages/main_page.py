from selenium.webdriver import ActionChains
from ..locators.main_page_locators import *
from ..pages.base_page import BasePage
from ..answers.answers import main_page_answers

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(self.driver)

    def get_accordion_items_count(self):
        return len(self.driver.find_elements(*accordion_items))

    def wait_for_load_main_page(self):
        title = self.base_page.wait_for_element_visibility(main_header_title)
        return 'Самокат' in title.text

    def click_on_question_item(self, number):
        accordion_item = [
            By.XPATH,
            accordion_item_locator.format(number=number)
        ]
        item = self.base_page.wait_for_element_visibility(accordion_item)
        self.driver.execute_script("arguments[0].scrollIntoView();", item)
        ActionChains(self.driver).move_to_element(item).click().perform()

    def check_if_question_item_open(self, number):
        accordion_item_panel = [
            By.XPATH,
            accordion_item_panel_locator.format(number=number)
        ]
        return self.driver.find_element(*accordion_item_panel).get_attribute('hidden') == None

    def check_if_question_content_is_right(self, number):
        accordion_item_panel = [
            By.XPATH,
            accordion_item_panel_locator.format(number=number)
        ]
        return self.base_page.wait_for_element_visibility(accordion_item_panel).text == main_page_answers.get(number)

    def click_on_main_page_order_button(self):
        button = self.base_page.wait_for_element_visibility(main_page_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        ActionChains(self.driver).move_to_element(button).click().perform()