#!/usr/bin/python3
"""A Module that defines Unit tests for the review module"""

import unittest
import os
from models import storage
from models.review import Review
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Test cases for the review class"""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Cleans the  FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        rv1 = Review()
        rv3 = Review("hello", "wait", "in")
        k = f"{type(r1).__name__}.{r1.id}"
        self.assertIsInstance(r1.text, str)
        self.assertIsInstance(r1.user_id, str)
        self.assertIsInstance(r1.place_id, str)
        self.assertEqual(rv3.text, "")

    def test_init(self):
        """Test method for class attributes"""
        rv1 = Review()
        rv2 = Review(**r1.to_dict())
        self.assertIsInstance(r1.id, str)
        self.assertIsInstance(r1.created_at, datetime)
        self.assertIsInstance(r1.updated_at, datetime)
        self.assertEqual(r1.updated_at, rv2.updated_at)

    def test_str_repr(self):
        """Test method for str_repr"""
        rv1 = Review()
        string = f"[{type(r1).__name__}] ({r1.id}) {r1.__dict__}"
        self.assertEqual(r1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        rv1 = Review()
        old_update = r1.updated_at
        r1.save()
        self.assertNotEqual(r1.updated_at, old_update)

    def test_to_dict(self):
        """Tests conversion of object attributes to dictionary"""
        rv1 = Review()
        rv2 = Review(**r1.to_dict())
        my_dict = rv2.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertEqual(my_dict['__class__'], type(rv2).__name__)
        self.assertIn('created_at', my_dict.keys())
        self.assertIn('updated_at', my_dict.keys())
        self.assertNotEqual(r1, rv2)


if __name__ == "__main__":
    unittest.main()
