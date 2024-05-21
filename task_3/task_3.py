# Задание 3
# имеется список списков
# a = [[1,2,3], [4,5,6]]
# сделать список словарей
# b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]
# *написать решение в одну строку


def list_of_lists_to_list_of_dicts(lists):
    result = []
    dicts = {}
    for sublist in lists:
        for i, v in enumerate(sublist):
            dicts[f"k{i + 1}"] = v
        result.append(dicts)
        dicts = {}
    return result


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6]]
    print(f"Generated list of dicts: {list_of_lists_to_list_of_dicts(a)}")
