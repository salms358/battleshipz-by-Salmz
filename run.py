import random

# Set up game constants

NUMBER_SHIPS = 5
SHIP_SIZES = 3
board_sizes = {"1": 7, "2": 9, "3": 12}
comp_board = [['O' for x in range(10)] for y in range(10)]
player_board = [['O' for x in range(10)] for y in range(10)]
difficulties = ""
board_size = ""

# Should print out ASCII art as a welcome page


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

# If the user wants to see the rules incase its their first time or theyneed a reminder they can ask for the rules to be printed onto the console


def rules():
    """ method to show the rules """
    rulez = input("Do you want to see the rules? (y/n)")
    while rulez.lower() not in ["y", "n"]:
        print("invalid input")
        rulez = input("Do you want to see the rules? (y/n)")
    if rulez == "y":
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

    print("lets gooooooooooo")

# Set up game board


def set_diff():
    """setting difficulty"""
    print("Select your difficulty level")
    print("1. easy")
    print("2. medium")
    print("3. hard")
    global difficulties
    board_size = board_sizes.get(difficulties)
    difficulties = input("Enter desired difficulty")
    while difficulties not in ["1", "2", "3"]:
        print("Invalid input")
        difficulties = input("Enter desired difficulty")


def dual_boards():
    """
    This should lead to both board printing at the same time
    """
    board = []
    for i in range(board_size):
        row = ["O"] * board_size
        board.append(row)

    print(
        f"Board size: {board_size}x{board_size}")
    comp_board = []
    for i in range(board_size):
        row = ["O"] * board_size
        comp_board.append(row)


def print_board(board):
    """
    printing both boards together
    """
    print(player_board)
    print(comp_board)

    # return player_board, [], print_boards

# Place ships randomly


def ships():
    for i in range(NUMBER_SHIPS):
        ship_row = random.randint(0, board_size - 1)
        ship_col = random.randint(0, board_size - 1)

    # Ensure the ship does not overlap with another ship
        while player_board[ship_row][ship_col] == "S":
            ship_row = random.randint(0, board_size - 1)
            ship_col = random.randint(0, board_size - 1)

        # Place the ship
        for j in range(SHIP_SIZES):
            if ship_col + j < board_size:
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
    while num_hits < SHIP_SIZES * NUMBER_SHIPS and num_guesses and comp_hits < board_size ** 2:
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

        # print("Computer board: ")
        # computer_board()
        # row_comp = random.randint(0, board_sizes[difficulties]-1)
        # col_comp = random.randint(0, board_sizes[difficulties]-1)


def print_scores():
    if (row_comp, col_comp) in comp_ship_placement:
        print("The computer hit your ship!")
        board_size[row_comp][col_comp] = "X"
        num_hits -= 1
    else:
        print("The computer missed your ship lucky!")
        board_size[row_comp][col_comp] = "."
        comp_misses += 1

    # End the game
    # print("Game over!")
    for row in player_board:
        print(" ".join(row))

    print("Number of guesses:", num_guesses)
    print("Number of hits:", num_hits)


if __name__ == "__main__":
    while True:
        welcome()
        rules()
        set_diff()
        ships()
        game()
        break

    # this is my game loop, to exit it use the break statement Thanks for playing!
