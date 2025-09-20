from core import LinkShortener

def main():
    service = LinkShortener()

    while True:
        print("\nМеню:")
        print("1 - Додати нове посилання")
        print("2 - Знайти посилання")
        print("3 - Вийти")

        choice = input("Ваш вибір: ")
        if choice == "1":
            full_link=input("Введіть повне посилання: ")
            short_link=input("Введіть коротке посилання: ")
            service.save_link(short_link, full_link)
            print(f"Скорочене посилання '{short_link}' збережено!")

        elif choice == "2":
            search_link = input("Введіть коротке ім’я: ")
            result=service.get_link(search_link)
            if result:
                print(f"Повне посилання: {result}")
            else:
                print("404 Not Found")

        elif choice=="3":
            print("Вихід із програми...")
            break

        else:
            print("Невірний вибір!")

