import random


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


def print_board(player_board, comp_board):
    """
    printing both boards together
    """
    print("Player board:")
    for row in player_board:
        print(" ".join(row))
    print()

    print("Computer board:")
    for row in comp_board:
        print(" ".join(row))
    print()


def ships(board_size: int, player_board, comp_board):
    """
    Place ships randomly
    """
    for i in range(NUMBER_SHIPS):
        ship_row = random.randint(0, board_size - 1)
        ship_col = random.randint(0, board_size - 1)

        # Ensure the ship does not overlap with another ship
        while player_board[ship_row][ship_col] == "S":
            ship_row = random.randint(0, board_size - 1)
            ship_col = random.randint(0, board_size - 1)

        player_board[ship_row][ship_col] = "S"

    for i in range(NUMBER_SHIPS):
        ship_row = random.randint(0, board_size - 1)
        ship_col = random.randint(0, board_size - 1)

        # Ensure the ship does not overlap with another ship
        while player_board[ship_row][ship_col] == "S":
            ship_row = random.randint(0, board_size - 1)
            ship_col = random.randint(0, board_size - 1)

        comp_board[ship_row][ship_col] = "S"

    return player_board, comp_board


def game(board_size: int, comp_board, player_board):
    """
    Gameplay loop method
    """
    # Play the game
    num_guesses = 8
    num_hits = 0
    comp_hits = 0
    comp_misses = 0
    # while num_hits < SHIP_SIZES * NUMBER_SHIPS and num_guesses and comp_hits < board_size ** 2:
    while num_guesses > 0:
        # Print game boards
        print_board(player_board, comp_board)

        # Get user input
        try:
            guess_row = int(input("Guess row: "))
            guess_col = int(input("Guess col: "))
            if guess_row <= board_size and guess_row > 0:
                # Do nothing
                pass
            else:
                raise "Number is out of bounds"
            if guess_col <= board_size and guess_col > 0:
                # Do nothing
                pass
            else:
                raise "Number is out of bounds"
        except ValueError:
            print("Invalid input")
            continue

        guess_row = guess_row - 1
        guess_col = guess_col - 1

        # Check if the guess is a hit or a miss
        if comp_board[guess_row][guess_col] == "S":
            print("Hit!")
            comp_board[guess_row][guess_col] = "X"
            num_hits += 1
        else:
            print("Miss!")
            comp_board[guess_row][guess_col] = "M"

        num_guesses -= 1

        # print("Computer board: ")
        # computer_board()
        # row_comp = random.randint(0, board_sizes[difficulties]-1)
        # col_comp = random.randint(0, board_sizes[difficulties]-1)

        comp_row = random.randint(0, board_size - 1)
        comp_col = random.randint(0, board_size - 1)


# Make sure the guess hasn't already been made
    while player_board[comp_row][comp_col] != " ":
        comp_row = random.randint(0, board_size - 1)
        comp_col = random.randint(0, board_size - 1)
        # computers turn
        if player_board[comp_row][comp_col] == "S":
            print("Computer hit your ship")
            player_board[comp_row][comp_col] == "X"
            num_hits -= 1
        else:
            print("computer misses your ships haha")
            player_board[comp_row][comp_col] = "M"


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
    print("Game over!")
    for row in player_board:
        print(" ".join(row))

    print("Number of guesses:", num_guesses)
    print("Number of hits:", num_hits)


if __name__ == "__main__":
    # Set up game constants
    NUMBER_SHIPS = 5
    SHIP_SIZES = 3
    board_sizes = {"1": 7, "2": 9, "3": 12}
    board_size = 0
    while True:
        welcome()
        rules()
        difficulties = set_diff()

        board_size = board_sizes[difficulties]
        comp_board = [["O" for x in range(board_size)] for y in range(board_size)]
        player_board = [["O" for x in range(board_size)] for y in range(board_size)]
        player_board, comp_board = ships(board_size, player_board, comp_board)

        game(board_size, comp_board)
        break
