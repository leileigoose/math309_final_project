class Player:
    move_count = 0

    def __init__(self, bank, space, in_jail):
        self.bank = bank
        self.in_jail = in_jail
        self.space = space
        

    def get_bank(self):
        return self.bank

    def set_bank(self, amount):
        self.bank += amount

    def get_space(self):
        return self.space

    def set_space(self, space):
        self.space += space

    @classmethod
    def set_move(cls):
        cls.move_count += 1

    @classmethod
    def get_move(cls):
        return cls.move_count

    def is_in_jail(self):
        return self.in_jail

    def set_jail(self, jail):
        self.in_jail = jail


