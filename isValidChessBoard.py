# isValidChessBoard() is a function that takes a dicitonary argument
# and returns True or False depending on if the board is valid.

# Function to check if spaces on currentBoard are valid.
validPieces = []
for i in ['w', 'b']:
    validPieces += [str(i) + 'king'] + [str(i) + 'queen'] + [str(i) + 'rook'] + \
                    [str(i) + 'bishop'] + [str(i) + 'knight'] + [str(i) + 'pawn']

def isBishopValid(board): # Checks if either bishop is in wrong color square
    blackSquares = []
    for i in range(1, 9, 2):
        blackSquares += [str(i) + 'a'] + [str(i) + 'c'] + \
                        [str(i) + 'e'] + [str(i) + 'h']
    for i in range(2, 9, 2):
        blackSquares += [str(i) + 'b'] + [str(i) + 'd'] + \
                        [str(i) + 'f'] + [str(i) + 'g']
    whiteSquares = []
    for i in range(2, 9, 2):
        whiteSquares += [str(i) + 'a'] + [str(i) + 'c'] + \
                        [str(i) + 'e'] + [str(i) + 'h']
    for i in range(1, 9, 2):
        whiteSquares += [str(i) + 'b'] + [str(i) + 'd'] + \
                        [str(i) + 'f'] + [str(i) + 'g']
    bishops = 



def isValidSpace(board):
    validSpaces = [] # Making a list of valid spaces on chess board.
    for i in range(1, 9):
        validSpaces += [str(i) + 'a'] + [str(i) + 'b'] + [str(i) + 'c'] + \
                        [str(i) + 'd'] + [str(i) + 'e'] + [str(i) + 'f'] + \
                        [str(i) + 'g'] + [str(i) + 'h']
    for space in list(board.keys()):
        if space not in validSpaces:
            return False

def isValidPieces(board):
    
    for piece in list(board.values()):
        if piece not in validPieces:
            return False

# The titular function.
def isValidChessBoard(board):

    pieces = list(currentBoard.values())

    if 'bking' and 'wking' not in board.values(): # Making sure boths kings are still on board.
        print(False)
    elif len(currentBoard) > 32: # Checking no more than 32 pieces on board
        print(False) 
    elif isValidSpace(currentBoard) == False: # Checking spaces are valid
        print(False)
    elif isValidPieces(currentBoard) == False: # Checking all pieces are valid
        print(False)
    # Cheking count of each piece is correct
    elif sum(value == 'wpawn' for value in currentBoard.values()) > 8:
        print(False)
    elif sum(value == 'bpawn' for value in currentBoard.values()) > 8:
        print(False)
    elif sum(value == 'wqueen' for value in currentBoard.values()) > 1:
        print(False)
    elif sum(value == 'bqueen' for value in currentBoard.values()) > 1:
        print(False)
    elif sum(value == 'wking' for value in currentBoard.values()) > 1:
        print(False)
    elif sum(value == 'bking' for value in currentBoard.values()) > 1:
        print(False)
    elif sum(value == 'wrook' for value in currentBoard.values()) > 2:
        print(False)
    elif sum(value == 'brook' for value in currentBoard.values()) > 2:
        print(False)
    elif sum(value == 'wbishop' for value in currentBoard.values()) > 2:
        print(False)
    elif sum(value == 'bbishop' for value in currentBoard.values()) > 2:
        print(False)
    elif sum(value == 'wknight' for value in currentBoard.values()) > 2:
        print(False)
    elif sum(value == 'bknight' for value in currentBoard.values()) > 2:
        print(False)
    else:
        print(True)


currentBoard = {'1a': 'bking', '6c': 'wqueen', '2g': 'bbishop',
                '5h':'bqueen', '3e': 'wking', '1b' : 'wpawn', '1c' : 'wpawn'}


#print(list(currentBoard.values()))
isValidChessBoard(currentBoard)
#print(sum(value == 'wpawn' for value in currentBoard.values()))
print(isBishopValid(currentBoard))