import pytest


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