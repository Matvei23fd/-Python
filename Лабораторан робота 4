text = """Банкноти з'явилися як зручніша альтернатива металевим монетам.Їхня історія налічує кілька століть.Сучасні банкноти відрізняються складною системою захисту та різноманітністю дизайнів, що відображають культуру та історію країни."""
sentences = text.split('. ')
print("Речення у тексті:")
print(sentences)

# Підрахунок кількості слів
words = text.split()
word_count = len(words)
print(f"\nКількість слів у тексті: {word_count}")

# Знаходимо кількість унікальних слів (без урахування регістру)
unique_words = set(word.lower() for word in words)
unique_word_count = len(unique_words)
print(f"Кількість унікальних слів: {unique_word_count}")

# Заміна слова "банкноти" на "гроші"
updated_text = text.replace("банкноти", "гроші")
print(f"\nТекст із заміною слова 'банкноти':\n{updated_text}")

# Пошук найчастішого символу у тексті
from collections import Counter
char_count = Counter(text)
most_common_char = char_count.most_common(1)[0]
print(f"\nНайчастіший символ у тексті: '{most_common_char[0]}' з кількістю повторень: {most_common_char[1]}")

# Переведення всього тексту в нижній регістр
lower_text = text.lower()
print("Текст у нижньому регістрі:")
print(lower_text)
