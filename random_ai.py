import random
from engine import Engine

class RandAI:
    def __init__(self, mark):
        self.mark = mark


    def make_move(self, gameboard):
        valid_move = False
        while not valid_move:
            row = random.randint(1,3)
            col = random.randint(1,3)

            if gameboard[row - 1][col - 1] == '_':
                gameboard[row - 1][col - 1] = self.mark
                valid_move = True