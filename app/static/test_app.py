import unittest
from app.main import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        """ Set up test client """
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_health_check(self):
        """ Test the health check endpoint """
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"healthy", response.data)

    def test_user_login(self):
        """ Test user login API """
        response = self.client.post("/login", json={"username": "testuser", "password": "password"})
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
