#!/usr/bin/python3
"""A Module that defines a class Review """

from models.base_model import BaseModel


class Review(BaseModel):
    """A class that inherits from BaseModel and represents a review"""
    place_id = ""
    user_id = ""
    text = ""
