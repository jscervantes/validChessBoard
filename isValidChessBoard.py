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
    wBishopWSquare = 0
    wBishopBSquare = 0  
    bBishopWSquare = 0
    bBishopBSquare = 0                 
    for k, v in currentBoard.items():
        if v == 'wbishop' and k in whiteSquares:
            wBishopWSquare += 1
        elif v == 'wbishop' and k in blackSquares:
            wBishopBSquare += 1
        elif v == 'bbishop' and k in whiteSquares:
            bBishopWSquare += 1
        elif v == 'bbishop' and k in blackSquares:
            bBishopBSquare += 1
    if wBishopWSquare > 1 or wBishopBSquare > 1 or bBishopWSquare > 1 or bBishopBSquare > 1:
        return False




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

    pieces = list(board.values())

    # Making sure boths kings are still on board.
    if 'bking' not in board.values():
        print('You are missing a black king.')
    elif 'wking' not in board.values():
        print('You are missing a white king.')
    elif len(board) > 32: # Checking no more than 32 pieces on board
        print('You have too many pieces!') 
    elif isValidSpace(board) == False: # Checking spaces are valid
        print("These space numbers are invalid.")
    elif isValidPieces(board) == False: # Checking all pieces are valid
        print("A piece or pieces are invalid.")
    # Cheking count of each piece is correct
    elif sum(value == 'wpawn' for value in currentBoard.values()) > 8:
        print('You have too many white pawns.')
    elif sum(value == 'bpawn' for value in currentBoard.values()) > 8:
        print('You have too many black pawns.')
    elif sum(value == 'wqueen' for value in currentBoard.values()) > 1:
        print('You have an extra white queen.')
    elif sum(value == 'bqueen' for value in currentBoard.values()) > 1:
        print('You have an extra black queen.')
    elif sum(value == 'wking' for value in currentBoard.values()) > 1:
        print('You have an extra white king.')
    elif sum(value == 'bking' for value in currentBoard.values()) > 1:
        print('You have an extra black king.')
    elif sum(value == 'wrook' for value in currentBoard.values()) > 2:
        print('You have too many white rooks.')
    elif sum(value == 'brook' for value in currentBoard.values()) > 2:
        print('You have too many black rooks.')
    elif sum(value == 'wbishop' for value in currentBoard.values()) > 2:
        print('You have too many white bishops.')
    elif sum(value == 'bbishop' for value in currentBoard.values()) > 2:
        print('You have too many black bishops.')
    elif sum(value == 'wknight' for value in currentBoard.values()) > 2:
        print('You have too many white knights.')
    elif sum(value == 'bknight' for value in currentBoard.values()) > 2:
        print('You have too many black knights.')
    # Running bishop check
    elif isBishopValid(board) == False:
        print('Bishops in invalid spaces.')
    else:
        print(True)


currentBoard = {'1a': 'bking', '6c': 'wqueen', '2g': 'bbishop',
                '5h':'bqueen', '3e': 'wking', '1b' : 'wpawn',
                 '1c' : 'wpawn', '5b' : 'bbishop', '8c' : 'wbishop',
                 '8e' : 'wbishop'}

#print(list(currentBoard.values()))
isValidChessBoard(currentBoard)