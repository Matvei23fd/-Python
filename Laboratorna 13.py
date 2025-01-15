import csv
import json
import os

# Шлях до файлів
csv_file = "data.csv"
json_file = "data.json"
new_csv_file = "new_data.csv"

# 1. Створення .csv файлу
def create_csv_file(file_path):
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Ім'я", "Вік", "Професія"])
            writer.writeheader()  # Запис заголовків
            # Додавання рядків
            writer.writerows([
                {"ID": 1, "Ім'я": "Іван", "Вік": 25, "Професія": "Програміст"},
                {"ID": 2, "Ім'я": "Марія", "Вік": 30, "Професія": "Дизайнер"},
                {"ID": 3, "Ім'я": "Петро", "Вік": 22, "Професія": "Дата Аналітик"}
            ])
        print(f"Файл {file_path} успішно створено.")
    except Exception as e:
        print(f"Помилка створення файлу {file_path}: {e}")

# 2. Конвертація .csv у .json
def csv_to_json(csv_path, json_path):
    try:
        with open(csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]  # Зчитування рядків у список
        with open(json_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        print(f"Дані з {csv_path} успішно записано у {json_path}.")
    except FileNotFoundError:
        print(f"Файл {csv_path} не знайдено.")
    except Exception as e:
        print(f"Помилка при роботі з файлами: {e}")

# 3. Конвертація .json у новий .csv із додаванням рядків
def json_to_csv_with_additional_data(json_path, new_csv_path):
    try:
        with open(json_path, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)  # Зчитування JSON
        # Додавання нових рядків
        data.append({"ID": 4, "Ім'я": "Oлена", "Вік": 28, "Професія": "Вчитель"})
        data.append({"ID": 5, "Ім'я": "Андрій", "Вік": 35, "Професія": "Інженер"})
        with open(new_csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["ID", "Ім'я", "Вік", "Професія"])
            writer.writeheader()
            writer.writerows(data)
        print(f"Дані з {json_path} успішно записано у {new_csv_path} з новими рядками.")
    except FileNotFoundError:
        print(f"Файл {json_path} не знайдено.")
    except Exception as e:
        print(f"Помилка при роботі з файлами: {e}")

# Головний блок програми
if __name__ == "__main__":
    create_csv_file(csv_file)  # Створення CSV
    csv_to_json(csv_file, json_file)  # Конвертація у JSON
    json_to_csv_with_additional_data(json_file, new_csv_file)  # Зворотна конвертація у CSV
