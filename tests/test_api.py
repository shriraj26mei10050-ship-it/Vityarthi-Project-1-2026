import unittest
import json
from app import app

class CampusLiveTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'Online')

    def test_get_rooms(self):
        response = self.app.get('/api/rooms')
        self.assertEqual(response.status_code, 200)

    def test_allocate_room(self):
        payload = {"student": "Amit Sharma", "type": "AC"}
        response = self.app.post('/api/rooms/allocate', 
                                 data=json.dumps(payload), 
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
