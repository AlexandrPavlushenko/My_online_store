import unittest

from src.my_classes import Category, Product


class TestProduct(unittest.TestCase):
    def setUp(self) -> None:
        """Создаем продукт для тестирования"""
        self.product = Product("Товар1", "Описание товара 1", 100.0, 10)

    def test_initialization(self) -> None:
        """Проверка инициализации объекта Product"""
        self.assertEqual(self.product.name, "Товар1")
        self.assertEqual(self.product.description, "Описание товара 1")
        self.assertEqual(self.product.price, 100.0)
        self.assertEqual(self.product.quantity, 10)

    def test_price(self) -> None:
        """Проверка установки и правильности цены"""
        self.product.price = 150.0
        self.assertEqual(self.product.price, 150.0)

    def test_quantity(self) -> None:
        """Проверка установки и правильности количества"""
        self.product.quantity = 20
        self.assertEqual(self.product.quantity, 20)


class TestCategory(unittest.TestCase):
    def setUp(self) -> None:
        """Настройка тестовых данных."""
        self.category1 = Category("Electronics", "Devices and gadgets.", ["Phone", "Tablet"])
        self.category2 = Category("Clothing", "Apparel and accessories.", ["T-Shirt", "Jeans", "Jacket"])

    def test_category_creation(self) -> None:
        """Тест на создание категории."""
        self.assertEqual(self.category1.name, "Electronics")
        self.assertEqual(self.category1.description, "Devices and gadgets.")
        self.assertEqual(self.category1.products, ["Phone", "Tablet"])

    def test_category_count(self) -> None:
        """Тест на подсчет категорий."""
        self.assertEqual(Category.category_count, 2)

    def test_product_count(self) -> None:
        """Тест на подсчет товаров."""
        self.assertEqual(Category.product_count, 15)
