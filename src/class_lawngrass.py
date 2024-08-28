from src.my_classes import Product


class LawnGrass(Product):
    """Класс для представления категории <<Трава газонная>>.
    :arg name - Наименование товара
    :arg description - Описание товара
    :arg price - Цена товара
    :arg quantity - Количество товара
    :arg country - Страна-производитель
    :arg germination_period - Срок прорастания
    :arg color - Цвет"""
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
