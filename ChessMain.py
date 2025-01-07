import pygame as p

import ChessEngine, EltonChessZero

BOARD_WIDTH = BOARD_HEIGHT = 512
MOVE_LOG_PANEL_WIDTH = 250
MOVE_LOG_PANEL_HEIGHT = BOARD_HEIGHT
DIMENSION = 8
SQUARE_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages ():
    """
    Initialize a global directory of images.
    This will be called exactly once in the main.
    """
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

#handles user input and graphics
def main():
    p.init()
    screen = p.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    game_state = ChessEngine.GameState()
    valid_moves = game_state.getValidMoves()
    move_made = False
    global animate 
    animate = False
    # print(game_state.board)
    loadImages()
    running = True
    square_selected = ()  # no square is selected initially, this will keep track of the last click of the user (tuple(row,col))
    player_clicks = []  # this will keep track of player clicks (two tuples)
    game_over = False
    #ai_thinking = False
    #move_undone = False
    playerOne = True  # if a human is playing white, then this will be True, if an AI is playing then this will be False
    playerTwo = False  # if a human is playing black, then this will be True, if an AI is playing then this will be False
    
    while running:
        human_turn = (game_state.white_to_move and playerOne) or (not game_state.white_to_move and playerTwo)
        for e in p.event.get():
            if not game_over:
                if e.type == p.QUIT:
                    running = False
                # mouse handler
                elif e.type == p.MOUSEBUTTONDOWN:
                    if not game_over and human_turn:
                        location = p.mouse.get_pos()  # (x, y) location of the mouse
                        col = location[0] // SQUARE_SIZE
                        row = location[1] // SQUARE_SIZE
                        if square_selected == (row, col) or col >= 8:  # user clicked the same square twice
                            square_selected = ()  # deselect
                            player_clicks = []  # clear clicks
                        else:
                            square_selected = (row, col)
                            player_clicks.append(square_selected)  # append for both 1st and 2nd click

                        # Ensure player_clicks has exactly two elements before creating a Move object
                        if len(player_clicks) == 2:
                            try:
                                move = ChessEngine.Move(player_clicks[0], player_clicks[1], game_state.board)
                                for i in range(len(valid_moves)):
                                    if move == valid_moves[i]:
                                        game_state.makeMove(valid_moves[i])
                                        move_made = True
                                        animate = True
                                        print(move.getChessNotation())  # Print the chess notation of the move
                                        square_selected = ()  # reset user clicks
                                        player_clicks = []
                                        break
                                if not move_made:
                                    player_clicks = [square_selected]
                            except IndexError:
                                # Reset state in case of an error
                                print("Invalid move: Resetting selection.")
                                square_selected = ()
                                player_clicks = []
                        else:
                            player_clicks = [square_selected]

                # key handlers
                elif e.type == p.KEYDOWN:
                    if e.key == p.K_z and len(game_state.move_log) != 1:  # undo when 'z' is pressed
                        game_state.undoMove()
                        move_made = True
                        animate = False
                    if e.key == p.K_r:  # reset the game when 'r' is pressed
                        game_state = ChessEngine.GameState()
                        valid_moves = game_state.getValidMoves()
                        square_selected = ()
                        player_clicks = []
                        move_made = False
                        animate = False
                        game_over = False
        
        #AI move finder logic
        if not game_over and not human_turn:
            AIMove = EltonChessZero.findBestMoveMinMax(game_state, valid_moves)
            if AIMove is None:
                AIMove = EltonChessZero.findRandomMove(valid_moves)
            game_state.makeMove(AIMove)
            move_made = True
            animate = True
            
            
        if move_made:
            if animate:
                animateMove(game_state.move_log[-1], screen, game_state.board, clock)
            valid_moves = game_state.getValidMoves()
            move_made = False
               
        drawGameState(screen,game_state ,valid_moves, square_selected)
        
        if game_state.checkmate or game_state.stalemate:
            game_over = True
            font = p.font.SysFont(None, 32)
            if game_state.stalemate:
                text = 'Stalemate'
            elif game_state.white_to_move:
                text = 'Black wins by checkmate'
            else:
                text = 'White wins by checkmate'
            text = font.render(text, True, p.Color('black'), p.Color('white'))
            text_rect = text.get_rect(center=(BOARD_WIDTH // 2, BOARD_HEIGHT // 2))
            screen.blit(text, text_rect)
        clock.tick(MAX_FPS)
        p.display.flip()
    
# responsible for all graphics
def drawGameState(screen,game_state, valid_moves, square_selected):
    drawBoard(screen) # draw squares
    #responsible mainly for drawing pieces  on the board 
    highlightSquares(screen, game_state, valid_moves, square_selected)
    drawPieces(screen,game_state.board)# highlingthing moves later on 

def highlightSquares(screen, game_state, valid_moves, square_selected):
    """
    Highlight square selected and moves for piece selected.
    """
    if (len(game_state.move_log)) > 0:
        last_move = game_state.move_log[-1]
        s = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
        s.set_alpha(100)
        s.fill(p.Color('green'))
        screen.blit(s, (last_move.end_col * SQUARE_SIZE, last_move.end_row * SQUARE_SIZE))
    if square_selected != ():
        row, col = square_selected
        if game_state.board[row][col][0] == (
                'w' if game_state.white_to_move else 'b'):  # square_selected is a piece that can be moved
            # highlight selected square
            s = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
            s.set_alpha(100)  # transparency value 0 -> transparent, 255 -> opaque
            s.fill(p.Color('blue'))
            screen.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            # highlight moves from that square
            s.fill(p.Color('yellow'))
            for move in valid_moves:
                if move.start_row == row and move.start_col == col:
                    screen.blit(s, (move.end_col * SQUARE_SIZE, move.end_row * SQUARE_SIZE))


def drawBoard(screen):
    global colors
    colors = [p.Color(222, 184, 135), p.Color(139, 69, 19)]
    
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c) % 2]
            p.draw.rect(screen,color,p.Rect(c*SQUARE_SIZE , r*SQUARE_SIZE ,SQUARE_SIZE , SQUARE_SIZE))
            
            
def drawPieces(screen,board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def animateMove(move, screen, board, clock):
    """
    Animates a move.
    """
    global colors
    dR = move.end_row - move.start_row
    dC = move.end_col - move.start_col
    frames_per_square = 10  # frames to move one square
    frame_count = (abs(dR) + abs(dC)) * frames_per_square
    for frame in range(frame_count + 1):
        r, c = (move.start_row + dR * frame / frame_count, move.start_col + dC * frame / frame_count)
        drawBoard(screen)
        drawPieces(screen, board)
        # erase the piece moved from its ending square
        color = colors[(move.end_row + move.end_col) % 2]
        end_square = p.Rect(move.end_col * SQUARE_SIZE, move.end_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        p.draw.rect(screen, color, end_square)
        # draw the captured piece back onto the board
        if move.piece_captured != '--':
            screen.blit(IMAGES[move.piece_captured], end_square)
        # draw the moving piece
        if move.piece_moved != '--':  # Add this check to skip empty squares
            screen.blit(IMAGES[move.piece_moved], p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        p.display.flip()
        clock.tick(60)

if __name__ == "__main__":    
    main()