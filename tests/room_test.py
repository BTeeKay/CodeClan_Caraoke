from logging import root
import unittest
from src.rooms import Rooms
from src.bars import Bars
from src.guests import Guests
from src.songs import Songs

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.bar1 = Bars("The Three Broomsticks", 1000)
        self.room1 = Rooms("Rock Room", 6, 20)
        self.bar1.add_room(self.room1)
        self.s1 = Songs("Pneuma", "Tool", 600)
        self.guest1 = Guests("Barry", 100, self.s1)
        self.s2 = Songs("Zeit", "Rammstein", 500)
        self.guest2 = Guests("Gary", 50, self.s2)
    
    def test_add_guest(self):
        self.room1.add_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_remove_guest(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.room1.remove_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))
    
    def test_cant_add_same_guest_twice(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_cant_remove_same_guest_twice(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.room1.remove_guest(self.guest1)
        self.room1.remove_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))
    
    def test_room_can_play_song(self):
        self.room1.play_song(self.s1)
        self.assertEqual("Pneuma", self.room1.playing.name)
    
    def test_cant_add_guest_if_capacity_full(self):
        self.r2 = Rooms("small room", 1, 15)
        self.r2.add_guest(self.guest1)
        self.assertTrue(self.r2.add_guest(self.guest2))
    
    def test_cheer_when_fav_song(self):
        self.room1.add_guest(self.guest2)
        self.assertEqual("This is my Jaaaam", self.room1.play_song(self.s2))
    
    def test_dont_cheer_when_not_fav_song(self):
        self.room1.add_guest(self.guest2)
        self.assertEqual(None, self.room1.play_song(self.s1))

    def test_clear_room(self):
        self.room1.clear_room()
        self.assertEqual(0, len(self.room1.guests))