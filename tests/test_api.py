import unittest
import sys
import os

# Add src folder to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from app import app


class ExpenseAPITest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_expenses(self):
        response = self.client.get("/expenses")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()