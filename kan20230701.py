import random
from engine import Engine
from random_ai import RandomAI


playerwin = False

engine = Engine()
ai = RandomAI("O")

def print_board(board):
    for row in range(3):
        for col in range(3):
            print(board[row][col], end=' ')
        print()

    print()


gameboard = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]

mark = 'X'
for turn in range(9):

    print('PLAYER X')

    valid_move = False

    # check if the input is valid
    while valid_move == False:
        row = int(input('Enter a row from 1-3: '))
        col = int(input('Enter a col from 1-3: '))

        if gameboard[row - 1][col - 1] == '_':
            gameboard[row - 1][col - 1] = mark
            valid_move = True

    print_board(gameboard)

    # now check if x is a winner
    # how to do this?
    if engine.is_winner(gameboard, 'X'):
        print('X won the game')
        break

    # player
    print('PLAYER O')
    ai.make_move(engine, gameboard)

    print_board(gameboard)

    if engine.is_winner(gameboard, 'O'):
        print('O won the game')
        break

