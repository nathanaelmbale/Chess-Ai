import random 



piece_value = { "K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "p": 1 }

piece_position_values = {
        "N": [
            [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
            [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
            [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
            [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
            [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
            [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
            [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
            [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]
        ],
        "B": [
            [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
            [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
            [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
            [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
            [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
            [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
            [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
            [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]
        ],
        "R": [
            [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
            [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
            [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
            [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
            [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
            [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
            [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
            [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]
        ],
        "Q": [
            [0.0, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.0],
            [0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.3, 0.3, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.3, 0.3, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.3, 0.3, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.3, 0.3, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.1],
            [0.0, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.0]
        ],
        "K": [
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ],
        "p": [
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
            [0.15, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, 0.15],
            [0.2, 0.05, 0.1, 0.25, 0.25, 0.1, 0.05, 0.2],
            [0.2, 0.0, 0.0, 0.2, 0.2, 0.0, 0.0, 0.2],
            [0.15, -0.05, -0.1, 0.0, 0.0, -0.1, -0.05, 0.15],
            [0.05, 0.1, 0.1, -0.2, -0.2, 0.1, 0.1, 0.05],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ]
    }

CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3
#positional advantage
# - pin to the king or a piece is good

def findRandomMove(valid_moves):
    """
    Picks and returns a random valid move.
    """
    print("Valid moves",  [move.getChessNotation() for move in valid_moves])
    return valid_moves[random.randint(0, len(valid_moves) - 1)]


def findBestMove(gs, valid_moves):
    """
    Find the best move using the minimax algorithm.
    
    """
    global next_move,counter
    next_move = None
    random.shuffle(valid_moves)
    counter = 0
    findMoveNegaMaxAlphaBeta(gs, valid_moves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.white_to_move else -1)
    print("Moves gone through" ,counter)
    return next_move



def findMoveNegaMaxAlphaBeta(gs, valid_moves, depth,alpha,beta, turn):
    global next_move,counter
    counter += 1
    if depth == 0:
        #score = scoreBoard(gs)
        return turn * evaluateBoard(gs)
    
    #move ordering - implement later
    max_score = -CHECKMATE
    for move in valid_moves:
        gs.makeMove(move)
        next_moves = gs.getValidMoves()
        score = -findMoveNegaMaxAlphaBeta(gs, next_moves, depth - 1, -beta, -alpha, -turn)
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move
                print(score, " ",next_move)
        gs.undoMove()
        if max_score > alpha: #prunning
            alpha = max_score
        if alpha >= beta:
            break
    return max_score

def evaluateBoard(gs):
    """
    Evaluate the board and return a score.
    """
    if gs.checkmate:
        if gs.white_to_move:
            return -CHECKMATE  # black wins
        else:
            return CHECKMATE  # white wins
    elif gs.stalemate:
        return STALEMATE

    score = 0
    piece_value = {"K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "p": 1}
    piece_position_values = {
        "N": [
            [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
            [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
            [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
            [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
            [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
            [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
            [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
            [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]
        ],
        "B": [
            [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
            [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
            [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
            [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
            [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
            [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
            [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
            [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]
        ],
        "R": [
            [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
            [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
            [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
            [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
            [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
            [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
            [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
            [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]
        ],
        "Q": [
            [0.0, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.0],
            [0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.3, 0.3, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.3, 0.3, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.3, 0.3, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.3, 0.3, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.1],
            [0.0, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.0]
        ],
        "K": [
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ],
        "p": [
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
            [0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, 0.1],
            [0.05, 0.05, 0.1, 0.25, 0.25, 0.1, 0.05, 0.05],
            [0.0, 0.0, 0.0, 0.2, 0.2, 0.0, 0.0, 0.0],
            [0.05, -0.05, -0.1, 0.0, 0.0, -0.1, -0.05, 0.05],
            [0.05, 0.1, 0.1, -0.2, -0.2, 0.1, 0.1, 0.05],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ]
    }

    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):
            piece = gs.board[row][col]
            if piece != "--":
                piece_position_value = piece_position_values.get(piece[1], [[0]*8]*8)[row][col]
                if piece[0] == 'w':
                    score += piece_value[piece[1]] + piece_position_value
                elif piece[0] == 'b':
                    score -= piece_value[piece[1]] + piece_position_value
    return score

def scoreBoard(gs):
    if gs.checkmate:
        if gs.white_to_move:
            return -CHECKMATE
        else:
            return CHECKMATE
    elif gs.stalemate:
        return STALEMATE
    
    score = 0
    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):
            square = gs.board[row][col]
            
            #Openninng - Score for opening
            openningScore = 0
            # Moving new pieces is good every move
            #print("Here " + square)
            # controlling the center with pawns is good
            # moving the queen early is bad
            # moving the same piece multiple times is bad
            # castling is good
            
            #Middle game - Score for middle game
            middleGameScore = 0
            # controlling the center is good
            
            #End game - Score for end game
            endGameScore = 0
            # king safety is important
            # pawn promotion is good
            # king activity is good
            
            if col == "--":
                if col[0] == 'w':
                    score += piece_value[col[1]]
                elif square[0] == 'b':
                    score -= piece_value[square[1]]
        
    
    return score
    