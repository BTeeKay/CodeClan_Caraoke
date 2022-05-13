import unittest
from src.guests import Guests
from src.songs import Songs
from src.rooms import Rooms
from src.bars import Bars

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.s1 = Songs("Pnumea", "Tool", 600)
        self.g1 = Guests("Barry", 200, self.s1)
        self.b1 = Bars("The Three Broomsticks", 1000)
        self.r1 = Rooms("Rock Room", 6, 20)

    def test_guest_has_name(self):
        self.assertEqual("Barry", self.g1.name)
    
    def test_guest_has_enough_money(self):
        self.assertFalse(self.g1.guest_has_enough_money(self.r1))