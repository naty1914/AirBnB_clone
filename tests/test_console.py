#!/usr/bin/python3
"""A Module that Defines unittests for console.py"""

import unittest
import os
import json
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class TestBaseModel(unittest.TestCase):
    """Test cases for the HBNBCommand CLI"""

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self) -> None:
        """Clean up FileStorage data"""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_base_model(self):
        """ Tests the create method for BaseModel object"""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd('create BaseModel')
            self.assertIsInstance(file.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                file.getvalue().strip()), storage.all().keys())

    def test_all_base_model(self):
        """Tests the all method for BaseModel object"""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd('all BaseModel')
            for item in json.loads(file.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_base_model(self):
        """Test showing a specific BaseModel object"""
        with patch('sys.stdout', new=StringIO()) as f:
            bm1 = BaseModel()
            bm1.color = "blue"
            HBNBCommand().onecmd(f'show BaseModel {bm1.id}')
            res = f"[{type(bm1).__name__}] ({bm1.id}) {bm1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_destroy_base_model(self):
        """Tests destroying a specific BaseModel object"""
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(f'destroy BaseModel {bm.id}')
            self.assertNotIn("BaseModel.{}".format(
                bm.id), storage.all().keys())

    def test_update_base_model(self):
        """Tests updating a specific BaseModel object"""
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cecilia"
            str_update = f'update BaseModel {b1.id} \'{{"name": "Ife"}}\''
            HBNBCommand().onecmd(str_update)
            self.assertEqual(b1.name, "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            b2 = BaseModel()
            b2.savings = 25.67
            str_update = f'update BaseModel {b2.id} \'{{"savings": 35.89}}\''
            HBNBCommand().onecmd(str_update)
            self.assertIn("savings", b2.__dict__.keys())
            self.assertEqual(b2.savings, 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            b3 = BaseModel()
            b3.age = 60
            HBNBCommand().onecmd(f'update BaseModel {b3.id} \'{{"age": 10}}\'')
            self.assertIn("age", b3.__dict__.keys())
            self.assertEqual(b3.age, 10)
