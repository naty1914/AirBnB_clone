#!/usr/bin/python
"""Defines a BaseModel class """

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class which defines other methods and classes

      public instance attributes:
           id(str): provides uniqe id for a specific user
           created_at: assigns current datetime
           updated_at: updates the current datetime

      Methods:
           __str__: prints string representation of the class
           save(self): update instance attribute
                       with the current datetime
           to_dict(self): return the dictionary representation of an instance
    """

    def __init__(self, *args, **kwargs):
        """initializes id, created_at, updated_at """
        if kwargs:
            for keys, value in kwargs.items():
                if keys == 'created_at' or keys == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    self.__dict__[keys] = value
                else:
                    self.__dict__[keys] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """updates the instance attribute with the current date """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance:
        """
        my_dict = self.__dict__.copy()
        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                my_dict[k] = v.isoformat()
            else:
                my_dict[k] = v
        my_dict['__class__'] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """returns [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
