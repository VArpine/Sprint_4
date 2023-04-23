from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.main_page_locators import accordion_items, \
    accordion_item_locator, \
    accordion_item_panel_locator, \
    main_header_title, \
    main_page_order_button

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_accordion_items_count(self):
        return len(self.driver.find_elements(*accordion_items))

    def wait_for_load_main_page(self):
        title = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(main_header_title))
        assert 'Самокат' in title.text

    def click_on_question_item(self, number):
        accordion_item = [
            By.XPATH,
            accordion_item_locator.format(number=number)
        ]
        item = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(accordion_item))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # self.driver.execute_script("arguments[0].scrollIntoView();", item)
        ActionChains(self.driver).move_to_element(item).click().perform()

    def check_if_question_item_open(self, number):
        accordion_item_panel = [
            By.XPATH,
            accordion_item_panel_locator.format(number=number)
        ]
        assert self.driver.find_element(*accordion_item_panel).get_attribute('hidden') == None

    def click_on_main_page_order_button(self):
        button = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(main_page_order_button))
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        ActionChains(self.driver).move_to_element(button).click().perform()