class Engine:

    def __init__(self):
        pass

    def is_winner(self, gameboard, mark):

        playerwin = False

        for i in range (3):
            if gameboard[0][i] == gameboard[1][i] == gameboard[2][i] == mark:
                playerwin =True
            if gameboard[i][0] == gameboard[i][1] == gameboard[i][2] == mark:
                playerwin = True
        if gameboard[0][0] == gameboard [1][1] == gameboard [2][2] == mark:
            playerwin = True
        if gameboard[0][2] == gameboard [1][1] == gameboard [2][0] == mark:
            playerwin = True

        return playerwin