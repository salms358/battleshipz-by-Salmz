from random import randint


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

# The rules are shown and validation present
# The validation used was taken from the code i linked


def rules():
    """Method to show the rules"""
    rulez = input("Do you want to see the rules? (y/n) ")
    while rulez.lower() not in ["y", "n"]:
        print("Invalid input")
        rulez = input("Do you want to see the rules? (y/n) ")
    if rulez == "y":
        print()
        print("The goal of the game is to sink all of your opponent's ships")
        print("before they sink yours.")
        print("The ships are of different sizes and are placed")
        print("horizontally or vertically on the board.")
        print("Players take turns to guess the location of their opponent's")
        print("ships by calling out a coordinate (e.g. D7)")
        print("If the guess is a hit, the player marks that location on their")
        print("opponent's board with a marker to indicate a hit.")
        print("If the guess is a miss, the player marks that location with a")
        print("marker to indicate a miss.")
        print("All of opponents ships must be sunk")
        print("Whoever sinks all ships first wins")
        print()
    print("Let's gooooooooooo!")
    print()

# Allows the user to choose the difficulty


def set_difficulty():
    """Setting difficulty"""
    print("Select your difficulty level")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulties = input("Enter desired difficulty: ")
    while difficulties not in ["1", "2", "3"]:
        print("Invalid input")
        difficulties = input("Enter desired difficulty: ")
    return difficulties


def dual_boards(board_size):
    """
    This should lead to both board printing at the same time
    """
    player_board = [
        ["O" for _ in range(board_size)] for _ in range(board_size)]
    comp_board = [["O" for _ in range(board_size)] for _ in range(board_size)]
    empty_board = [["O" for _ in range(board_size)] for _ in range(board_size)]
    return player_board, comp_board, empty_board

# Prints both boards together


def print_board(player_board, empty_board):
    """
    Printing both boards together
    """
    print("Player board:")
    for row in player_board:
        print(" ".join(row))
    print()
    print("Computer board:")
    for row in empty_board:
        print(" ".join(row))
    print()

# Allows the ships to be randomly placed on the boards


def ships(board_size: int, player_board, comp_board):
    """
    Place ships randomly
    """
    for i in range(NUMBER_SHIPS):
        x = randint(0, board_size - 1)
        y = randint(0, board_size - 1)
        comp_board.append((x, y))
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
    for i in range(NUMBER_SHIPS):
        ship_row = randint(0, board_size - 1)
        ship_col = randint(0, board_size - 1)

    return player_board, comp_board


def computer_guess(player_board, comp_guess):
    global board_size
    while True:
        guess_row = randint(0, board_size - 1)
        guess_col = randint(0, board_size - 1)
        # See if the computer guessed these positions before,
        # if not then it can try out these positions
        if [guess_row, guess_col] not in comp_guess:
            break
    comp_guess.append([guess_row, guess_col])

# The game loop allowing the user to play the game


def game(board_size: int, player_board, comp_board, empty_board):
    """
    Gameplay loop method
    """
    # Play the game
    num_guesses = 24
    num_hits = 0
    comp_hits = 0
    comp_guess = 24

    while num_guesses > 0:
        # Print game boards
        print_board(player_board, empty_board)
        # Get user input
        try:
            guess_row = int(input("Guess row: ")) - 1
            guess_col = int(input("Guess col: ")) - 1
        except ValueError:
            print("Invalid input please enter an integer")
            continue

        if guess_row < 0 or guess_row >= board_size or \
                guess_col < 0 or guess_col >= board_size:
            print("Invalid coordinate. Please enter a valid coordinate.")
            continue
        # Users turn
        if empty_board[guess_row][guess_col] == "M" or \
                empty_board[guess_row][guess_col] == "S":
            print("You guessed the same coordinates before.")
            continue

        # Check if user hits a ship
        if comp_board[guess_row][guess_col] == "S":
            if empty_board[guess_row][guess_col] == "H" or \
                    empty_board[guess_row][guess_col] == "M":
                print("You've already hit that location.")
            else:
                print("Hit!")
                empty_board[guess_row][guess_col] = "H"
                num_hits += 1
                print("Player score:", num_hits)
        else:
            # If user misses a ship
            empty_board[guess_row][guess_col] = "M"
            print("Miss!")
            num_guesses -= 1
            print("Guesses remaining:", num_guesses)

        # Computer's turn
        comp_row = randint(0, board_size - 1)
        comp_col = randint(0, board_size - 1)

        if player_board[comp_row][comp_col] == "S":
            print("The computer hit your ship at row", comp_row + 1,
                  "col", comp_col + 1)
            player_board[comp_row][comp_col] = "X"
            comp_hits += 1
            print("Computer score:", comp_hits)
        else:
            player_board[comp_row][comp_col] = "M"
            print("The computer missed your ship at row", comp_row + 1,
                  "col", comp_col + 1)
        # ending the game
        if comp_hits == 5:
            print("Computer won")
            print_board(player_board, empty_board)
            break

        if num_guesses == 0:
            print("Too many incorrect guesses. Game over")
            print_board(player_board, empty_board)
            break

        if comp_guess == 0:
            print("Computer has too many incorrect guesses. Game over")
            print_board(player_board, empty_board)
            break

        # End the game if the user sinks all computer's ships
        if num_hits == 5:
            print("You won")
            print_board(player_board, empty_board)
            break


if __name__ == "__main__":
    # Set up game constants
    NUMBER_SHIPS = 5
    SHIP_SIZES = 3
    board_sizes = {"1": 7, "2": 9, "3": 12}
    board_size = 0
# Calling necessaery functions and validation for playing the game again
board_sizes = {"1": 7, "2": 9, "3": 12}
while True:
    welcome()
    rules()
    difficulties = set_difficulty()
    board_size = board_sizes[difficulties]
    comp_board = [["O" for _ in range(board_size)] for _ in range(board_size)]
    empty_board = [["O" for _ in range(board_size)] for _ in range(board_size)]
    player_board = [
        ["O" for _ in range(board_size)] for _ in range(board_size)]
    player_board, comp_board = ships(board_size, player_board, comp_board)
    game(board_size, player_board, comp_board, empty_board)
    play_again = input("Do you want to play again? (y/n): ")
    while play_again.lower() not in ["y", "n"]:
        print("Invalid input")
        play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "n":
        break
