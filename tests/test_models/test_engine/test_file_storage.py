#!/usr/bin/env python3
""" Test for storage engine """

import unittest
import os
from models.engine import file_storage
from models.engine.file_storage import FileStorage


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
