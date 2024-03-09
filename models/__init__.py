#!/usr/bin/python3
"""A Module that defines the init """

from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
