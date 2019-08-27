#!/usr/bin/python3

from api import app
import unittest

class FlaskTest(unittest.TestCase):

    def flask_test(self):
        app_exec = app()

        self.assertIsNotNone(app_exec)

if __name__ == '__main__':
   unittest.main()
