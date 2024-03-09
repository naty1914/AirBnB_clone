#!/usr/bin/python3
"""A MOdule that defines Unit tests for the city module"""

import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for the place class"""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """cleans the FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        pl_1 = Place()
        pl_3 = Place("hello", "wait", "in")
        k = f"{type(pl_1).__name__}.{pl_1.id}"
        self.assertIsInstance(pl_1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(pl_3.name, "")

        self.assertIsInstance(pl_1.name, str)
        self.assertIsInstance(pl_1.user_id, str)
        self.assertIsInstance(pl_1.city_id, str)
        self.assertIsInstance(pl_1.description, str)
        self.assertIsInstance(pl_1.number_bathrooms, int)
        self.assertIsInstance(pl_1.number_rooms, int)
        self.assertIsInstance(pl_1.price_by_night, int)
        self.assertIsInstance(pl_1.max_guest, int)
        self.assertIsInstance(pl_1.longitude, float)
        self.assertIsInstance(pl_1.latitude, float)
        self.assertIsInstance(pl_1.amenity_ids, list)

    def test_init(self):
        """Test method for public instances attributes"""

        pl_1 = Place()
        pl_2 = Place(**pl_1.to_dict())
        self.assertIsInstance(pl_1.id, str)
        self.assertIsInstance(pl_1.created_at, datetime)
        self.assertIsInstance(pl_1.updated_at, datetime)
        self.assertEqual(pl_1.updated_at, pl_2.updated_at)

    def test_str_repr(self):
        """Test method for str_repr"""
        pl_1 = Place()
        string = f"[{type(pl_1).__name__}] ({pl_1.id}) {pl_1.__dict__}"
        self.assertEqual(pl_1.__str__(), string)

    def test_save(self):
        """Tests the save method"""
        pl_1 = Place()
        old_update = pl_1.updated_at
        pl_1.save()
        self.assertNotEqual(pl_1.updated_at, old_update)

    def test_todict(self):
        """Test conversion of object attributes to dictionary"""
        pl_1 = Place()
        pl_2 = Place(**pl_1.to_dict())
        my_dict = pl_2.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertEqual(my_dict['__class__'], type(pl_2).__name__)
        self.assertIn('created_at', my_dict.keys())
        self.assertIn('updated_at', my_dict.keys())
        self.assertNotEqual(pl_1, pl_2)


if __name__ == "__main__":
    unittest.main()
