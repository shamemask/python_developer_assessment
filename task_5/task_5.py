"""
Имеется текстовый файл с набором русских слов(имена существительные, им.падеж)
Одна строка файла содержит одно слово.
Написать программу которая выводит список слов, каждый элемент списка которого - это новое слово,
которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
Порядок вывода слов НЕ имеет значения
Например, текстовый файл содержит слова: ласты, стык, стыковка, баласт, кабала, карась
Пользователь вводмт первое слово: ласты
Программа выводит:
ластык
ластыковка
Пользователь вводмт первое слово: кабала
Программа выводит:
кабаласты
кабаласт
Пользователь вводмт первое слово: стыковка
Программа выводит:
стыковкабала
стыковкарась
"""
import os


def load_words(file_path):
    """Загружает слова из файла в список."""
    abs_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(abs_path, file_path)
    with open(full_path, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file]
    return words


def find_combinations(user_word, words):
    """Находит все комбинации слов, которые начинаются на заданное слово."""
    combinations = []
    for word in words:
        if user_word == word:
            continue
        for i in range(1, len(user_word)):
            if user_word.endswith(word[:i]):
                new_word = user_word + word[i:]
                if new_word != user_word:
                    combinations.append(new_word)
    return combinations


def main():
    # Загрузка слов из файла
    words = load_words('words.txt')

    # Ввод первого слова пользователем
    user_word = input("Введите первое слово: ").strip()

    # Поиск и вывод комбинаций
    combinations = find_combinations(user_word, words)

    for combination in combinations:
        print(combination)


if __name__ == "__main__":
    main()



