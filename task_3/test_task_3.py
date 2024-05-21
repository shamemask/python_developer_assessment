import unittest

from task_3 import list_of_lists_to_list_of_dicts


class TestListOfListsToListOfDicts(unittest.TestCase):
    def test_conversion(self):
        input_list = [[1, 2, 3], [4, 5, 6]]
        expected_output = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]
        self.assertEqual(list_of_lists_to_list_of_dicts(input_list), expected_output)


if __name__ == '__main__':
    unittest.main()
