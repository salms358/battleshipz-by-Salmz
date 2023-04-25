    if empty_board[guess_row][guess_col] == "M" or \
                empty_board[guess_row][guess_col] == "S":
                print("you guessed the same coordinates mate")
            
            if player_board[guess_col][guess_row] == "M" or \
                player_board[guess_row][guess_col] == "H":
                print("Computer sort yourself out you guessed the same coordinates")