import random

from task_3 import list_of_lists_to_list_of_dicts


def generate_list_of_lists(n, m):
    return [[i * m + j + 1 for j in range(m)] for i in range(n)]

# Пример использования:
n = random.randint(1, 20)  # количество внутренних списков
m = random.randint(1, 100)  # количество элементов в каждом внутреннем списке
result = generate_list_of_lists(n, m)
print(f"Generated list of lists: {result}")


print(f"Generated list of dicts: {list_of_lists_to_list_of_dicts(result)}")