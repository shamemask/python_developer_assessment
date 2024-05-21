import os
import unittest
import datetime
from tempfile import TemporaryDirectory

from task_4 import delete_files_older_than


def create_file_with_old_timestamp(filename, days_ago):
    target_date = datetime.datetime.now() - datetime.timedelta(days=days_ago)
    timestamp = target_date.timestamp()
    with open(filename, 'w') as file:
        file.write("This is a test file.")
    os.utime(filename, (timestamp, timestamp))


class TestFileOperations(unittest.TestCase):

    def setUp(self):
        self.test_dir = TemporaryDirectory()
        self.root_dir = self.test_dir.name

        # Create files and subdirectories
        os.makedirs(os.path.join(self.root_dir, "subdir"))

        # Create files with old timestamps
        self.old_file = os.path.join(self.root_dir, "old_file.txt")
        self.old_sub_file = os.path.join(self.root_dir, "subdir", "old_sub_file.txt")
        self.new_file = os.path.join(self.root_dir, "new_file.txt")

        create_file_with_old_timestamp(self.old_file, 90)
        create_file_with_old_timestamp(self.old_sub_file, 90)
        create_file_with_old_timestamp(self.new_file, 10)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_delete_files_older_than(self):
        delete_files_older_than(self.root_dir, 30)

        self.assertFalse(os.path.exists(self.old_file), "Old file was not deleted")
        self.assertFalse(os.path.exists(self.old_sub_file), "Old file in subdirectory was not deleted")
        self.assertTrue(os.path.exists(self.new_file), "New file was incorrectly deleted")


if __name__ == "__main__":
    unittest.main()
