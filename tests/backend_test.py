import os
import sys
import unittest
import json


from src.backend.main import app

class TestBackend(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_weather(self):
        response = self.app.get('/weather?location=Kuala Lumpur')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        print(f"data: {data}")
        self.assertEqual(data['location'], 'Kuala Lumpur')
        self.assertIn('is_raining', data)

if __name__ == '__main__':
    unittest.main()
