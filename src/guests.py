class Guests:
    def __init__(self, name, wallet, song):
        self.name = name
        self.wallet = wallet
        self.song = song
    
    def guest_has_enough_money(self, room):
        if self.wallet < room.fee:
            return True
        return False
