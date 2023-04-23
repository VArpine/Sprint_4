from selenium.webdriver.common.by import By

accordion_items = [By.XPATH, './/div[@class="accordion__item"]']
accordion_item_locator = './/div[@class="accordion__item"][{number}]//div[@class="accordion__button"]'
accordion_item_panel_locator = './/div[@class="accordion__item"][{number}]//div[@class="accordion__panel"]'

main_header_title = [By.CLASS_NAME, 'Home_Header__iJKdX']
main_page_order_button = [By.XPATH, './/button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM")]']
