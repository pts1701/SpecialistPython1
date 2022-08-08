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

brands = []
for item in items:
    brands_tmp = item["brand"]
    brands.append(brands_tmp)
brands_set = set(brands)
brands = list(brands_set)

print("Товары на складе представлены брэндами: ", brands)

# TODO: your code here

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here

print("На складе самый дорогой товар брэнда(ов): ")

# TODO: your code here
