#!/usr/bin/python3
"""A Module Defines unittests for FileStorage module."""

import unittest
import models
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """Taste case  for testing instantiation of the FileStorage class"""

    def test_FileStorage_instantiation_no_args(self):
        """Test FileStorage instantiation without arguments."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """Test FileStorage instantiation with an argument."""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Test if the file_path attribute is private and of type str."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        """Test if the objects attribute is private and of type dict."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """Test if models.storage is an instance of FileStorage."""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Unit tests for testing methods of the FileStorage class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """cleans the FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test the all method"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """Tests the all method with an argument"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """Tests the new method"""
        bm = BaseModel()
        st = State()
        ct = City()
        us = User()
        am = Amenity()
        pl = Place()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("City." + ct.id, models.storage.all().keys())
        self.assertIn(ct, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        """Tests the new method with arguments"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """Tests the new method with None"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """Test the save method."""
        bm = BaseModel()
        st = State()
        ct = City()
        us = User()
        am = Amenity()
        pl = Place()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(st)
        models.storage.new(us)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(pl)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("City." + ct.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        """Tests the save method with an argument"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """Tests the reload method"""
        bm = BaseModel()
        st = State()
        ct = City()
        us = User()
        am = Amenity()
        pl = Place()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(st)
        models.storage.new(ct)
        models.storage.new(us)
        models.storage.new(am)
        models.storage.new(pl)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + ct.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        """Tests the reload method with an argument"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
