#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to
    instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)."""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                deserialized_objects = json.load(f)
                for key, value in deserialized_objects.items():
                    class_name = key.split('.')[0]
                    obj = eval(class_name + "(**value)")
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects."""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def close(self):
        """Call reload() method."""
        self.reload()
