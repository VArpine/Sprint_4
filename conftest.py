import pytest
from selenium import webdriver
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.order_page import OrderPage


class Order:
    def __init__(self, name, surname, address, station, phone, date, duration):
        self.name = name
        self.surname = surname
        self.address = address
        self.station = station
        self.phone = phone
        self.date = date
        self.duration = duration


@pytest.fixture # фикстура, которая создаёт заказ
def order_one():
    order_one = Order(
        name='Тест',
        surname='Тестов',
        address='ул. Мира 105',
        station='ВДНХ',
        phone='+79119999999',
        date='14.05.2023',
        duration='двое суток'
    )

    return order_one


@pytest.fixture # фикстура, которая создаёт заказ
def order_two():
    order_two = Order(
        name='Сергей',
        surname='Сергеев',
        address='ул. Бауманская 2',
        station='Бауманская',
        phone='+79219999988',
        date='12.05.2023',
        duration='трое суток'
    )

    return order_two


@pytest.fixture(scope="class")
def firefox_driver_init(request):
    firefox_driver = webdriver.Firefox()
    request.cls.driver = firefox_driver

    yield

    firefox_driver.quit()

@pytest.fixture(scope="class")
def use_base_page(request):
    request.cls.base_page = BasePage(request.cls.driver)

@pytest.fixture(scope="class")
def use_main_page(request):
    request.cls.main_page = MainPage(request.cls.driver)

@pytest.fixture(scope="class")
def use_order_page(request):
    request.cls.order_page = OrderPage(request.cls.driver)