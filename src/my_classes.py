class Product:
    """Класс: Товары. Свойства: Наименование товара
    Описание товара
    Цена товара
    Количество товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product: dict):
        """Взвращает созданный объект класса Product из параметров товара в словаре"""
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или орицательная")
        else:
            self.__price = value

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return f"{self.price * self.quantity + other.price * other.quantity} руб."


class Category:
    """Класс:Категория товара. Свойства: Наименование категории
    Описание категории
    Список товаров в категории"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    def add_product(self, product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        count = 0
        for i in self.__products:
            count += i.quantity
        return f"{self.name}, количество продуктов: {count} шт."
