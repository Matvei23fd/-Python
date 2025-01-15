try:
    # Створення першого файлу та запис у нього
    with open("questions.txt", "w") as file1:
        file1.write("Прізвище: Середа\n")
        file1.write("Питання з програмування мовою Python:\n")
        file1.write("1. Як створити список у Python?\n")
        file1.write("2. Як працює цикл for у Python?\n")

    # Створення другого файлу та запис у нього
    with open("answers.txt", "w") as file2:
        file2.write("Прізвище: Середа\n")
        file2.write("Відповіді:\n")
        file2.write("1. Список у Python створюється за допомогою квадратних дужок, наприклад: my_list = [1, 2, 3]\n")
        file2.write("2. Цикл for використовується для ітерації через елементи об'єкта, наприклад:\n")
        file2.write("   for item in my_list:\n")
        file2.write("       print(item)\n")

    print("Файли успішно створено та заповнено.")

except FileNotFoundError:
    print("Помилка: Файл не знайдено.")

except IOError:
    print("Помилка: Проблема з введенням/виведенням.")

except Exception as e:
    print(f"Сталася несподівана помилка: {e}")
