from random import randint

class Die:
    def __init__(self, die_side=6):
        self.die_side = die_side

    def roll(self):
        return randint(1, self.die_side)