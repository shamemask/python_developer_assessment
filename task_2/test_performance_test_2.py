import unittest
import random
import time

from task_2 import compute_total_numbers_non_numpy, compute_total_numbers_numpy, compute_total_sum_non_numpy, \
    compute_total_sum_numpy, compute_average_value_non_numpy, compute_average_value_numpy, \
    compute_all_numbers_tuple_non_numpy, compute_all_numbers_tuple_numpy


class TestLoad(unittest.TestCase):
    def generate_random_sets(self, size):
        return [{random.randint(0, size) for _ in range(random.randint(1, size // 10))} for _ in range(size)]

    def timed_execution(self, func):
        start_time = time.time()
        func()
        end_time = time.time()
        return end_time - start_time


    def test_total_numbers_non_numpy(self):
        light_random_sets = self.generate_random_sets(1000)
        execution_time = self.timed_execution(lambda: compute_total_numbers_non_numpy(light_random_sets))
        print(f"\nTotal numbers (non-numpy): Execution time: {execution_time:.5f} seconds")

    def test_total_numbers_numpy(self):
        light_random_sets = self.generate_random_sets(1000)
        execution_time = self.timed_execution(lambda: compute_total_numbers_numpy(light_random_sets))
        print(f"\nTotal numbers (numpy): Execution time: {execution_time:.5f} seconds")

    def test_total_sum_non_numpy(self):
        light_random_sets = self.generate_random_sets(1000)
        execution_time = self.timed_execution(lambda: compute_total_sum_non_numpy(light_random_sets))
        print(f"\nTotal sum (non-numpy): Execution time: {execution_time:.5f} seconds")

    def test_total_sum_numpy(self):
        light_random_sets = self.generate_random_sets(1000)
        execution_time = self.timed_execution(lambda: compute_total_sum_numpy(light_random_sets))
        print(f"\nTotal sum (numpy): Execution time: {execution_time:.5f} seconds")

    def test_average_value_non_numpy(self):
        light_random_sets = self.generate_random_sets(1000)
        execution_time = self.timed_execution(lambda: compute_average_value_non_numpy(light_random_sets))
        print(f"\nAverage value (non-numpy): Execution time: {execution_time:.5f} seconds")

    def test_average_value_numpy(self):
        light_random_sets = self.generate_random_sets(1000)
        execution_time = self.timed_execution(lambda: compute_average_value_numpy(light_random_sets))
        print(f"\nAverage value (numpy): Execution time: {execution_time:.5f} seconds")

    def test_all_numbers_tuple_non_numpy(self):
        light_random_sets = self.generate_random_sets(1000)
        execution_time = self.timed_execution(lambda: compute_all_numbers_tuple_non_numpy(light_random_sets))
        print(f"\nAll numbers tuple (non-numpy): Execution time: {execution_time:.5f} seconds")

    def test_all_numbers_tuple_numpy(self):
        light_random_sets = self.generate_random_sets(1000)
        execution_time = self.timed_execution(lambda: compute_all_numbers_tuple_numpy(light_random_sets))
        print(f"\nAll numbers tuple (numpy): Execution time: {execution_time:.5f} seconds")

if __name__ == '__main__':
    unittest.main()
