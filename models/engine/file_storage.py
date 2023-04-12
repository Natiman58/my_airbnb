#!/usr/bin/python3
"""
    A file storeage engine to handle JSON file
    serialization and deserialization
"""
import json
import os
from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        from models.base_model import BaseModel
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, BaseModel):
            return obj.to_dict()
        else:
            return super().default(obj)

class FileStorage:
    """
        that serializes instances to a JSON file
        and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
            return the dict of __objects
        """
        return self.__objects

    def new(self, obj):
        """
            adds obj to the __objects dict
            with key 'obj class name.id'
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()
        #print(f"The new obj added-> {self.__objects}")

    def save(self):
        """
            Serializes __objects to the JSON file (path: __file_path)
        """
        from models.base_model import BaseModel
        objs_dict = {}
        for key, value in self.__objects.items():
            if isinstance(value, BaseModel):
                objs_dict[key] = value.to_dict()
            objs_dict[key] = value

        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(objs_dict, f, indent=4, cls=CustomJSONEncoder)

    def reload(self):
        """
            Deserialize the JSON file to a dict object;
            Load the object from the JSON file
        """
        from models.base_model import BaseModel
        class_map = {
            'BaseModel': BaseModel
        }
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, 'r', encoding="utf-8") as f:
                    data = json.load(f)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        obj_class = class_map.get(class_name)
                        if obj_class:
                                obj = obj_class(**value)
                                self.__objects[key] = obj
        except FileNotFoundError:
            pass
