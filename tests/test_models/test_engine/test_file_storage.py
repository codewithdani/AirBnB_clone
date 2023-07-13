#!/ursr/bin/env python3
""" Test for storage engine """

import unittest
from models.engine import file_storage

class TestFileStorage(unittest.TestCase):
    """TestFileStorage: set of tests for filestorage
    Args:
        unittest: python testing module
    """

    def test_module_doc(self):
        """ checks for module docs """
        self.assertTrue(len(file_storage.__doc__) > 0)
