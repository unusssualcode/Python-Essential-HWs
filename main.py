# task1
#
# import random
#
# with open("nums.txt", "w") as f:
#     for _ in range(1000):
#         num = random.randint(1, 1000)
#         f.write(f"{num}\n")
#
# print("Файл random_numbers.txt створено та заповнено 10000 випадкових чисел.")
#
# with open("nums.txt", "r") as f:
#     total_sum=sum(int(line.strip()) for line in f)
#
# print(f"Сума чисел у файлі: {total_sum}")

# task3

# import pickle
# import json
#
# products=[
#     {"id": 1, "name": "Ноутбук", "price": 25000, "in_stock": True},
#     {"id": 2, "name": "Смартфон", "price": 15000, "in_stock": True},
#     {"id": 3, "name": "Навушники", "price": 2000, "in_stock": False},
#     {"id": 4, "name": "Клавіатура", "price": 1200, "in_stock": True}
# ]
#
# with open("products.pkl", "wb") as f:
#     pickle.dump(products, f)
#
# print("Список товарів збережено у форматі pickle (products.pkl)")
#
# with open("products.json", "w", encoding="utf-8") as products_file:
#     json.dump(products, products_file, ensure_ascii=False, indent=4)
#
# print("Список товарів збережено у форматі JSON (products.json)")

# task2

import shelve

with shelve.open("short_links_db") as short_links:
    full_link = input("Enter the link: ")
    short_link = input("Enter the short link: ")
    short_links[short_link] = full_link
    print(f"Short link '{short_link}' saved!")

    search_link = input("Enter the link: ")
    result = short_links.get(search_link)
    if result:
        print(f"Short link '{search_link}' found!")
    else:
        print(short_links.get(search_link), "404 Not found")

