import unittest
from todo import create_app

class TodoTest(unittest.TestCase):
    def setUp(self):
        """Set up the test client and database."""
        self.app = create_app(config_overrides={
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'TESTING': True
        })
        self.client = self.app.test_client()
    
    def assertDictSubset(self, expected_subset: dict, whole: dict):
        """Helper method to check if expected_subset exists within whole dictionary."""
        for key, value in expected_subset.items():
            self.assertEqual(whole[key], value)
