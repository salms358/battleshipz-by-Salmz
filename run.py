from random import randint

random_number = randint(0, 10)


# Should print out ASCII art as a welcome page
def welcome():
    """Ascii art of ship"""
    print(
        r"""
   __    __    __
                             |==|  |==|  |==|
                           __|__|__|__|__|__|_
                        __|___________________|___
                     __|__[]__[]__[]__[]__[]__[]__|___
                    |............................o.../
                    \.............................../
               hjw_,~')_,~')_,~')_,~')_,~')_,~')_,~')/,~')_
               """
    )
    print("Welcome to the battleships game! :)")


# If the user wants to see the rules incase its their first time or theyneed
# a reminder they can ask for the rules to be printed onto the console
def rules():
    """method to show the rules"""
    rulez = input("Do you want to see the rules? (y/n) ")
    while rulez.lower() not in ["y", "n"]:
        print("invalid input")
        rulez = input("Do you want to see the rules? (y/n) ")
    if rulez == "y":
        print()
        print("The goal of the game is to sink all of your opponent's ships")
        print("before they sink yours.")
        print("The ships are of different sizes and are placed")
        print("horizontally or vertically on the board.")
        print("Players take turns to guess the location of their opponent's")
        print("ships by calling out a coordinate (e.g.D7)")
        print("If the guess is a hit, the player marks that location on their")
        print("opponent's board with a marker to indicate a hit.")
        print("If the guess is a miss, the player marks that location with a ")
        print("marker to indicate a miss.")
        print("The game continues until all ships of one player have been sunk ")
        print("and the other player is declared the winner.")
        print()

    print("lets gooooooooooo!")
    print()


def set_diff():
    """setting difficulty"""
    print("Select your difficulty level")
    print("1. easy")
    print("2. medium")
    print("3. hard")
    difficulties = input("Enter desired difficulty: ")
    while difficulties not in ["1", "2", "3"]:
        print("Invalid input")
        difficulties = input("Enter desired difficulty: ")
    return difficulties


def dual_boards():
    """
    This should lead to both board printing at the same time
    """
    board = []
    for i in range(board_size):
        row = ["O"] * board_size
        board.append(row)

    print(f"Board size: {board_size}x{board_size}")
    comp_board = []
    for i in range(board_size):
        row = ["O"] * board_size
        comp_board.append(row)

    empty_board = []
    for i in range(board_size):
        row = ["O"] * board_size
        board.append(row)



def print_board(player_board, comp_board):
    """
    printing both boards together
    """
    print("Player board:")
    for row in player_board:
        print(" ".join(row))
    print()
    for row in empty_board:
        print(" ".join(row))  
    print()
#print(" ".join(["O" if val == "S" else val for val in row]))  
    #print("Computer board:")


def ships(board_size: int, player_board, comp_board):
    """
    Place ships randomly
    """
    for i in range (NUMBER_SHIPS):
        x = randint(0, board_size - 1)
        y = randint(0, board_size - 1)
        hidden_ships.append((x,y))
    for i in range(NUMBER_SHIPS):
        ship_row = randint(0, board_size - 1)
        ship_col = randint(0, board_size - 1)


        # Ensure the ship does not overlap with another ship
        while player_board[ship_row][ship_col] == "S":
            ship_row = randint(0, board_size - 1)
            ship_col = randint(0, board_size - 1)

        player_board[ship_row][ship_col] = "S"

    for i in range(NUMBER_SHIPS):
        ship_row = randint(0, board_size - 1)
        ship_col = randint(0, board_size - 1)

        # Ensure the ship does not overlap with another ship
        while player_board[ship_row][ship_col] == "S":
            ship_row = randint(0, board_size - 1)
            ship_col = randint(0, board_size - 1)

        comp_board[ship_row][ship_col] = "S"

    return player_board, comp_board


def game(board_size: int, player_board, comp_board, empty_board):
    """
    Gameplay loop method
    """
    # Play the game
    num_guesses = 20
    num_hits = 0
    comp_hits = 0
    comp_misses = 0
    comp_guess = 20
    
    while num_guesses > 0:
        # Print game boards
        print_board(player_board, empty_board)

        # Get user input
        try:
            guess_row = int(input("Guess row: "))
            guess_col = int(input("Guess col: "))
            if guess_row <= board_size and guess_row > 0:
                pass
            else:
                raise "Number is out of bounds"
            if guess_col <= board_size and guess_col > 0:
                pass
            else:
                raise "Number is out of bounds"
        except ValueError:
            print("Invalid input")
            continue
        if comp_board[guess_row][guess_col] == "S":
            print("Hit!")
            


            print(num_guesses)
            #for val in row:
                #if val == "S" and not revealed:
                   # print("S", end=" ")
                   # revealed = True
                #else:
                    
            empty_board[guess_row][guess_col] = "S"
            num_hits += 1
            if num_hits == 5:
                print("You won")
                break
            row = randint(0, len(player_board) - 1)
            col = randint(0, len(player_board) - 1)

            if player_board[row][col] == "S":
                print("The computer hit your ship at row", row, "column", col, "!")
                player_board[row][col] = "H"
                comp_hits += 1
                if comp_hits == 5:
                    print("computer won")
                    break
            else:
                print("The computer missed at row", row, "column", col, ".")
                player_board[row][col] = "M"
        else:
            print("Miss!")
            empty_board[guess_row][guess_col] = "M"
            num_guesses -= 1
            print(f"Guesses remaining:",{num_guesses})
            if num_guesses == 0:
                print("too many incorrect guesses game over")
                break
           
            row = randint(0, len(player_board) -1)
            col = randint(0, len(player_board) - 1)


            if player_board[row][col] == "S":
                print("The computer hit your ship at row", row, "column", col, "!")
                player_board[row][col] = "H"
                comp_hits += 1
            else:
                print("The computer missed at row", row, "column", col, ".")
                player_board[row][col] = "M"
                comp_guess -= 1
                print(f"Guesses remaining Computer:",{num_guesses})
                if comp_guess == 0:
                    print("Computer has too many incorrect guesses game over")
                    break
                
        


def print_scores():
    """
    Method to print user score
    """
    if (row_comp, col_comp) in comp_ship_placement:
        print("The computer hit your ship!")
        board_size[row_comp][col_comp] = "X"
        num_hits -= 1
    else:
        print("The computer missed your ship lucky!")
        board_size[row_comp][col_comp] = "."
        comp_misses += 1

    # End the game



if __name__ == "__main__":
    # Set up game constants
    NUMBER_SHIPS = 5
    SHIP_SIZES = 3
    board_sizes = {"1": 7, "2": 9, "3": 12}
    board_size = 1
    comp_ships = []
    player_ships = []
    num_guesses = 5
    hidden_ships = []
    while True:
        welcome()
        rules()
        difficulties = set_diff()
        board_size = board_sizes[difficulties]
        # hidden_comp_board = 
        comp_board = [["O" for x in range(board_size)] for y in range(board_size)]
        empty_board = [["O" for x in range(board_size)] for y in range(board_size)]
        player_board = [["O" for x in range(board_size)] for y in range(board_size)]
        player_board, comp_board = ships(board_size, player_board, comp_board)
        game(board_size, comp_board, player_board, empty_board)
        break













