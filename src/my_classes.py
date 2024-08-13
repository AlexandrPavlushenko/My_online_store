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


class Category:
    """Класс:Категория товара. Свойства: Наименование категории
    Описание категории
    Список товаров в категории"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
