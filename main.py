# task2

# class Contact:
#     def __init__(self, surname, name, age, mob_phone, email):
#         self.surname = surname
#         self.name = name
#         self.age = age
#         self.mob_phone = mob_phone
#         self.email = email
#
#     def get_contact(self):
#         return f"{self.surname} {self.name}, {self.age} років, тел: {self.mob_phone}, email: {self.email}"
#
#     def sent_messgae(self, message):
#         return f"Повідомлення '{message}' відправлено на {self.email}"
#
# class UpdateContact(Contact):
#     def __init__(self, surname, name, age, mob_phone, email, job):
#         super().__init__(surname, name, age, mob_phone, email)
#         self.job = job
#
#     def get_message(self):
#         return f"Контакт: {self.surname} {self.name}, професія: {self.job}"
#
# person1=Contact("ghghgh","ghfgfkdjh", 34, 3805000000, "email@email.com")
# person2=UpdateContact("jsjsksj","jidjjsfnkjs", 32, 380508377362, "email2@email.com", "traktorist")
#
# print(person1.get_contact())
# print(person1.sent_messgae("hello"))
#
# print(person2.get_contact())
# print(person2.sent_messgae("hello2"))
# print(person2.get_message())

# task3

# class Contact:
#     def __init__(self, surname, name, age, mob_phone, email):
#         self.surname = surname
#         self.name = name
#         self.age = age
#         self.mob_phone = mob_phone
#         self.email = email
#
#     def get_contact(self):
#         return f"{self.surname} {self.name}, {self.age} років, тел: {self.mob_phone}, email: {self.email}"
#
#     def sent_messgae(self, message):
#         return f"Повідомлення '{message}' відправлено на {self.email}"
#
# class UpdateContact(Contact):
#     def __init__(self, surname, name, age, mob_phone, email, job):
#         super().__init__(surname, name, age, mob_phone, email)
#         self.job = job
#
#     def get_message(self):
#         return f"Контакт: {self.surname} {self.name}, професія: {self.job}"
#
# person1=Contact("ghghgh","ghfgfkdjh", 34, 3805000000, "email@email.com")
# person2=UpdateContact("jsjsksj","jidjjsfnkjs", 32, 380508377362, "email2@email.com", "traktorist")
#
# print(person1.get_contact())
# print(person1.sent_messgae("hello"))
#
# print(person2.get_contact())
# print(person2.sent_messgae("hello2"))
# print(person2.get_message())
#
# print("\n=== Використання hasattr(), getattr(), setattr(), delattr() ===")
# print(hasattr(person1, "surname"))
# print(getattr(person1, "surname"))
# setattr(person1, "surname", "fhjdksiusysh")
# delattr(person1, "surname")


# task4

# class Contact:
#     def __init__(self, surname, name, age, mob_phone, email):
#         self.surname = surname
#         self.name = name
#         self.age = age
#         self.mob_phone = mob_phone
#         self.email = email
#
#     def get_contact(self):
#         return f"{self.surname} {self.name}, {self.age} років, тел: {self.mob_phone}, email: {self.email}"
#
#     def sent_messgae(self, message):
#         return f"Повідомлення '{message}' відправлено на {self.email}"
#
# class UpdateContact(Contact):
#     def __init__(self, surname, name, age, mob_phone, email, job):
#         super().__init__(surname, name, age, mob_phone, email)
#         self.job = job
#
#     def get_message(self):
#         return f"Контакт: {self.surname} {self.name}, професія: {self.job}"
#
# person1=Contact("ghghgh","ghfgfkdjh", 34, 3805000000, "email@email.com")
# person2=Contact("Petrov", "Petro", 25, 380507778899, "petro@email.com")
#
# person3=UpdateContact("jsjsksj","jidjjsfnkjs", 32, 380508377362, "email2@email.com", "traktorist")
# person4 = UpdateContact("Koval", "Olena", 35, 380671112244, "olena@email.com", "вчитель")

# print(isinstance(person1, Contact))
# print(isinstance(person1, UpdateContact))
#
#
# print(issubclass(UpdateContact, Contact))
# print(issubclass(Contact, object))
# print(person1.get_contact())
# print(person1.sent_messgae("hello"))
#
# print(person2.get_contact())
# print(person2.sent_messgae("hello2"))
# print(person2.get_message())
#
# print("\n=== Використання hasattr(), getattr(), setattr(), delattr() ===")
# print(hasattr(person1, "surname"))
# print(getattr(person1, "surname"))
# setattr(person1, "surname", "fhjdksiusysh")
# delattr(person1, "surname")

# task5

# class Contact:
#     def __init__(self, surname, name, age, mob_phone, email):
#         self.surname = surname
#         self.name = name
#         self.age = age
#         self.mob_phone = mob_phone
#         self.email = email
#
#     def get_contact(self):
#         return f"{self.surname} {self.name}, {self.age} років, тел: {self.mob_phone}, email: {self.email}"
#
#     def sent_messgae(self, message):
#         return f"Повідомлення '{message}' відправлено на {self.email}"
#
# class UpdateContact(Contact):
#     def __init__(self, surname, name, age, mob_phone, email, job):
#         super().__init__(surname, name, age, mob_phone, email)
#         self.job = job
#
#     def get_message(self):
#         return f"Контакт: {self.surname} {self.name}, професія: {self.job}"
#
# person1=Contact("ghghgh","ghfgfkdjh", 34, 3805000000, "email@email.com")
# person2=Contact("Petrov", "Petro", 25, 380507778899, "petro@email.com")
#
# person3=UpdateContact("jsjsksj","jidjjsfnkjs", 32, 380508377362, "email2@email.com", "traktorist")
# person4 = UpdateContact("Koval", "Olena", 35, 380671112244, "olena@email.com", "вчитель")
#
# print(Contact.__dict__)
# print(UpdateContact.__dict__)
# print(person1.__dict__)
# print(person2.__dict__)
# print(person3.__dict__)
# print(person4.__dict__)
#
# delattr(person3, "job")
# delattr(person4, "job")
#
# print(Contact.__dict__)
# print(UpdateContact.__dict__)
# print(person1.__dict__)
# print(person2.__dict__)
# print(person3.__dict__)
# print(person4.__dict__)

# task6

# import inspect
#
# class Contact:
#     def __init__(self, surname, name, age, mob_phone, email):
#         self.surname = surname
#         self.name = name
#         self.age = age
#         self.mob_phone = mob_phone
#         self.email = email
#
#     def get_contact(self):
#         return f"{self.surname} {self.name}, {self.age} років, тел: {self.mob_phone}, email: {self.email}"
#
#     def sent_messgae(self, message):
#         return f"Повідомлення '{message}' відправлено на {self.email}"
#
#
# class UpdateContact(Contact):
#     def __init__(self, surname, name, age, mob_phone, email, job):
#         super().__init__(surname, name, age, mob_phone, email)
#         self.job = job
#
#     def get_message(self):
#         return f"Контакт: {self.surname} {self.name}, професія: {self.job}"
#
#
# for name, function in inspect.getmembers(Contact, inspect.isfunction):
#     print(f"{name}: {function.get_contact()}")
#
# for name, function in inspect.getmembers(UpdateContact, inspect.isfunction):
#     print(f"{name}: {function.get_contact()}")