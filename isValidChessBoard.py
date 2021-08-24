# isValidChessBoard() is a function that takes a dicitonary argument
# and returns True or False depending on if the board is valid

# Making a list of valid spaces on chess board.
validSpaces = []
for i in range(1, 9):
    validSpaces += [str(i) + 'a'] + [str(i) + 'b'] + [str(i) + 'c'] + \
                    [str(i) + 'd'] + [str(i) + 'e'] + [str(i) + 'f'] + \
                    [str(i) + 'g'] + [str(i) + 'h']

# The titular funciton.
def isValidChessBoard(board):
    if 'bking' and 'wking' not in board.values(): # Making sure boths kings are still on board.
        print(False)
    elif list(board.keys()) in validSpaces: # My attempt to compare the keys with the valid spaces. 
        print(False)
    else:
        print(True)
    
currentBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
                '5h':'bqueen', '3e': 'wking'}

# print(validSpaces)
# print(currentBoard.keys())
isValidChessBoard(currentBoard)