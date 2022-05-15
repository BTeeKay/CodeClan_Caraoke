class Rooms:
    def __init__(self, name, capacity, fee):
        self.name = name
        self.capacity = capacity
        self.guests = []
        self.playing = None
        self.fee = fee
    
    def add_guest(self, guest):
        for g in self.guests:
            if g == guest:
                return None
        if len(self.guests) >= self.capacity:
            return True
        self.guests.append(guest)
        return False
    
    def remove_guest(self, guest):
        for g in self.guests:
            if g == guest:
                self.guests.remove(guest)

    def play_song(self, song):
        self.playing = song
        for g in self.guests:
            if g.song == song:
                return "This is my Jaaaam"

    def clear_room(self):
        self.guests.clear()