import unittest
from src.bars import Bars
from src.rooms import Rooms
from src.songs import Songs
from src.guests import Guests

class TestBar(unittest.TestCase):
    
    def setUp(self):
        self.bar1 = Bars("The Three Broomsticks", 1000)
        self.room1 = Rooms("Rock Room", 6, 20)
        self.song1 = Songs("Pnumea", "Tool", 600)
        self.guest1 = Guests("Barry", 200, self.song1)
    
    def test_add_room_to_bar(self):
        self.bar1.add_room(self.room1)
        self.assertEqual(1, len(self.bar1.room))
    
    def test_add_fee_to_till(self):
        self.bar1.transaction(self.room1, self.guest1)
        self.assertEqual(1020, self.bar1.till)