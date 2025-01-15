students_performance = {
    "group_number": "12345",
    "students": [
        {
            "full_name": "Бойко Ольга Василівна",
            "course": 2,
            "subjects": {
                "Математика": [5, 4, 5],
                "Інформатика": [3, 4, 4],
                "Фізика": [4, 5, 5]
            },
            "average_grade": 4.5
        },
        {
            "full_name": "Парфененко Юлія Вікторівна",
            "course": 1,
            "subjects": {
                "Математика": [3, 4, 5],
                "Історія": [5, 5, 5],
                "Хімія": [4, 4, 4]
            },
            "average_grade": 4.3
        }
    ]
}
print("Список студентів:")
for student in students_performance['students']:
    print(f"Прізвище та ім'я: {student['full_name']}")
    print(f"Курс: {student['course']}")
    print("Оцінки за предметами:")
    for subject, grades in student['subjects'].items():
        print(f"  {subject}: {grades}")
    print(f"Середній бал: {student['average_grade']}\n")
