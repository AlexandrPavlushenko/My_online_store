import unittest

from src.my_classes import Category, Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Создание объекта Product перед каждым тестом"""
        self.product = Product(name="Товар 1",
                               description="Описание товара 1",
                               price=100.0,
                               quantity=10)

    def test_initialization(self):
        """Тестирование инициализации объекта Product"""
        self.assertEqual(self.product.name, "Товар 1")
        self.assertEqual(self.product.description, "Описание товара 1")
        self.assertEqual(self.product.price, 100.0)
        self.assertEqual(self.product.quantity, 10)

    def test_price_setter_valid(self):
        """Тестирование установки корректной цены"""
        self.product.price = 150.0
        self.assertEqual(self.product.price, 150.0)

    def test_new_product_creation(self):
        """Тестирование метода new_product"""
        new_product_data = {
            "name": "Товар 2",
            "description": "Описание товара 2",
            "price": 200.0,
            "quantity": 5
        }
        new_product = Product.new_product(new_product_data)
        self.assertEqual(new_product.name, "Товар 2")
        self.assertEqual(new_product.description, "Описание товара 2")
        self.assertEqual(new_product.price, 200.0)
        self.assertEqual(new_product.quantity, 5)


class Product_test:  # Создадим простую модель класса "Товары" для теста
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity


class TestCategory(unittest.TestCase):

    def setUp(self):
        self.product1 = Product_test("Товар 1", 100.0, 10)
        self.product2 = Product_test("Товар 2", 150.0, 5)
        self.category = Category("Категория 1", "Описание категории 1", [self.product1, self.product2])

    def test_initialization(self):
        self.assertEqual(self.category.name, "Категория 1")
        self.assertEqual(self.category.description, "Описание категории 1")
        self.assertEqual(len(self.category.products.splitlines()), 2)

    def test_add_product(self):
        new_product = Product_test("Товар 3", 200.0, 2)
        self.category.add_product(new_product)
        self.assertEqual(len(self.category.products.splitlines()), 3)
        self.assertIn("Товар 3", self.category.products)

    def test_product_count(self):
        self.assertEqual(Category.product_count, 7)
