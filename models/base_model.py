#!/usr/bin/python3
"""
    A base model for all the objectes
"""
from uuid import uuid4
from datetime import datetime
#from models import storage

class BaseModel:
    """
        A base model for all the objects
    """
    def __init__(self, *args, **kwargs):
        from models import storage
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    self.id = kwargs.get('id')
                    self.created_at = datetime.strptime(kwargs.get('created_at'), '%Y-%m-%dT%H:%M:%S.%f')
                    self.updated_at = datetime.strptime(kwargs.get('updated_at'), '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            returns the string representation of the object
            class name + id + dict(attribures list)
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the upadted at attribute with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """
            returns all the attributes in the class obj
        """
        copy_dict = self.__dict__.copy()
        copy_dict['__class__'] = self.__class__.__name__
        copy_dict['created_at'] = datetime.now().isoformat()
        copy_dict['updated_at'] = datetime.now().isoformat()
        return copy_dict

    