#!/usr/bin/python3
"""A Module that defines Unit tests for the city module"""

import unittest
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City

ct1 = City()
ct2 = City(**ct1.to_dict())
ct3 = City("hello", "wait", "in")


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """cleans FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for a public instances attribute"""
        k = f"{type(ct1).__name__}.{ct1.id}"
        self.assertIsInstance(ct1.name, str)
        self.assertEqual(ct3.name, "")
        ct1.name = "Abuja"
        self.assertEqual(ct1.name, "Abuja")

    def test_init(self):
        """Test method for class attributes"""
        self.assertIsInstance(ct1.id, str)
        self.assertIsInstance(ct1.created_at, datetime)
        self.assertIsInstance(ct1.updated_at, datetime)
        self.assertEqual(ct1.updated_at, ct2.updated_at)

    def test_save(self):
        """Test method for save"""
        old_update = ct1.updated_at
        ct1.save()
        self.assertNotEqual(ct1.updated_at, old_update)

    def test_to_dict(self):
        """Test method for dict"""
        my_dict = ct2.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertEqual(my_dict['__class__'], type(ct2).__name__)
        self.assertIn('created_at', my_dict.keys())
        self.assertIn('updated_at', my_dict.keys())
        self.assertNotEqual(ct1, ct2)


if __name__ == "__main__":
    unittest.main()
