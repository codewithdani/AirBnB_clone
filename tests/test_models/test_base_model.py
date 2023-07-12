#!usr/bin/env python3
"""
    unittest for base model
"""

import unittest
from models import base_model

class TestBaseModel(unittest.TestCase):
    """TestBaseModels: performs test on basemodel
    Args:
        unittest: python testing module
    """

    def test_module_doc(self):
        """ checks for module documentation """
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(base_model.BaseModel.__doc__) > 0)

    def test_method_doc(self):
        """ tests for method documentation """
        for method in dir(base_model.BaseModel):
            self.assertTrue(len(method.__doc__) > 0)

    def test_uuid(self):
        """ tests for correct and unique uuid """
        first = base_model.BaseModel()
        second = base_model.BaseModel()
        
        self.assertNotEqual(first.id, second.id)

if __name__ == '__main__':
    unittest.main()
