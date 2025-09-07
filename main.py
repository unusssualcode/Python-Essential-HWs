# Task2

# class Calculator:
#     def add(self, a, b):
#         return a + b
#
#     def subtract(self, a, b):
#         return a - b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def divide(self, a, b):
#         if b == 0:
#             raise ZeroDivisionError("Ділення на нуль неможливе")
#         return a / b
#
#     def power(self, a, b):
#         if a == 0 and b < 0:
#             raise ValueError("0 не можна підносити до від’ємного степеня")
#
#         return a ** b
#
#
# class CalculatorApp:
#     def __init__(self):
#         self.calculator = Calculator()
#
#     def run(self):
#         print("Простий калькулятор (класи)")
#         print("Операції: +, -, *, /, **")
#         print("Введіть 'exit' для виходу")
#
#         while True:
#             try:
#                 operation = input("\nВведіть вираз (наприклад: 2 + 3): ")
#
#                 if operation == "exit":
#                     print("Роботу завершено.")
#                     break
#
#                 parts=operation.split()
#                 if len(parts) != 3:
#                     print(" Помилка: введіть у форматі 'число оператор число'")
#                     continue
#
#                 a_str, operator, b_str = parts
#
#                 try:
#                     a = int(a_str)
#                     b = int(b_str)
#                 except ValueError:
#                     print("Помилка: аргументи повинні бути числами")
#                     continue
#
#                 if operator == "+":
#                     result = self.calculator.add(a, b)
#                 elif operator == "-":
#                     result = self.calculator.subtract(a, b)
#                 elif operator == "*":
#                     result = self.calculator.multiply(a, b)
#                 elif operator == "/":
#                     try:
#                         result = self.calculator.divide(a, b)
#                     except ZeroDivisionError as e:
#                         print(e)
#                         continue
#
#                 elif operator == "^":
#                     try:
#                         result = self.calculator.power(a, b)
#                     except ValueError as e:
#                         print(e)
#                         continue
#
#                 else:
#                     print("Помилка: невідомий оператор")
#                     continue
#
#                 print(f" Результат: {result}")
#
#             except Exception as e:
#                 print(f" Непередбачена помилка: {e}")
#
# if __name__ == "__main__":
#     app = CalculatorApp()
#     app.run()


# Task3

class Employee:
    def __init__(self, name:str, surname:str, department:str, start_date:int):
        if not name or not surname or not department :
            raise ValueError("Name and Surname cannot be empty")

        if not isinstance(start_date, int) or start_date < 1900 or start_date > 2100 :
            raise ValueError("Start date must be between 1900 and 2100")

        self.name = name
        self.surname = surname
        self.department = department
        self.start_date = start_date

    def __str__(self):
        return f"{self.name} {self.surname}, department: {self.department}, {self.start_date}"

def main():
    employees=[]

    number_of_employees=int(input("How many employees? "))
    for i in range(number_of_employees):
        print(f"\nEnter employee info {i+1}:")
        try:
            name = input("Enter employee name: ").strip()
            surname = input("Enter employee surname: ").strip()
            department = input("Enter employee department: ").strip()
            start_date = int(input("Enter employee start date: ").strip())
            employee=Employee(name, surname, department, start_date)
            employees.append(employee)
        except Exception as e:
            print(e)

    try:
        year = int(input("Enter year to filter employees: "))
    except ValueError:
        print("Year must be an integer")
        return

    print(f"\nСпівробітники, прийняті після {year}:")

    find=False
    for emp in employees:
        if emp.start_date > year:
            print(emp)
            find = True

    if not find:
        print("There is no employee with that year")

if __name__ == "__main__":
    main()

