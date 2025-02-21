import unittest
from app.main import app

class TestSecurity(unittest.TestCase):
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_invalid_auth(self):
        """Test access without authentication"""
        response = self.app.get('/protected')
        self.assertEqual(response.status_code, 401)

    def test_valid_auth(self):
        """Test access with valid token"""
        headers = {"Authorization": "Bearer valid_token"}
        response = self.app.get('/protected', headers=headers)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
