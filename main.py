# Завдання 1
#
# Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.


# class Book:
#     def __init__(self, title, author, year, genre):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.genre= genre
#
#     def __repr__(self):
#         return f"Book(title='{self.title}', author='{self.author}', year={self.year},genre='{self.genre}')"
#
#     def __str__(self):
#         return f"«{self.title}» ({self.year}), {self.genre}. Автор: {self.author}"
#
# book1 = Book("Джордж Орвелл", "1984", 1949, "антиутопія")
# book2 = Book("Дж. К. Ролінґ", "Гаррі Поттер і філософський камінь", 1997, "фентезі")
# book3 = Book("Ф. М. Достоєвський", "Злочин і кара", 1866, "роман")
#
# print(book1)
# print([book1, book2, book3])


# Завдання 2
#
# Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.

# class Review:
#     def __init__(self, review, text):
#         self.review = review
#         self.text = text
#
#     def __str__(self):
#         return f"{self.review}, {self.text}"
#
# class Book:
#     def __init__(self, title, author, year, genre):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.genre= genre
#         self.reviews = []
#
#     def add_review(self, review):
#         self.reviews.append(review)
#
#     def __str__(self):
#         reviews_texts = "\n".join([f" - {str(r)}" for r in self.reviews]) if self.reviews else "No reviews"
#         return f"{self.title} ({self.author}) by {self.year}: {reviews_texts}"
#
# book1 = Book("<NAME>", "<NAME>", "2005", "Fantasy")
#
# book1.add_review(Review("<NAME>", "<NAME>"))
# print(book1)


# Завдання 4
#
# Створіть клас, який описує автомобіль.
# Створіть клас автосалону, що містить в собі список автомобілів, доступних для продажу,
# і функцію продажу заданого автомобіля.

# class Car:
#     def __init__(self, brand, model, year, price):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.price = price
#
#     def __str__(self):
#         return f"{self.brand} {self.model} ({self.year}) - ${self.price}"
#
# class CarsDealership:
#     def __init__(self, name):
#         self.name = name
#         self.cars = []
#
#     def add_car(self, car):
#         self.cars.append(car)
#
#     def show_cars(self):
#         if self.cars:
#             print(self.name)
#             for car in self.cars:
#                 print(f" -{car}")
#         else:
#             print("No cars available")
#
#
#     def sell_cars(self,car):
#             if car in self.cars:
#                 self.cars.remove(car)
#                 print(f"{car.name} sold out")
#             else:
#                 print(f"{car.name} not found")