#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        del cls.HBNB

    def setUp(self):
        """Reset FileStorage objects dictionary."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
            pass

    def test_create_for_errors(self):
                "** class doesn't exist **\n", f.getvalue())

    def test_create_command_validity(self):
            self.assertIn(am, f.getvalue())

    def test_create_command_with_kwargs(self):
            self.assertIn("'longitude': 43.434", output)


if __name__ == "__main__":
    unittest.main()
