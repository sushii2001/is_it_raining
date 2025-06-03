import unittest
import json
from src.main import app

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_rain_route(self):
        response = self.app.get('/rain?location=Pulau Tikus')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIn('location', data)
        self.assertIn('latitude', data)
        self.assertIn('longitude', data)
        self.assertIn('is_raining', data)
        self.assertIn('time', data)

if __name__ == '__main__':
    unittest.main()
