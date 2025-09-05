# Завдання 1

# class Car:
#     def __init__(self, brand:str, model:str, year: int, mileage: int=0 ):
#         self.__brand = brand
#         self.__model = model
#         self.__year = year
#         self.__mileage = mileage
#         self.color="white"
#
#     def get_brand(self):
#         return self.__brand
#
#     def set_brand(self, new_brand: str):
#         if isinstance(new_brand, str) and new_brand.strip():
#             self.__brand = new_brand
#         else:
#             print("Invalid brand")
#
# car=Car("Toyota", "Camry")
# print(car.get_brand())
#
# car.set_brand("Mercedes")
# print(car.get_brand())

# Завдання 2

# class English:
#     def greeting(self):
#         return "Hello, my friend!"
#
# class Spanish:
#     def greeting(self):
#         return "Hola, amigo!"
#
# def hello(lang1, lang2):
#     print(lang1.greeting())
#     print(lang2.greeting())
#
# english = English()
# spanish = Spanish()
# hello(spanish, english)

# Завдання 3 DONE

# Завдання 4

# class Base:
#     @classmethod
#     def method(cls):
#         print("Base")
#
# class Child(Base):
#     @classmethod
#     def method(cls):
#         print("Child")
#
# Base.method()
# Child.method()

# Завдання 5

from PIL import Image, ImageDraw

class Shape:
    def __init__(self):
        # Колір тла
        self.back_color = (155, 213, 117, 100)
        # Створюємо зображення 500 * 500
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save('picture.png', quality=95)

class Cone(Shape):
    def draw(self):
        self.draw1.polygon([(50,150), (200, 300), (350,400)], fill=self.back_color)
        print("Cone was drawn")

class Poraboloid(Shape):
    def draw(self):
        for x in range(50,500):
            y=int(0.002 * (x - 50)**2 + 150)
            self.draw1.line([(x,y),(x, 500)], fill=self.back_color)
        print("Poraboloid was drawn")

cone = Cone()
cone.draw()
cone.save()

poraboloid = Poraboloid()
poraboloid.draw()
poraboloid.save()
