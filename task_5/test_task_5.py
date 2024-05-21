import unittest

from task_5 import find_combinations, load_words


class TestWordCombinations(unittest.TestCase):

    def setUp(self):
        self.words = load_words('100_words.txt')

    def test_tank_combinations(self):
        user_word = "танк"
        expected_combinations = [
            "танкабан",
            "танкактус",
            "танкарандаш",
            "танкнига",
            "танкот",
            "танкраб"
        ]
        result = find_combinations(user_word, self.words)
        self.assertCountEqual(result, expected_combinations)

    def test_gruzovik_combinations(self):
        user_word = "грузовик"
        expected_combinations = [
            "грузовикабан",
            "грузовикактус",
            "грузовикарандаш",
            "грузовикнига",
            "грузовикот",
            "грузовикраб"
        ]
        result = find_combinations(user_word, self.words)
        self.assertCountEqual(result, expected_combinations)

    def test_yabloko_combinations(self):
        user_word = "яблоко"
        expected_combinations = [
            "яблокогонь",
            "яблокот",
            "яблокобувь",
            "яблококо",
            "яблокоса"
        ]
        result = find_combinations(user_word, self.words)
        self.assertCountEqual(result, expected_combinations)

if __name__ == '__main__':
    unittest.main()
