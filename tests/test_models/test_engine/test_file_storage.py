#!/usr/bin/env python3
""" Test for storage engine """

import unittest
import os
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """TestFileStorage: set of tests for filestorage
    Args:
        unittest: python testing module
    """

    def setUp(self):
        """ prep necessary data """
        self.data = FileStorage()

    def test_module_doc(self):
        """ checks for module docs """
        self.assertTrue(len(file_storage.__doc__) > 1)

    def test_class_doc(self):
        """ checks for class docs """
        self.assertTrue(len(self.data.__doc__) > 1)

    def test_method_doc(self):
        """ checks for method docs """
        for method in dir(self.data):
            self.assertTrue(len(method) > 1)

    def test_initialization(self):
        """ checks for class initialization """
        obj = self.data
        self.assertIsInstance(obj, FileStorage)

    def test_all_method(self):
        """ checks for all methon type """
        my_obj = self.data
        my_dict = my_obj.all()
        self.assertTrue(type(my_dict) == dict)

    def test_new_method(self):
        """ checks for new method """
        my_obj = self.data
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_dict = my_obj.all()
        form = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertTrue(form in my_dict)


    def test_reload_method(self):
        """ checks the reload method """
        first = self.data
        new_obj = BaseModel()
        first.new = (new_obj)
        first.save()
        my_dict1 = first.all()
        os.remove("file.json")
        first.reload()
        my_dict2 = first.all()
        self.assertTrue(my_dict1 == my_dict2)


    def test_save_method(self):
        """ checks for the save method of filrstorage"""
        first = self.data
        new_obj = BaseModel()
        first.new(new_obj)
        my_dict1 = first.all()
        first.save()
        first.reload()
        my_dict2 = first.all()
        for key in my_dict1:
            key1 = key
        for key in my_dict2:
            key2 = key
        self.assertEqual(my_dict1[key1].to_dict(), my_dict2[key2].to_dict())


if __name__ == "__main__":
    unittest.main()
