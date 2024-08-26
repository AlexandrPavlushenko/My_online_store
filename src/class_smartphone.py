from src.my_classes import Product


class Smartphone(Product):
    """Класс для представления категории <<Смартфоны>>.
    :arg name - Наименование товара
    :arg description - Описание товара
    :arg price - Цена товара
    :arg quantity - Количество товара
    :arg efficiency - Производительность
    :arg model - Модель
    :arg memory - Объем встроенной памяти
    :arg color - цвет"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
