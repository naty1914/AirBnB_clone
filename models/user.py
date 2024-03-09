#!/usr/bin/python3
"""A Module that Defines the  user class """

from models.base_model import BaseModel


class User(BaseModel):
    """A User class that inherits from BaseModel and manage users objects"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
