import unittest
from src.guests import Guests

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.g1 = Guests("Barry", 500, 500)

    def test_guest_has_name(self):
        self.assertEqual("Barry", self.g1.name)