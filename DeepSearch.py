def evaluateMaterial(gamestate):
    piece_value = { "K": 0, "Q": 10, "R": 5, "B": 3, "N": 3 }
    
    material_on_the_board = 0
    total_piece_value = 0
    move_count = len(gamestate.move_log)
    
    for row in gamestate.board:
        for square in row:
            if square != "--" and square[1] != "p":  # Ignore empty squares and pawns
                material_on_the_board += piece_value[square[1]]
                total_piece_value += piece_value[square[1]]
    
    # Determine the game time
    if move_count < 7 and total_piece_value > 22:
        game_time = "opening_theory"
    elif total_piece_value < 16:
        game_time = "end_game"
    elif move_count >= 14 or not any("Q" in square for row in gamestate.board for square in row):
        game_time = "middle_game"
    else:
        game_time = "opening_theory"
    
    return material_on_the_board, game_time