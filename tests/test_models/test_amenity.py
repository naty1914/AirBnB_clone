#!/usr/bin/python3
""" A module that defines Unit tests for the `amenity` class"""

import unittest
import os
from datetime import datetime
from models import storage
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Test cases for the `Amenity` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Cleans up FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes_initialization(self):
        """Tests method for class attributes"""
        am1 = Amenity()
        am2 = Amenity(**am1.to_dict())
        am3 = Amenity("hello", "wait", "in")

        s = f"{type(am1).__name__}.{am1.id}"
        self.assertIsInstance(am1.name, str)
        self.assertIn(s, storage.all())
        self.assertEqual(am3.name, "")

    def test_public_instances(self):
        """Tests public instance attributes"""
        am1 = Amenity()
        am2 = Amenity(**am1.to_dict())
        self.assertIsInstance(am1.id, str)
        self.assertIsInstance(am1.created_at, datetime)
        self.assertIsInstance(am1.updated_at, datetime)
        self.assertEqual(am1.updated_at, am2.updated_at)

    def test_str_repr(self):
        """Tests  method for str_repr"""
        am1 = Amenity()
        string_expected = f"[{type(am1).__name__}] ({am1.id}) {am1.__dict__}"
        self.assertEqual(am1.__str__(), string_expected)

    def test_save(self):
        """Test method for save"""
        am1 = Amenity()
        old_One = am1.updated_at
        am1.save()
        self.assertNotEqual(am1.updated_at, old_One)

    def test_todict(self):
        """Test method for dict"""
        am1 = Amenity()
        am2 = Amenity(**am1.to_dict())
        am_dict = am2.to_dict()
        self.assertIsInstance(am_dict, dict)
        self.assertEqual(am_dict['__class__'], type(am2).__name__)
        self.assertNotEqual(am1, am2)
        self.assertIn('created_at', am_dict.keys())
        self.assertIn('updated_at', am_dict.keys())


if __name__ == "__main__":
    unittest.main()
