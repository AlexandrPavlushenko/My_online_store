from src.class_base_product import BaseProduct, BaseEntity
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс: Товары.
    :arg name - Наименование товара
    :arg description - Описание товара
    :arg price - Цена товара
    :arg quantity - Количество товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, new_product: dict):
        """Взвращает созданный объект класса Product из параметров товара в словаре"""
        return cls(**new_product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или орицательная")
        else:
            self.__price = value

    def __add__(self, other) -> str:
        if type(other) is self.__class__:
            return f"{self.price * self.quantity + other.price * other.quantity} руб."
        raise TypeError


class Category(BaseEntity):
    """Класс:Категория товара.
    :arg name - Наименование категории
    :arg description - Описание категории
    :arg products - Список товаров в категории"""

    category_count = 0  # Счетчик товаров в категории
    product_count = 0  # Общий счетчик товаров

    def __init__(self, name: str, description: str, products: list) -> None:
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}| "
        return products_str

    def add_product(self, product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def __str__(self) -> str:
        count = 0
        for i in self.__products:
            count += i.quantity
        return f"{self.name}, количество продуктов: {count} шт."
