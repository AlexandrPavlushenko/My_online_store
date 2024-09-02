import pytest

from src.my_classes import Category, Product


@pytest.fixture
def product_data():
    """Возвращает данные для создания тестового товара."""
    return {"name": "Товар A", "description": "Описание товара A", "price": 100.0, "quantity": 10}


@pytest.fixture
def invalid_product_data():
    """Возвращает некорректные данные для тестирования."""
    return {"name": "Товар B", "description": "Описание товара B", "price": 0, "quantity": -5}


@pytest.fixture
def product(product_data):
    """Создает объект товара на основе фикстуры product_data."""
    return Product.new_product(product_data)


@pytest.fixture
def category(product):
    """Создает категорию с одним товаром."""
    return Category("Категория 1", "Описание категории 1", [product])


@pytest.fixture
def category2():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])


def test_product_creation(product_data):
    """Проверяет создание товара с корректными данными."""
    prod = Product.new_product(product_data)
    assert prod.name == "Товар A"
    assert prod.description == "Описание товара A"
    assert prod.price == 100.0
    assert prod.quantity == 10


def test_product_price_setter_invalid_zero(product):
    """Проверяет, что установка цены равной нулю не позволяет сохранить ее."""
    product.price = 0
    assert product.price != 0


def test_product_price_setter_invalid_negative(product):
    """Проверяет, что установка отрицательной цены не работает."""
    product.price = -50
    assert product.price != -50


def test_product_zero_quantity():
    """Проверяет вызов исключения ValueError при нулевом или отрицательном количестве товара"""
    with pytest.raises(ValueError):
        Product("Hyuawei", "Nova 9SE", 20000.0, 0)
        Product("Hyuawei", "Nova 9SE", 20000.0, -10)


def test_product_str(product):
    """Проверяет строковое представление товара."""
    assert str(product) == "Товар A, 100.0 руб. Остаток: 10 шт."


def test_product_addition(product):
    """Проверяет, что сложение двух товаров возвращает правильную сумму."""
    product2_data = {"name": "Товар B", "description": "Описание товара B", "price": 50.0, "quantity": 5}
    product2 = Product.new_product(product2_data)
    total_price = product + product2
    assert total_price == "1250.0 руб."


def test_category_creation(category):
    """Проверяет создание категории с товарами."""
    assert category.name == "Категория 1"
    assert category.description == "Описание категории 1"
    assert len(category._Category__products) == 1


def test_category_add_product(category):
    """Проверяет добавление товара в категорию."""
    new_product_data = {"name": "Товар C", "description": "Описание товара C", "price": 30.0, "quantity": 3}
    new_product = Product.new_product(new_product_data)
    category.add_product(new_product)
    assert len(category._Category__products) == 2
    assert Category.product_count == 3


def test_category_add_invalid_product(category):
    """Проверяет, что добавление неправильного типа вызывает ошибку."""
    with pytest.raises(TypeError):
        category.add_product("Некорректный продукт")


def test_category_str(category):
    """Проверяет строковое представление категории."""
    assert str(category) == "Категория 1, количество продуктов: 10 шт."


def test_category_product_count(category):
    """Проверяет общий счетчик товаров в категории."""
    assert Category.product_count == 6
    category.add_product(
        Product.new_product({"name": "Товар D", "description": "Описание товара D", "price": 20, "quantity": 2})
    )
    assert Category.product_count == 7


def test_product_quantity_change(product):
    """Проверяет, что изменение количества товара обновляет объект."""
    product.quantity = 15
    assert product.quantity == 15


def test_category_middle_price(category2):
    """Проверяет правильность подсчета средней цены в категории"""
    assert category2.middle_price() == 140333.33


def test_category_middle_price_empty():
    """Проверяет вывод нулевого значения средней цены, при отсутствии списка товаров в категории"""
    cat = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником",
        [],
    )
    assert cat.middle_price() == 0
