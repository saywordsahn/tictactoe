import random
from engine import Engine
from random_ai import RandAI


playerwin = False

engine = Engine()

ai = RandAI("O")

def print_board(board):
    for row in range(3):
        for col in range(3):
            print(board[row][col], end=' ')
        print()

    print()

gameboard = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]

print_board(gameboard)

mark = 'X'
for turn in range(9):

    print('PLAYER', mark)

    valid_move = False

    while valid_move == False:
        row = int(input('Enter a row from 1-3: '))
        col = int(input('Enter a col from 1-3: '))

        if gameboard[row - 1][col - 1] == '_':
            gameboard[row - 1][col - 1] = mark
            valid_move = True

    print_board(gameboard)

    if engine.is_winner(gameboard, "X") == True:
        print ("X", "player has won!")
        break

    print_board(gameboard)
    ai.make_move(gameboard)
    print_board(gameboard)

    if engine.is_winner(gameboard, "0") == True:
        print("0", "player has won!")
        break