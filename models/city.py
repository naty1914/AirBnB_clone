#!/usr/bin/python3
"""A Module that define the class city """

from models.base_model import BaseModel


class City(BaseModel):
    """A class that inherits from BaseModel and represents a City"""
    state_id = ""
    name = ""
