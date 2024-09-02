from src.my_classes import Product


class Order:
    """Класс: Заказ товара.
    :arg product - Товар, который был куплен
    :arg quantity - Количество купленного товара
    :arg total_price - Итоговая стоимость заказа"""

    def __init__(self, product: Product, quantity: int) -> None:
        super().__init__()
        if quantity <= 0:
            raise ValueError("Количество должно быть больше нуля")
        if quantity > product.quantity:
            raise ValueError("Недостаточное количество товара на складе")

        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

        product.quantity -= quantity  # Уменьшаем количество товара на складе после заказа

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, Количество: {self.quantity}, Итоговая стоимость: {self.total_price} руб."
