#!/usr/bin/python3
import sys
import datetime
import uuid
"""base_model module"""


class BaseModel:
    """
    class name = BaseModel
    attrinutes = id, created_at, updated_ad
    methods = save(), to_dict()
    """
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __init__(self, *args, **kwargs):
        """class constructor"""
        if len(kwargs) > 0:
            self.__dict__.update(kwargs)
            self.created_at.isoformat()
            self.updated_at.isoformat()
            del self.__dict__["__class__"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()

    def __str__(self):
        """overiding default str method"""
        self.__dict__.update({"id": self.id})
        self.__dict__.update({"updated_at": self.updated_at})
        self.__dict__.update({"created_at": self.created_at})
        obj_dict = self.__dict__
        return "[{}] ({}) {}".format(type(self).__name__, self.id, obj_dict)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetim
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        self.__dict__.update({"__class__": type(self).__name__})
        self.created_at.isoformat()
        self.updated_at.isoformat()
        return self.__dict__
