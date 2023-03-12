# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
for num, item in enumerate(items, 1):
    print(num, item["name"])
# 2. Выведите цену самого дешевого товара
min_price = float(items[0]["price"])
for item in items:
    if float(item["price"]) < min_price:
        min_price = float(item["price"])

print('Самый дешовый товар: ', min_price)
