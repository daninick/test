import random


class Dice:
    def roll(self):
        first_dice = random.randint(1,6)
        second_dice = random.randint(1,6)
        return first_dice,second_dice


dice = Dice()
print(dice.roll())