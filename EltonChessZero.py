import random 


piece_value = { "K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "p": 1 }
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

"""
def findBestMove(gs, valid_moves):
    
    #Find the best move using the minimax algorithm.
    
    
    turn_multiplier = 1 if gs.white_to_move else -1
    opponent_min_max_score = CHECKMATE
    best_player_move = None
    random.shuffle(valid_moves)
    #print("Valid moves",  [move.getChessNotation() for move in valid_moves])
    for player_move in valid_moves:
        gs.makeMove(player_move)
        #print(gs.checkmate)
        opponent_moves = gs.getValidMoves()
        opponent_max_score = -CHECKMATE
        
        
        for opponent_move in opponent_moves:
            gs.makeMove(opponent_move)
            if gs.checkmate:
                score = -turn_multiplier *CHECKMATE
            elif gs.stalemate:
                score = STALEMATE
            else:
                score = - turn_multiplier * evaluateBoard(gs.board)
            if score > opponent_max_score:
                opponent_max_score = score
            gs.undoMove()
        
        if opponent_max_score < opponent_min_max_score:
            opponent_min_max_score = opponent_max_score
            best_player_move = player_move
        gs.undoMove()
    
    return best_player_move
    """

def findBestMove(gs, valid_moves):
    """
    Find the best move using the minimax algorithm.
    
    """
    global next_move,counter
    next_move = None
    random.shuffle(valid_moves)
    counter = 0
    findMoveNegaMaxAlphaBeta(gs, valid_moves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.white_to_move else -1)
    print(counter)
    return next_move

def findMoveMinMax(gs, valid_moves, depth, white_to_move):
    global next_move
    if depth == 0:
        return evaluateBoard(gs.board)
    
    if white_to_move:
        max_score = -CHECKMATE
        for move in valid_moves:
            gs.makeMove(move)
            next_moves = gs.getValidMoves()
            score = findMoveMinMax(gs, next_moves, depth - 1, False)
            if score > max_score:
                max_score = score
                if depth == DEPTH:
                    next_move = move
            gs.undoMove()
            return max_score
    else:
        min_score = CHECKMATE
        for move in valid_moves:
            gs.makeMove(move)
            next_moves = gs.getValidMoves()
            score = findMoveMinMax(gs, next_moves, depth - 1, True)
            if score < min_score:
                min_score = score
                if depth == DEPTH:
                    next_move = move
            gs.undoMove()
            return min_score
    

def findMoveNegaMax(gs, valid_moves, depth, turn):
    global next_move
    if depth == 0:
        #print(scoreBoard(gs))
        return turn * scoreBoard(gs)
    
    max_score = -CHECKMATE
    for move in valid_moves:
        gs.makeMove(move)
        next_moves = gs.getValidMoves()
        score = -findMoveNegaMax(gs, next_moves, depth - 1, -turn)
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move
        gs.undoMove()
    return max_score


def findMoveNegaMaxAlphaBeta(gs, valid_moves, depth,alpha,beta, turn):
    global next_move,counter
    counter += 1
    if depth == 0:
        #print(scoreBoard(gs))
        return turn * scoreBoard(gs)
    
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
    for row in gs.board:
        for square in row:
            if square != "--":
                if square[0] == 'w':
                    score += piece_value[square[1]] 
                elif square[0] == 'b':
                    score -= piece_value[square[1]] 
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
    for row in gs.board:
        for square in row:
            if square[0] == 'w':
                score += piece_value[square[1]]
            elif square[0] == 'b':
                score -= piece_value[square[1]]
    return score
    