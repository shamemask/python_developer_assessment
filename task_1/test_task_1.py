import unittest
import csv

from task_1 import read_csv_file, write_csv_file


class TestCSVProcessing(unittest.TestCase):

    def setUp(self):
        # Создаем временный файл с данными для тестирования
        self.test_file = 'test_f.csv'
        with open(self.test_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['lastname', 'name', 'patronymic', 'date_of_birth', 'id'],
                                    delimiter='|')
            writer.writeheader()
            writer.writerow(
                {'lastname': 'Фамилия1', 'name': 'Имя1', 'patronymic': 'Отчество1', 'date_of_birth': '21.11.1998',
                 'id': '312040348-3048'})
            writer.writerow(
                {'lastname': 'Фамилия2', 'name': 'Имя2', 'patronymic': 'Отчество2', 'date_of_birth': '11.01.1972',
                 'id': '457865234-3431'})
            writer.writerow(
                {'lastname': 'Фамилия1', 'name': 'Имя1', 'patronymic': 'Отчество1', 'date_of_birth': '21.11.1998',
                 'id': '312040348-3048'})

    def tearDown(self):
        # Удаляем временный файл после завершения тестов
        import os
        os.remove(self.test_file)

    def test_read_csv_file(self):
        data = read_csv_file(self.test_file)
        # Проверяем, что данные считываются правильно
        self.assertEqual(len(data), 2)
        self.assertTrue('312040348-3048' in data)
        self.assertTrue('457865234-3431' in data)
        self.assertEqual(len(data['312040348-3048']), 1)
        self.assertEqual(len(data['457865234-3431']), 1)

    def test_write_csv_file(self):
        data = {'312040348-3048': [
            {'lastname': 'Фамилия1', 'name': 'Имя1', 'patronymic': 'Отчество1', 'date_of_birth': '21.11.1998',
             'id': '312040348-3048'}],
                '457865234-3431': [
                    {'lastname': 'Фамилия2', 'name': 'Имя2', 'patronymic': 'Отчество2', 'date_of_birth': '11.01.1972',
                     'id': '457865234-3431'}]}
        output_file = 'output_test_f.csv'
        write_csv_file(data, output_file)

        # Проверяем, что файл записывается правильно
        with open(output_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter='|')
            rows = list(reader)
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]['id'], '312040348-3048')
            self.assertEqual(rows[1]['id'], '457865234-3431')

        # Удаляем временный файл после теста
        import os
        os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
