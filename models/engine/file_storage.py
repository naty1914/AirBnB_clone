#!/usr/bin/python3
"""A module that defines  a class FileStorage"""

import os
import json
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ A class that serializes instances to a JSON file"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionaty __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """saves the serialized object to a JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Reloads the deserialized the Json file"""
        my_classes = {
                     "BaseModel": BaseModel,
                     "User": User,
                     "State": State,
                     "City": City,
                     "Amenity": Amenity,
                     "Place": Place,
                     "Review": Review
                     }

        if not os.path.exists(FileStorage.__file_path):
            return

        data = None
        try:
            with open(FileStorage.__file_path, "r") as ds:
                data = json.load(ds)
        except Exception:
            pass
        if data is None:
            return
        FileStorage.__objects = {
                k: my_classes[k.split('.')[0]](**v)
                for k, v in data.items()}
