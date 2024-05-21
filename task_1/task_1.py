import csv

# Задание 1
# имеется текстовый файл f.csv, по формату похожий на .csv с разделителем |
"""
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
...
"""
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одинаковым id присутствуют разные данные - собрать такие записи


def read_csv_file(file_path):
    data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='|')
        for row in reader:
            id = row['id'].strip()
            if id in data:
                # Если id уже есть в данных, проверяем, совпадают ли все поля, если нет, добавляем запись в список значений
                if row not in data[id]:
                    data[id].append(row)
            else:
                data[id] = [row]
    return data


def write_csv_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['lastname', 'name', 'patronymic', 'date_of_birth', 'id'], delimiter='|')
        writer.writeheader()
        for id, rows in data.items():
            for row in rows:
                writer.writerow(row)

def main():
    input_file = 'f.csv'
    output_file = 'unique_f.csv'

    # Читаем данные из файла
    data = read_csv_file(input_file)

    # Записываем уникальные записи в новый файл
    write_csv_file(data, output_file)

    print(f"Уникальные записи сохранены в файл {output_file}:")

if __name__ == "__main__":
    main()
