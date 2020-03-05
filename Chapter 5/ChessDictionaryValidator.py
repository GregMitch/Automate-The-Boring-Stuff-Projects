def is_valid_chess_board(chessBoard):

    tiles = ('1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h', # Tuple of valid chess board positions.
             '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h',
             '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h',
             '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h',
             '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h',
             '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',
             '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h',
             '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h')

    characters = ('bishop', 'king', 'knight', 'pawn', 'queen', 'rook') # Tuple of valid chess pieces, used tuples as they are faster then lists.

    # Following 12 variables are for keeping track of each colours piece counts. Probably more efficient way of storing this info.
    wking = 0
    wqueen = 0
    wbishop = 0
    wrook = 0
    wknight = 0
    wpawn = 0
    
    bking = 0
    bqueen = 0
    bbishop = 0
    brook = 0
    bknight = 0
    bpawn = 0
    
    for position in chessBoard.keys(): #Checks every key to make sure it is a valid position on the board.
        #print(position) Testing purposes
        if position not in tiles:
            print('Following position does not exist on our chess board: ' + position)
            return(False)

    for pieces in chessBoard.values(): #Checks every value to make sure it is a valid Chess piece and increments its respective variable if it's valid
        #print(pieces[0]) Testing purposes
        if(pieces[0] != 'b' and pieces[0] != 'w'): #Checks piece colour
            print('Following colour does not exist in our chest board: ' + pieces[0])
            return(False)

        if(pieces[1:] not in characters): # Checks piece name  
            print('Following piece does not exist in our chest board: ' + pieces[1:])
            return(False)
  
        if(pieces == 'wking'):
            wking += 1

        elif(pieces == 'bking'):
            bking += 1

        elif(pieces == 'wqueen'):
            wqueen += 1

        elif(pieces == 'bqueen'):
            bqueen += 1

        elif(pieces == 'wknight'):
            wknight += 1

        elif(pieces == 'bknight'):
            bknight += 1

        elif(pieces == 'wrook'):
            wrook += 1

        elif(pieces == 'brook'):
            brook += 1

        elif(pieces == 'wbishop'):
            wbishop += 1

        elif(pieces == 'bbishop'):
            bbishop += 1

        elif(pieces == 'wpawn'):
            wpawn += 1

        elif(pieces == 'bpawn'):
            bpawn += 1

    if(wking != 1 or bking != 1): #Checks for 1 king of both colours
        #print(wking, bking) Testing purposes
        print('There is not exactly one black or exactly one white king on the board')
        return(False)

    if(wqueen > 1 or bqueen > 1 or wpawn > 8 or bpawn > 8 or wbishop > 2 or bbishop > 2 or wknight > 2 or bknight > 2 or wrook > 2 or brook > 2): #Checks to make sure there isnt too many of the other 5 pieces
        print('There are too many pieces of one type on the board')
        return(False)

    return(True)
