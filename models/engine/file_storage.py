#!/usr/bin/python3
"""Defines the FileStorage class."""
import json


class FileStorage:
    """Represent an interface to save and reload data in JSON format."""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return all objects in storage."""
        if cls is None:
            return self.__objects

        objects = {}
        for key, value in self.__objects.items():
            if isinstance(value, cls):
                objects[key] = value

        return objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize the objects to the JSON file."""
        serialized_objs = {}
        for key, value in self.__objects.items():
            serialized_objs[key] = value.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserialize the objects from the JSON file."""
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                obj_dict = json.load(f)
        except FileNotFoundError:
            return

        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

        for key, value in obj_dict.items():
            class_name = key.split('.')[0]
            if class_name in classes:
                self.__objects[key] = classes[class_name](**value)

    def close(self):
        """Deserialize the JSON file to objects"""
        self.reload()
