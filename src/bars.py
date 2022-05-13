class Bars:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.room = []
    
    def add_room(self, room):
        self.room.append(room)
    
    def transaction(self, room, guest):
        if room.add_guest(guest) == False:
            if guest.guest_has_enough_money(room) == False:
                self.till += room.fee
                guest.wallet -= room.fee
