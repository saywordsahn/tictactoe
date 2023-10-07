from random_ai import RandomAI
from engine import Engine

ai = RandomAI('O')
engine = Engine()

board = [["_" for row in range(3)] for i in range(3)]


def printBoard(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()


def isValid(row, col):
    global board
    if row >= 3 or col >= 3:
        return False
    if board[col][row] != "_":
        return False
    return True


def checkWin(board):
    # Check Row
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == 'O' or board[0][i] == board[1][i] == board[2][i] == 'X':
            return True
    # Check Col
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'O' or board[i][0] == board[i][1] == board[i][2] == 'X':
            return True
    # Check Diagonal
    if board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][0] == board[1][1] == board[2][2] == 'X':
        return True
    if board[0][2] == board[1][1] == board[2][0] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'X':
        return True

    return False


def ask(piece, board):
    print(f"Player {piece}'s Turn")
    placement = input("Input the row and col coordinates of the place where you want to place: ")
    row = int(placement[0])
    col = int(placement[2])
    if isValid(row, col):
        board[row][col] = piece
        printBoard(board)
    else:
        print("Error")
        ask(piece)

player = 'X'

for i in range(9):
    ask(player, board)
    if checkWin(board):
        print(f"Player {player} has won the game!")
        break

    print()

    ai.make_move(engine, board)
    printBoard(board)
