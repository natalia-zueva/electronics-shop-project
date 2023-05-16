import csv

class InstantiateCSVError(KeyError):
    pass



class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return ValueError



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов')


    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса `Item` данными из файла _src/items.csv
        """
        path = r"../src/items.csv"

        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all.clear()
                for row in reader:
                    item = (cls(row['name'], row['price'], row['quantity']))

        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл items.csv')
        except KeyError:
            print('InstantiateCSVError: Файл item.csv поврежден')





    @staticmethod
    def string_to_number(num):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(num))





