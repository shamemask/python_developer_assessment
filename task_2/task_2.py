# Задание 2
# в наличии список множеств. внутри множества целые числа
# посчитать
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все числа из множеств в один кортеж
# *написать решения в одну строку

import numpy as np


def compute_total_numbers_non_numpy(sets):
    all_numbers = [n for s in sets for n in s]
    return len(all_numbers)


def compute_total_numbers_numpy(sets):
    all_numbers = np.array([n for s in sets for n in s])
    return all_numbers.size


def compute_total_sum_non_numpy(sets):
    all_numbers = [n for s in sets for n in s]
    return sum(all_numbers)


def compute_total_sum_numpy(sets):
    all_numbers = np.array([n for s in sets for n in s])
    return all_numbers.sum()


def compute_average_value_non_numpy(sets):
    all_numbers = [n for s in sets for n in s]
    total_numbers = len(all_numbers)
    total_sum = sum(all_numbers)
    return total_sum / total_numbers if total_numbers else 0


def compute_average_value_numpy(sets):
    all_numbers = np.array([n for s in sets for n in s])
    return all_numbers.mean()


def compute_all_numbers_tuple_non_numpy(sets):
    all_numbers = [n for s in sets for n in s]
    return tuple(all_numbers)


def compute_all_numbers_tuple_numpy(sets):
    all_numbers = np.array([n for s in sets for n in s])
    return tuple(all_numbers)


if __name__ == '__main__':
    m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
    print("Total numbers (non-numpy): ", compute_total_numbers_non_numpy(m))
    print("Total numbers (numpy): ", compute_total_numbers_numpy(m))
    print("Total sum (non-numpy): ", compute_total_sum_non_numpy(m))
    print("Total sum (numpy): ", compute_total_sum_numpy(m))
    print("Average value (non-numpy): ", compute_average_value_non_numpy(m))
    print("Average value (numpy): ", compute_average_value_numpy(m))
    print("All numbers tuple (non-numpy): ", compute_all_numbers_tuple_non_numpy(m))
    print("All numbers tuple (numpy): ", compute_all_numbers_tuple_numpy(m))