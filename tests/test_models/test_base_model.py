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

if __name__ == '__main__':
    unittest.main()
