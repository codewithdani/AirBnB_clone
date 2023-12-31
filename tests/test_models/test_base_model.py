#!usr/bin/env python3
"""
    unittest for base model
"""
import unittest
from datetime import datetime
from models import base_model
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseModels: performs test on basemodel
    Args:
        unittest: python testing module
    """

    def test_module_doc(self):
        """ checks for module documentation """
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """ checks for class documentation """
        self.assertTrue(len(base_model.BaseModel.__doc__) > 0)

    def test_method_doc(self):
        """ checks for method documentation """
        for method in dir(base_model.BaseModel):
            self.assertTrue(len(method.__doc__) > 0)

    def test_uuid(self):
        """ checks for correct and unique uuid """
        first = BaseModel()
        second = BaseModel()
        self.assertNotEqual(first.id, second.id)
        self.assertTrue(type(first.id) == str)
        self.assertTrue(type(second.id) == str)

    def test_datetime_type(self):
        """ checks for time type """
        first = BaseModel()
        second = BaseModel()

        self.assertTrue(type(first.created_at) == datetime)
        self.assertTrue(type(first.updated_at) == datetime)

    def test_save_method(self):
        """ checks for save method """
        first = BaseModel()
        create = first.created_at
        update = first.updated_at

        first.save()
        self.assertIsNotNone(first.id)
        self.assertIsNotNone(first.created_at)
        self.assertIsNotNone(first.updated_at)
        self.assertNotEqual(create, update)

    def test_to_dict_method(self):
        """ checks to_dict method """
        first = BaseModel()
        var_dict = first.to_dict()
        self.assertIsInstance(var_dict, dict)
        self.assertIn('id', var_dict)
        self.assertEqual(var_dict["id"], first.id)

    def test_initialization(self):
        """ checks for iitialization of basemodel """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_str_representation(self):
        """ checks for str method """
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)


if __name__ == '__main__':
    unittest.main()
