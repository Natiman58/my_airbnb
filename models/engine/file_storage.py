#!/usr/bin/python3
"""
    A module for serialization and deserialization
"""
import json
import os
from datetime import datetime
from models.user import User
from models.base_model import BaseModel

from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review  import Review

class FileStorage:
    """
        stores the json files and the dict objects
    """
    __file_path = 'file.json'
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }
    
    def all(self):
        """
            returns all the objects
        """
        return self.__objects
    
    def new(self, obj):
        """
            saves the new obj in the __obj dict with key
            obj_class_name.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj
    
    def save(self):
        """ 
            saves the object into a json file;
            serialization
        """
        obj_dict = {}
        for key, val in self.__objects.items():
            if isinstance(val, BaseModel):
                new_val = val.to_dict()
                obj_dict[key] = new_val
            elif isinstance(val, datetime):
                new_val = datetime.isostream()
                obj_dict[key] = new_val
            else:
                obj_dict[key] = val

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict, f, indent=4)

    def reload(self):
        """
            deserializes the json file into a dict obj
        """
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    data = json.load(f)
                    for key, value in data.items():
                        class_name = key.split('.')[0]
                        obj_class = self.classes.get(class_name)
                        if obj_class:
                            obj = obj_class(**value)
                            self.__objects[key] = obj
            else:
                pass
        except FileNotFoundError:
            pass
