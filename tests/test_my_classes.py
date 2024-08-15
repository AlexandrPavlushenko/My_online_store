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

    def test_price_setter_zero(self) -> None:
        """Проверка установки нулевой цены"""
        self.product.price = 0
        self.assertEqual(self.product.price, 100.0)  # Цена должна остаться прежней

    def test_price_setter_negative(self) -> None:
        """Проверка установки отрицательной цены"""
        self.product.price = -50
        self.assertEqual(self.product.price, 100.0)  # Цена должна остаться прежней

    def test_new_product_class_method(self) -> None:
        """Проверка метода создания нового продукта"""
        new_product_data = {
            "name": "Товар 2",
            "description": "Описание товара 2",
            "price": 200.0,
            "quantity": 5
        }
        new_product = Product.new_product(new_product_data)
        self.assertEqual(new_product.name, "Товар 2")
        self.assertEqual(new_product.price, 200.0)


class TestCategory(unittest.TestCase):
    def setUp(self) -> None:
        """Настройка тестовых данных."""
        self.category = Category("Electronics", "Devices and gadgets", [])
        self.category1 = Category("Electronics", "Devices and gadgets.", ["Phone", "Tablet"])
        self.category2 = Category("Clothing", "Apparel and accessories.", ["T-Shirt", "Jeans", "Jacket"])

    def test_category_creation(self) -> None:
        """Тест на создание категории."""
        self.assertEqual(self.category1.name, "Electronics")
        self.assertEqual(self.category1.description, "Devices and gadgets.")
        self.assertEqual(self.category1.products, ["Phone", "Tablet"])

    def test_category_count(self) -> None:
        """Тест на подсчет категорий."""
        self.assertEqual(Category.category_count, 9)

    def test_product_count(self) -> None:
        """Тест на подсчет товаров."""
        self.assertEqual(Category.product_count, 28)

    def test_add_product(self) -> None:
        """Тест на добавление нового товара"""
        self.category.add_product("Smartphone")
        self.assertIn("Smartphone", self.category.products)
        self.assertEqual(len(self.category.products), 1)
        self.assertEqual(Category.product_count, 13)

    def test_add_multiple_products(self) -> None:
        """Тестирование добавления нескольких товаров последовательно."""
        self.category.add_product("Smartphone")
        self.category.add_product("Laptop")
        self.assertIn("Laptop", self.category.products)
        self.assertEqual(len(self.category.products), 2)
        self.assertEqual(Category.product_count, 7)
