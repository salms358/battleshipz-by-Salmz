import random

# Set up game constants

NUMBER_SHIPS = 5
SHIP_SIZES = 3
easy_mode = 1
medium_mode = 2
hard_mode = 3
board_sizes = {"1": 7, "2": 9, "3": 12}
comp_board = [['O' for x in range(10)] for y in range(10)]
player_board = [['O' for x in range(10)] for y in range(10)]
boatsz = {"Destroyer": 2, "Cruiser": 3, "Battleship": 4, "Aircraft Carrier": 5}
difficulties = ""


def welcome():
    """Ascii art of ship"""
    print(r"""
   __    __    __
                             |==|  |==|  |==|
                           __|__|__|__|__|__|_
                        __|___________________|___
                     __|__[]__[]__[]__[]__[]__[]__|___
                    |............................o.../
                    \.............................../
               hjw_,~')_,~')_,~')_,~')_,~')_,~')_,~')/,~')_
               """)
    print("Welcome! :)")


def rules():
    """ method to show the rules """
    rulez = input("Do you want to see the rules? (y/n)")
    while rulez.lower() not in ["y","n"]:
        print("invalid input")
        rulez = input("Do you want to see the rules? (y/n)")

    if rulez == "y":
        print("The goal of the game is to sink all of your opponent's ships before they sink yours.")

        print("The ships are of different sizes and are placed horizontally or vertically on the board.")

        print("Players take turns to guess the location of their opponent's ships by calling out a coordinate (e.g.D7)")

        print("If the guess is a hit, the player marks that location on their opponent's board with a marker to indicate a hit.")

        print("If the guess is a miss, the player marks that location with a marker to indicate a miss.")

        print("The game continues until all ships of one player have been sunk, and the other player is declared the winner.")

    print("lets gooooooooooo")

# Set up game board


def set_diff():
    """setting difficulty"""
    print("Select your difficulty level")
    print("1. easy")
    print("2. medium")
    print("3. hard")
    global difficulties
    difficulties = input("Enter desired difficulty")
    while difficulties not in ["1" , "2" , "3"]:
        print("Invalid input")
        difficulties = input("Enter desired difficulty")
        
        #set_diff()
        #player_board = dual_boards()
        #comp_board = dual_boards()
        #print_boards(player_board, comp_board)


def dual_boards():
    """
    This should lead to both board printing at the same time
    """
    board = []
    for i in range(board_sizes[difficulties]):
        row = ["O"] * board_sizes[difficulties]
        board.append(row)

def print_board(board):
    print(player_board)
    print(comp_board)
        
    print(f"Board size: {board_sizes[difficulties]}x{board_sizes[difficulties]}")

    comp_board = []
    for i in range(board_sizes[difficulties]):
        row = ["O"] * board_sizes[difficulties]
        comp_board.append(row)
        
    

    #return player_board, [], print_boards

# Place ships randomly


def ships():
    for i in range(NUMBER_SHIPS):
        ship_row = random.randint(0, board_sizes[difficulties] - 1)
        ship_col = random.randint(0, board_sizes[difficulties] - 1)

    # Ensure the ship does not overlap with another ship
        while player_board[ship_row][ship_col] == "S":
            ship_row = random.randint(0, board_sizes[difficulties] - 1)
            ship_col = random.randint(0, board_sizes[difficulties] - 1)

        # Place the ship
        for j in range(SHIP_SIZES):
            if ship_col + j < board_sizes[difficulties]:
                player_board[ship_row][ship_col + j] = "S"
            else:
                comp_board[ship_row] = + 1
    comp_ship_placement = []
    for i in range(SHIP_SIZES):
        row = random.randint(0, SHIP_SIZES - 1)
        col = random.randint(0, SHIP_SIZES - 1)
        comp_ship_placement.append((row, col))


def game():
    """gameplay"""

    # Play the game
    num_guesses = 0
    num_hits = 0
    comp_hits = 0
    comp_misses = 0
    comp_score = 0
    user_score = 0
    while num_hits < SHIP_SIZES * NUMBER_SHIPS and num_guesses and comp_hits < board_sizes[difficulties] ** 2:
        # Print the game board
        for row in player_board:
            print(" ".join(row))

        # Get user input
        guess_row = int(input("Guess row: "))
        guess_col = int(input("Guess col: "))

        # Check if the guess is a hit or a miss
        if board_sizes[guess_row][guess_col] == "S":
            print("Hit!")
            board_sizes[guess_row][guess_col] = "X"
            num_hits += 1
        else:
            print("Miss!")
            board_sizes[guess_row][guess_col] = "X"

        num_guesses += 1

        #print("Computer board: ")
        #computer_board()
        row_comp = random.randint(0, board_sizes[difficulties]-1)
        col_comp = random.randint(0, board_sizes[difficulties]-1)
        def print_scores():
            if (row_comp, col_comp) in comp_ship_placement:
                print("The computer hit your ship!")
                board[row_comp][col_comp] = "X"
                num_hits -= 1
            else:
                print("The computer missed your ship lucky!")
                board[row_comp][col_comp] = "."
                comp_misses += 1



    # End the game
    print("Game over!")
    for row in player_board:
        print(" ".join(row))

    print("Number of guesses:", num_guesses)
    print("Number of hits:", num_hits)


if __name__ == "__main__":
    while True:
        welcome()
        rules()
        set_diff()
        #ships()
        game()
        break 
    
    #this is my game loop, to exit it use the break statement Thanks for playing!