# Task1
#
# class  Editor:
#     def __init__(self, master):
#         self.master = master
#
#     def view_document(self):
#         print("You look thru current document")
#
#     def edit_document(self):
#         print("Eou cant edit document in Free plan")
#
# class ProEditor(Editor):
#     def edit_document(self):
#         print("You editing current document")
#
# LICENS_KEY="12345"
#
# key=print("Enter your key")
#
# if key==LICENS_KEY:
#     editor=ProEditor()
#     print("License activated")
# else:
#     editor=Editor()
#     print("License not activated, you are in free version")
#
# editor.view_document()
# editor.edit_document()

# Task2
#
# class GraphicObj:
#     def __init__(self):
#         print("Initializing GraphicObj")
#
#     def draw(self):
#         print("Drawing GraphicObj")
#
# class Rectangle(GraphicObj):
#     def __init__(self):
#         print("Initializing Rectangle")
#
#     def draw(self):
#         print("Drawing Rectangle")
#
# class ClickableObj(GraphicObj):
#     def __init__(self):
#         print("Initializing ClickableObj")
#
#     def click(self):
#         print("Clickable ClickableObj")
#
# class ButtonObj(Rectangle, ClickableObj):
#     def __init__(self):
#         print("Initializing ButtonObj")
#
#     def draw(self):
#         print("Drawing ButtonObj")
#
#     def click(self):
#         print("Clickable ClickableObj")
#
#
# rectangle = Rectangle()
# btn=ButtonObj()
#
# rectangle.draw()
# btn.click()
# btn.draw()

# Task3
#
# class A:
#     def __init__(self):
#         pass
#
#     def action(self):
#         print("A")
#
# class B(A):
#     def __init__(self):
#         pass
#     def action(self):
#         print("B")
#
# class C(A):
#     def __init__(self):
#         pass
#     def action(self):
#         print("C")
#
# class D(B,C):
#     def __init__(self):
#         pass
#     def action(self):
#         print("D")
#
# d = D()
# d.action()
#
#
# print(D.mro())


# Task5-6

# from datetime import date
#
#
# class MyClass1:
#     all_people=[]
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#         MyClass1.all_people.append(self)
#
#     @classmethod
#     def fromBirthYear(cls, surname, name, birthYear):
#         return cls(surname, name, date.today().year - birthYear)
#
#     def print_info(self):
#         print(self.surname + " " + self.name + "'s age is: " + str(self.age))
#
#     @staticmethod
#     def is_adult_ua(age):
#         return age >= 18
#
#
#     @staticmethod
#     def is_adult_usa(age):
#         return age >= 21
#
#     @classmethod
#     def count_adults_ua(cls):
#         return sum(1 for person in cls.all_people if cls.is_adult_ua(person.age))
#
#     @classmethod
#     def count_adults_usa(cls):
#         return sum(1 for person in cls.all_people if cls.is_adult_usa(person.age))
#
#
#
# class MyClass2(MyClass1):
#     color = 'White'
#
#
# m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
# m_per1.print_info()
# print("Adult in UA:", MyClass1.is_adult_ua(m_per1.age))
# print("Adult in USA:", MyClass1.is_adult_usa(m_per1.age))
#
# for p in MyClass1.all_people:
#     p.print_info()
#
# print("Повнолітні в Україні:", MyClass1.count_adults_ua())
# print("Повнолітні в США:", MyClass1.count_adults_usa())
#
# m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan',  2000)
# m_per2.print_info()
#
# m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
# print(isinstance(m_per3, MyClass2))
#
# m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
# print(isinstance(m_per4, MyClass1))
#
# print(issubclass(MyClass1, MyClass2))
# print(issubclass(MyClass2, MyClass1))

# Task7
#
# class Vehicle:
#     def __init__(self, make, model, year, max_speed):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#
#     def __str__(self):
#         return f'{self.make} {self.model} {self.year} {self.max_speed} km/h'
#
#     def __repr__(self):
#         return f'{self.make} {self.model} {self.year} {self.max_speed} km/h'
#
#     def info(self):
#         return f'{self.make} {self.model} {self.year} {self.max_speed} km/h'
#
# class Car(Vehicle):
#     def __init__(self, make, model, year, max_speed, door_count, fuel):
#         super().__init__(make, model, year, max_speed)
#         self.door_count = door_count
#         self.fuel = fuel
#
#     def info(self):
#         return f"{super().info}, number of door count: {self.door_count}, fuel: {self.fuel}"
#
# class Bycicle(Vehicle):
#     def __init__(self, make, model, year, max_speed, type_byke):
#         super().__init__(make, model,year, max_speed )
#         self.type_byke = type_byke
#
#     def info(self):
#         return f"{super().info}, type_byke: {self.type_byke}"
#
# car1 = Car("Toyota", "Camry", 2020, 220, 4, "Gasoline")
# bike1 = Bycicle("Giant", "Escape 3", 2021, 30, "City")
#
# vehicles=[car1, bike1]
#
# for vehicle in vehicles:
#     print(vehicle.info())

