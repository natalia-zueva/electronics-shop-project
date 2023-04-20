"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert Item.calculate_total_price(item1) == 200000
    assert Item.calculate_total_price(item2) == 100000


# def test___init__():
#     assert Item.all.append() == [<src.item.Item object at 0x000001AC2DBC4310>, <src.item.Item object at 0x000001AC2D958510>]


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.apply_discount(item1)
    assert item1.price == 8000.0
    # assert Item.apply_discount(item1) == 8000.0
    assert Item.apply_discount(item2) == 10000



