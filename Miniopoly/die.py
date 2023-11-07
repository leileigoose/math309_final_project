import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)



d1 = Die()
d2 = Die()

print(d1.roll())
