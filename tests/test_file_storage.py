import os
import unittest

from scripts.file_storage import (
    create_storage,
    upload_file,
    list_files,
    read_file,
    delete_file
)

from config import STORAGE_PATH


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        create_storage()

        self.test_file = "test_file.txt"

        with open(self.test_file, "w", encoding="utf-8") as file:
            file.write("Hello, World!")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        for filename in list_files():
            filepath = os.path.join(STORAGE_PATH, filename)

            if os.path.exists(filepath):
                os.remove(filepath)

    def test_upload_file(self):
        upload_file(self.test_file)

        self.assertIn(
            "test_file.txt",
            list_files()
        )

    def test_read_file(self):
        upload_file(self.test_file)

        content = read_file("test_file.txt")

        self.assertEqual(
            content,
            "Hello, World!"
        )

    def test_delete_file(self):
        upload_file(self.test_file)

        delete_file("test_file.txt")

        self.assertNotIn(
            "test_file.txt",
            list_files()
        )

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            read_file("does_not_exist.txt")


if __name__ == "__main__":
    unittest.main()