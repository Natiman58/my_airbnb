#!/usr/bin/python3
"""
    A file storeage engine to handle JSON file
    serialization and deserialization
"""
import json
import os

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
        self.__objects[key] = obj
    def save(self):
        """
            serializes __objects dict to a JSON file
            dump on to a JSON file
        """
        with open(self.__file_path, 'w') as f:
            print(self.__objects)
            json.dump(self.__objects, f)

    def reload(self):
        """
            deserialize the json file to a dict object; __objects
            load the object from the json file
        """
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    print(f.read())

                    self.__objects = json.load(f)

                for key, value in self.__objects.items():
                    class_name, obj_id = key.split(".")
                    obj_class = eval(class_name)  # dynamically retrieve class name
                    obj = obj_class(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
