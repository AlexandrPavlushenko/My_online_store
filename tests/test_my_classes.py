from src.my_classes import Category, Product


def test_product_creation():
    # Фикстура для теста
    product_data = {
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": 100.0,
        "quantity": 20
    }

    product = Product.new_product(product_data)

    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 100.0
    assert product.quantity == 20


def test_product_str_method():
    product = Product("Товар 2", "Описание товара 2", 150.0, 5)
    assert str(product) == "Товар 2, 150.0 руб. Остаток: 5 шт."


def test_price_setter():
    product = Product("Товар 3", "Описание товара 3", 200.0, 10)
    product.price = 250.0
    assert product.price == 250.0

    product.price = -50.0  # Попробуем установить отрицательную цену
    assert product.price != -50.0  # Цена не должна измениться


def test_category_creation():
    product1 = Product("Товар 1", "Описание товара 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание товара 2", 150.0, 10)
    category = Category("Категория 1", "Описание категории 1", [product1, product2])

    assert category.name == "Категория 1"
    assert category.description == "Описание категории 1"
    assert len(category.products.split('\n')) - 1 == 2  # количество продуктов


def test_category_add_product():
    product = Product("Товар 3", "Описание товара 3", 200.0, 2)
    category = Category("Категория 2", "Описание категории 2", [])

    category.add_product(product)

    assert len(category.products.split('\n')) - 1 == 1  # теперь должно быть 1 товар в категории


def test_category_total_products_count():
    product1 = Product("Товар 1", "Описание товара 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание товара 2", 150.0, 10)
    category = Category("Категория 3", "Описание категории 3", [product1, product2])

    assert str(category) == "Категория 3, количество продуктов: 15 шт."
