from src.item import Item

PATH = r"C:\Users\Admin\PycharmProjects\electronics-shop-project\src\items.csv"

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.__name = 'Смартфон'
    assert item.__name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.__name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv(PATH)  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
