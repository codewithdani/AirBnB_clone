#!/usr/bin/env python3
""" module for basemodel creation """
import datetime
import uuid
import models

class BaseModel():
    """ The base modeks class """
    def __init__(self, *args, **kwargs):
        """ initializes base model
        Args:
            args: positional arrguments
            kwargs: keyword aegunents
        """

        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.strptime(value, date_format)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)

    def __str__(self):
        """ returns in format """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates updated_at and makes petsist"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return dictionary repr of model """
        dict_copy = dict(self.__dict__)
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
