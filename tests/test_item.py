"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


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
    assert item.name == "Смартфон"
    item = Item('СуперСмартфон', 10000, 5)
    assert print('Длина наименования товара превышает 10 символов')


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

