import csv
from faker import Faker
import random
from datetime import datetime

# Создаем экземпляр Faker для генерации случайных данных
fake = Faker()
dublicates_chance = 0.3  # Коэффициент для уменьшения вероятности дубликатов при генерации
id_or_data = 0.5  # Коэффициент вероятности копии id или целых данных


# Функция для генерации случайной даты рождения
def generate_birthdate():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2005, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date).strftime('%d.%m.%Y')


# Генерация отдельной записи
def generate_record(ids, data):
    # Проверяем, если иногда должны быть только дубликаты id
    if random.random() < dublicates_chance and ids:
        if random.random() < id_or_data:
            # генерация дубликата id
            id = random.choice(list(ids))
            lastname = fake.last_name()
            name = fake.first_name()
            patronymic = fake.first_name()
            birthdate = generate_birthdate()
        else:
            # генерация дубликата данных
            copy_data = random.choice(data)
            lastname = copy_data[0]
            name = copy_data[1]
            patronymic = copy_data[2]
            birthdate = copy_data[3]
            id = copy_data[4]
    else:
        lastname = fake.last_name()
        name = fake.first_name()
        patronymic = fake.first_name()
        birthdate = generate_birthdate()
        id = fake.uuid4()
    return lastname, name, patronymic, birthdate, id


# Генератор данных
def generate_data(num_records):
    data = []
    ids = set()
    for _ in range(num_records):
        record = generate_record(ids, data)
        data.append(record)
        ids.add(record[-1])  # Добавляем id в множество ids
    return data


# Функция для записи данных в csv-файл
def write_to_csv(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(['lastname', 'name', 'patronymic', 'date_of_birth', 'id'])
        writer.writerows(data)


if __name__ == '__main__':
    # Генерируем данные
    data = generate_data(1000)  # Генерируем установленное количество записей
    write_to_csv('f.csv', data)  # Записываем данные в файл csv


# unittest

