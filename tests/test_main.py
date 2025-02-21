import unittest
from app.main import app

class TestMainApp(unittest.TestCase):
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        """Test health check endpoint"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "healthy"})

    def test_user_api(self):
        """Test user API route"""
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

if __name__ == '__main__':
    unittest.main()
