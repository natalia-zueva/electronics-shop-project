"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item, InstantiateCSVError
from src.phone import Phone
import pytest


def test__repr__():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test__str__():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == 'Смартфон'


def test__add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert phone1 + 10 == ValueError


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert Item.calculate_total_price(item1) == 200000
    assert Item.calculate_total_price(item2) == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    item2 = Item("Ноутбук", 20000, 5)
    assert item2.price == 20000


def test_name():
    item = Item('Смартфон', 10000, 5)
    item.name = "Телефон"
    assert item.name == "Телефон"
    with pytest.raises(Exception):
        item.name = "Супер_Телефон"


def test_instantiate_from_csv():
    # Item.instantiate_from_csv()
    # assert len(Item.all) == 5
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path="нет такого файла")

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path=r"src/items.csv")





def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5









