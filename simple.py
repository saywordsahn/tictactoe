
def isvalid():
    if row > 2:
        print("invalid row")
        print("invalid col")

def printboard(board):
    print(board[0][0] + ' ' + board[0][1] + ' ' + board[0][2])
    print(board[1][0] + ' ' + board[1][1] + ' ' + board[1][2])
    print(board[2][0] + ' ' + board[2][1] + ' ' + board[2][2])

board = [["_","_","_"],
        ["_","_","_"],
        ["_","_","_"]]
print(board)

row = int(input("enter a row"))
print (row)
col = int(input("enter a column"))
print(col)


printboard(board)
