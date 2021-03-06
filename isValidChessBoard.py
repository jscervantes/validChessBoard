# isValidChessBoard() is a program written in Python3 that takes a dicitonary argument
# and returns True or False depending on if the board is valid.


################ Checker Functions ##################

def isBishopValid(board):
    """Checks if either bishop is in wrong color square"""

    answer = ""

    blackSquares = []
    for j in 'aceg':
        for i in range(1, 9, 2):
            blackSquares.append(j + str(i))
    for j in 'bdfh':
        for i in range(2, 9, 2):
            blackSquares.append(j + str(i))

    whiteSquares = []
    for j in 'aceg':
        for i in range(2, 9, 2):
            whiteSquares.append(j + str(i))
    for j in 'bdfh':
        for i in range(1, 9, 2):
            whiteSquares.append(j + str(i))

    wBishop_WSquare = 0
    wBishop_BSquare = 0  
    bBishop_WSquare = 0
    bBishop_BSquare = 0                 
    for k, v in board:
        if v == 'wbishop' and k in whiteSquares:
            wBishop_WSquare += 1
        elif v == 'wbishop' and k in blackSquares:
            wBishop_BSquare += 1
        elif v == 'bbishop' and k in whiteSquares:
            bBishop_WSquare += 1
        elif v == 'bbishop' and k in blackSquares:
            bBishop_BSquare += 1

    if wBishop_WSquare > 1 or wBishop_BSquare > 1 or bBishop_WSquare > 1 or bBishop_BSquare > 1:
        answer = "Bishop(s) are in invalid space(s)."
    else:
        answer = "Bishops are in valid spaces."

    return answer


def isValidSpace(board):
    """Checks if spaces on board are real."""
    validSpaces = []
    answer = ""
    for j in 'abcdefgh':
        for i in range(1, 9):
            validSpaces.append(j + str(i))
    for space in list(board.keys()):
        if space not in validSpaces:
            answer = "The spaces given are invalid."
        else:
            answer = "Spaces valid."

    return answer


def isValidPieces(pieces):    
    """Checks if pieces on board are real"""
    validPieces = ('wking', 'bking', 'wqueen', 'bqueen', 'wrook', 'brook', 
            'wbishop', 'bbishop', 'wknight', 'bknight', 'wpawn', 'bpawn')
    answer = ""
    for piece in pieces:
        if piece not in validPieces:
            answer = "There is/are invalid piece(s)."
            break
        else:
            answer = "Pieces are valid."

    return answer


def kingCounter(pieces):
    """Checks both kings are still on the board."""
    answer = ""

    if sum(king == 'wking' for king in pieces) > 1:
        answer = 'You have an extra white king.'
    elif sum(king == 'bking' for king in pieces) > 1:
        answer = 'You have an extra black king.'
    elif 'bking' not in pieces:
        answer = "You are missing a black king."
    elif 'wking' not in pieces:
        answer = "You are missing a white king."
        if 'bking' not in pieces:
            answer = "You are missing both kings."
    else:
        answer = "Both kings present."

    return answer


def totalPieceCounter(pieces):
    answer = ""
    if len(pieces) > 32:
        answer = "You have too many pieces!"
    else:
        answer = "Number of pieces valid."

    return answer


def pawnCounter(pieces):
    answer = ""
    if sum(pawn == 'wpawn' for pawn in pieces) > 8:
        answer = "You have too many white pawns."
    elif sum(pawn == 'bpawn' for pawn in pieces) > 8:
        answer = "You have too many black pawns."
    else:
        answer = "Pawn count valid."

    return answer


def queenCounter(pieces):
    answer = ""
    if sum(queen == 'wqueen' for queen in pieces) > 1:
        answer = 'You have an extra white queen.'
    elif sum(queen == 'bqueen' for queen in pieces) > 1:
        answer = 'You have an extra black queen.'
    else:
        answer = "Queen count valid."

    return answer


def rookCounter(pieces):
    answer = ""
    if sum(rook == 'wrook' for rook in pieces) > 2:
        answer = 'You have too many white rooks.'
    elif sum(rook == 'brook' for rook in pieces) > 2:
        answer = 'You have too many black rooks.'
    else:
        answer = "Rook count valid."

    return answer
        

def bishopCounter(pieces):
    answer = ""
    if sum(bishop == 'wbishop' for bishop in pieces) > 2:
        answer = 'You have too many white bishops.'
    elif sum(bishop == 'bbishop' for bishop in pieces) > 2:
        answer = 'You have too many black bishops.'
    else:
        answer = 'Bishop count valid.'
        
    return answer


def knightCounter(pieces):
    answer = ""
    if sum(knight == 'wknight' for knight in pieces) > 2:
        answer = 'You have too many white knights.'
    elif sum(knight == 'bknight' for knight in pieces) > 2:
        answer = 'You have too many black knights.'
    else:
        answer = 'Knight count is valid.'

    return answer


############### Main function ###################

def main():
    board = {'1a': 'bking', '6c': 'wqueen', '2g': 'bbishop',
            '5h':'bqueen', '3e': 'wking', '1b' : 'wpawn',
            '1c' : 'wpawn', '5b' : 'bbishop', '8c' : 'wbishop',
            '8e' : 'wbishop', '8b' : 'wknight'}

    pieces = list(board.values())

    print(kingCounter(pieces))
    print(totalPieceCounter(pieces))
    print(isValidSpace(board))
    print(isValidPieces(pieces))
    print(isBishopValid(board))
    print(pawnCounter(pieces))
    print(queenCounter(pieces))
    print(rookCounter(pieces))
    print(bishopCounter(pieces))
    print(knightCounter(pieces))



if __name__ == "__main__":
    main()
