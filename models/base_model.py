#!/usr/bin/python3
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
        A class to handle model creation
        for each object
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, val)
            print(f'over here ->> {kwargs} ---')
            self.id = str(kwargs.get('id', uuid.uuid4()))
            self.created_at = datetime.strptime(kwargs.get('created_at'), '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs.get('updated_at'), '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f'[{self.__class__.__name__ }] ({ self.id }) {self.__dict__})'

    def save(self):
        #self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Returns the dictionary representation/serialization
            and adds the key '__class__' for the class name
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        return self.__dict__
