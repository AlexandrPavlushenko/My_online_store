import unittest
from unittest.mock import patch
from src.class_smartphone import Smartphone


class TestSmartphone(unittest.TestCase):

    @patch('src.my_classes.Product')
    def test_smartphone_initialization(self, MockProduct):
        # Настройка имитации поведения базового класса Product
        MockProduct.return_value = None

        # Создание экземпляра Smartphone
        smartphone = Smartphone(
            name="iPhone 14",
            description="Последняя версия iPhone с улучшенной камерой",
            price=1099.99,
            quantity=50,
            efficiency=99.9,
            model="iPhone 14 Pro",
            memory=128,
            color="Синий"
        )

        # Проверка инициализации свойств
        self.assertEqual(smartphone.name, "iPhone 14")
        self.assertEqual(smartphone.description, "Последняя версия iPhone с улучшенной камерой")
        self.assertEqual(smartphone.price, 1099.99)
        self.assertEqual(smartphone.quantity, 50)
        self.assertEqual(smartphone.efficiency, 99.9)
        self.assertEqual(smartphone.model, "iPhone 14 Pro")
        self.assertEqual(smartphone.memory, 128)
        self.assertEqual(smartphone.color, "Синий")
