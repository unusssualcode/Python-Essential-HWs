# task1

import re
# from collections import Counter
#
# def word_frequency(text):
#     words = re.findall(r'\w+', text.lower())
#
#     freq = Counter(words)
#     return dict(freq)
#
# text = "Привіт світ! Привіт Python. Python — це круто!"
# test = word_frequency(text)
# print(test)

# task2

# def extract_data(input_file, output_file):
#     with open(input_file, "r", encoding="utf-8") as f:
#         text=f.read()
#
#     date_pattern=r"\b\d{1,2}[./-]\d{1,2}[./-]\d{4}\b"
#
#     phone_pattern=r"(+\?38\d{9}|\(?0\d{2}\)?\s?\d{3}[-]?\d{2}[-]?\d{2}\)"
#
#     mail_pattern=r"\b[\w\.-]+@[\w\.-]+\.\w+\b"
#
#     dates=re.findall(date_pattern, text)
#     phones=re.findall(phone_pattern, text)
#     mails=re.findall(mail_pattern, text)
#
#     with open(output_file, "w", encoding="utf-8") as f:
#         f.write("Дати народження:\n")
#         f.write("\n".join(dates) + "\n\n")
#
#         f.write("Телефони:\n")
#         f.write("\n".join(phones) + "\n\n")
#
#         f.write("Електронні адреси:\n")
#         f.write("\n".join(mails)+ "\n")
#
# extract_data("input.txt", "output.txt")

# task3

# def last_three_chars(sentence):
#     words = sentence.split()
#     for word in words:
#         print(word[-3:])
#
# user_input = input("Введіть пропозицію: ")
# last_three_chars(user_input)

# task4

# def analyze_text(text):
#     text = text.lower()
#
#     words = re.findall(r'\w+', text)
#
#     unique_words = set(words)
#     print("Унікальні слова:")
#     print(unique_words)
#     print("\nЗагальна кількість слів:", len(words))
#     print("Кількість унікальних слів:", len(unique_words))
#
#
# sentense=input("Введіть текст для аналізу: ")
# analyze_text(sentense)

# task5

def student_info(text):
    surname_pattern = r"Прізвище:\s*([А-Яа-яЇїІіЄєҐґ\-]+)"
    name_pattern = r"Ім'я:\s*([А-Яа-яЇїІіЄєҐґ\-]+)"
    dob_pattern = r"Дата народження:\s*(\d{1,2}[./-]\d{1,2}[./-]\d{4})"
    email_pattern = r"Email:\s*([\w\.-]+@[\w\.-]+\.\w+)"
    feedback_pattern = r"Відгук:\s*(.+)$"

    surname = re.search(surname_pattern, text)
    name = re.search(name_pattern, text)
    dob = re.search(dob_pattern, text)
    email = re.search(email_pattern, text)
    feedback = re.search(feedback_pattern, text)

    student = {
        "Прізвище": surname.group(1) if surname else None,
        "Імя": name.group(1) if name else None,
        "Дата народження": dob.group(1) if dob else None,
        "Email": email.group(1) if email else None,
        "Відгук": feedback.group(1) if feedback else None,
    }

    return student

user_input = input("Введіть інформацію про учня: ")
info = student_info(user_input)
print(info)