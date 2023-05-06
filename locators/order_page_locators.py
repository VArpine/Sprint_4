from selenium.webdriver.common.by import By

order_title = [By.XPATH, './/div[@class="Order_Header__BZXOb"]']
name_field = [By.XPATH, './/div[@class="Order_Form__17u6u"]//div[@class="Input_InputContainer__3NykH"][1]//input']
surname_field = [By.XPATH, './/div[@class="Order_Form__17u6u"]//div[@class="Input_InputContainer__3NykH"][2]//input']
address_field = [By.XPATH, './/div[@class="Order_Form__17u6u"]//div[@class="Input_InputContainer__3NykH"][3]//input']
station_field = [By.XPATH, './/div[@class="Order_Form__17u6u"]//div[@class="select-search"]//input']
station_item_button = [By.XPATH, './/button[contains(@class, "Order_SelectOption__82bhS")]']
phone_field = [By.XPATH, './/div[@class="Order_Form__17u6u"]//div[@class="Input_InputContainer__3NykH"][4]//input']
next_button = [By.XPATH, './/div[@class="Order_NextButton__1_rCA"]//button']

date_field = [By.XPATH, './/div[@class="Order_MixedDatePicker__3qiay"]//input']
date_item = [By.XPATH, './/div[contains(@class, "react-datepicker__day--selected")]']
duration_field = [By.XPATH, './/div[@class="Dropdown-control"]']
duration_item_field_locator = './/div[@class="Dropdown-menu"]//div[contains(text(),"{value}")]'
order_button = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]//button[contains(text(),"Заказать")]']
order_show_button = [By.XPATH, './/div[@class="Order_NextButton__1_rCA"]//button[contains(text(),"Посмотреть статус")]']

order_modal_title = [By.XPATH, './/div[@class="Order_ModalHeader__3FDaJ"]']
order_modal_yes_button = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]//button[contains(text(),"Да")]']
