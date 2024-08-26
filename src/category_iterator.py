from src.my_classes import Category


class CategoryIterator:
    """Итератор по товарам в категории."""

    def __init__(self, cat: Category):
        self._category = cat
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Проверка, не вышли ли мы за пределы списка товаров
        if self._index < len(self._category._Category__products):
            prod = self._category._Category__products[self._index]
            self._index += 1
            return prod
        else:
            # Если достигли конца списка, вызываем исключение StopIteration
            raise StopIteration


# if __name__ == "__main__":
#     product1 = Product("Товар 1", "Описание товара 1", 100.0, 5)
#     product2 = Product("Товар 2", "Описание товара 2", 150.0, 10)
#     category = Category("Категория 1", "Описание категории 1", [product1, product2])
#
#     iterator = CategoryIterator(category)
#
#     for product in iterator:
#         print(product)
