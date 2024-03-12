#!/usr/bin/python3
"""A Module for Testing the base model class """

import unittest
import json
import os
import uuid
import time
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """Test cases for the base class """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary"""
        base1 = BaseModel()
        base2_uuid = str(uuid.uuid4())
        base2 = BaseModel(id=base2_uuid, name="The Weeknd", album="Trilogy")
        base1_dict = base1.to_dict()
        self.assertIsInstance(base1_dict, dict)
        self.assertIn('id', base1_dict.keys())
        self.assertIn('created_at', base1_dict.keys())
        self.assertIn('updated_at', base1_dict.keys())
        self.assertEqual(base1_dict['__class__'], type(base1).__name__)

    def test_initial(self):
        """Test positive cases of the BaseModel initialization. """
        base1 = BaseModel()
        base2_uuid = str(uuid.uuid4())
        base2 = BaseModel(id=base2_uuid, name="The Weeknd", album="Trilogy")
        self.assertIsInstance(base1.id, str)
        self.assertIsInstance(base2.id, str)
        self.assertEqual(base2_uuid, base2.id)
        self.assertEqual(base2.album, "Trilogy")
        self.assertEqual(base2.name, "The Weeknd")
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.created_at, datetime)
        self.assertEqual(str(type(base1)),
                         "<class 'models.base_model.BaseModel'>")

    def test_save(self):
        """Test method for save"""
        base = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        base.save()
        diff = base.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_save_storage(self):
        """Tests that storage.save() is called from save()."""
        base = BaseModel()
        base.save()
        key = "{}.{}".format(type(base).__name__, base.id)
        data = {key: base.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(data)))
            f.seek(0)
            self.assertEqual(json.load(f), data)

    def test_str(self):
        """Tests the str representation"""
        base1 = BaseModel()
        string = f"[{type(base1).__name__}] ({base1.id}) {base1.__dict__}"
        self.assertEqual(base1.__str__(), string)


if __name__ == "__main__":
    unittest.main()
