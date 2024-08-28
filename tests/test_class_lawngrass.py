import unittest
from src.class_lawngrass import LawnGrass
from unittest.mock import patch


class TestLawnGrass(unittest.TestCase):

    @patch('src.my_classes.Product')
    def test_lawn_grass_initialization(self, MockProduct):
        # Настройка имитации поведения базового класса Product
        MockProduct.return_value = None

        # Создание экземпляра LawnGrass
        lawn_grass = LawnGrass(
            name="Смешанная трава",
            description="Лучший выбор для вашего газона",
            price=150.0,
            quantity=100,
            country="Россия",
            germination_period="7-14 дней",
            color="Зеленый"
        )

        # Проверка инициализации свойств
        self.assertEqual(lawn_grass.name, "Смешанная трава")
        self.assertEqual(lawn_grass.description, "Лучший выбор для вашего газона")
        self.assertEqual(lawn_grass.price, 150.0)
        self.assertEqual(lawn_grass.quantity, 100)
        self.assertEqual(lawn_grass.country, "Россия")
        self.assertEqual(lawn_grass.germination_period, "7-14 дней")
        self.assertEqual(lawn_grass.color, "Зеленый")
