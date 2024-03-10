#!/usr/bin/python3
"""A Module that defines the Unit tests for the user module"""


import unittest
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User


class TestState(unittest.TestCase):
    """Test cases for the  user class"""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """cleans the FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        us_1 = User()
        k = f"{type(us_1).__name__}.{us_1.id}"
        self.assertIn(k, storage.all())
        self.assertIsInstance(us_1.email, str)
        self.assertIsInstance(us_1.password, str)
        self.assertIsInstance(us_1.first_name, str)
        self.assertIsInstance(us_1.last_name, str)

    def test_str(self):
        """Test method for str representation"""
        us_1 = User()
        string = f"[{type(us_1).__name__}] ({us_1.id}) {us_1.__dict__}"
        self.assertEqual(us_1.__str__(), string)

    def test_init(self):
        """Test method for the public instances attributes"""
        us_1 = User()
        us_2 = User(**us_1.to_dict())
        self.assertIsInstance(us_1.id, str)
        self.assertIsInstance(us_1.created_at, datetime)
        self.assertIsInstance(us_1.updated_at, datetime)
        self.assertEqual(us_1.updated_at, us_2.updated_at)

    def test_save(self):
        """Tests for the save method"""
        us_1 = User()
        old_update = us_1.updated_at
        us_1.save()
        self.assertNotEqual(us_1.updated_at, old_update)

    def test_todict(self):
        """Test conversion of object attributes to dictionary"""
        us_1 = User()
        us_2 = User(**us_1.to_dict())
        my_dict = us_2.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertEqual(my_dict['__class__'], type(us_2).__name__)
        self.assertIn('created_at', my_dict.keys())
        self.assertIn('updated_at', my_dict.keys())
        self.assertNotEqual(us_1, us_2)


if __name__ == "__main__":
    unittest.main()
