import unittest
from modules import allocation, tickets, gatepass

class TestHostelSystem(unittest.TestCase):
    def test_room_booking(self):
        output = allocation.allocate_room("Rohan", "Non-AC")
        self.assertEqual(output["status"], "success")

    def test_complaint_logging(self):
        output = tickets.create_ticket("201", "Light fuse")
        self.assertEqual(output["status"], "success")

    def test_gate_pass_request(self):
        output = gatepass.request_outpass("Rohan", "Market")
        self.assertEqual(output["status"], "success")

if __name__ == '__main__':
    unittest.main()
