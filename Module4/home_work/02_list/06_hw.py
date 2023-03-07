# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

all_brends = []
for brands in items:
    all_brends.append(brands["brand"])
list_brends = []
unique_brends = set(all_brends)
for number in unique_brends:
    list_brends.append(number)
print(list_brends)

print("На складе больше всего товаров брэнда(ов): ")

count_adidas = all_brends.count('adidas')
count_reebok = all_brends.count('reebok')
count_puma = all_brends.count('puma')
if count_adidas > count_reebok and count_adidas > count_puma:
     print(f'Больше товаров бренда Adidas, {count_adidas} шт.')
elif count_puma > count_reebok and count_adidas < count_puma:
     print(f'Больше товаров бренда Puma, {count_puma} шт.')
elif count_puma < count_reebok and count_adidas < count_reebok:
    print(f'Больше товаров бренда Reebok, {count_reebok} шт.')
elif count_puma == count_reebok and count_adidas == count_puma:
     print(f"Товаров всех брендов равное количество, {count_adidas} шт.")
elif count_puma == count_reebok and count_adidas < count_reebok:
     print(f'Больше товаров бренда Puma и Reebok, по {count_puma} шт.')
elif count_adidas == count_reebok and count_adidas > count_puma:
     print(f'Больше товаров бренда Adidas и Reebok, по {count_adidas} шт.')
elif count_adidas == count_puma and count_adidas > count_reebok:
     print(f'Больше товаров бренда Adidas и Puma, по {count_adidas} шт.')

print("На складе самый дорогой товар брэнда(ов): ")

list_price = []
for i in items:
    list_price.append(i['price'])
max_price = max(list_price)
for i in items:
    if max_price in i.values():
        name = i['name']
        price = i['price']
        brand = i['brand']
        print(f'Самый дорогой шмот {name}, его цена {price} УбиенныхЕнотов, а штопает {brand}')
# ВОПРОС: Почему не работает вывод вида - print(f'Самый дорогой шмот {i['name']}, его цена {i['price']} УбиенныхЕнотов, а штопает {i['brand']}')
