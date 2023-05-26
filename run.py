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
    return comp_board, empty_board
def print_board(player_board, comp_board):
    """
    printing both boards together
    """
    print("Player board:")
    for row in player_board:
        print(" ".join(row))
    print()
    print("Computer board:")
    for row in empty_board:
        print(" ".join(row))  
    print()


def ships(board_size: int, player_board, comp_board):
    """
    Place ships randomly
    """
    for i in range (NUMBER_SHIPS):
        x = randint(0, board_size - 1)
        y = randint(0, board_size - 1)
        comp_ships.append((x,y))
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


# Computers turn
def computer_guess(player_board):
    global board_size
    while True:
        guess_row = randint(0, board_size - 1)
        guess_col = randint(0, board_size - 1)
        # See if the computer guessed these positions before,
        # if not then it can try out these positions
        if [guess_row, guess_col] not in comp_guess:
            break
        computer_guess.append([guess_row, guess_col])


def game(board_size: int, player_board, comp_board, empty_board):
    """
    Gameplay loop method
    """
    # Play the game
    num_guesses = 20
    num_hits = 0
    comp_hits = 0
    comp_guess = 20
    revealed = False

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

        if guess_row < 0 or guess_row >= board_size or guess_col < 0 or guess_col >= board_size:
            print("Invalid coordinate. Please enter a valid coordinate.")
            continue

        if empty_board[guess_row][guess_col] == "M" or empty_board[guess_row][guess_col] == "S":
            print("You guessed the same coordinates before.")
            continue

        # Check if user hits a ship
    
        if empty_board[guess_row][guess_col] == "S":
            if player_board[guess_row][guess_col] == "H":
                print("You've already hit that location.")
            else:
                print("Hit!")
                player_board[guess_row][guess_col] = "H"
                num_hits += 1
                print("Player score:", num_hits)
        else:
            # If user misses a ship
            empty_board[guess_row][guess_col] = "M"
            print("Miss!")
            num_guesses -= 1
            print("Guesses remaining:", num_guesses)

        # End the game if the user sinks all computer's ships
        if num_hits == 5:
            print("You won")
            break

        # Computer's turn
        comp_row = randint(0, board_size - 1)
        comp_col = randint(0, board_size - 1)
        if comp_board[comp_row][comp_col] == "S":
            print("The computer hit your ship at row", comp_row + 1, "column", comp_col + 1, "!")
            comp_board[comp_row][comp_col] = "H"
            comp_hits += 1
            print("Computer's score:", comp_hits)
        else:
            print("The computer missed at row", comp_row + 1, "column", comp_col + 1, ".")

        # If computer sinks all of user's ships
        if comp_hits == 5:
            print("Computer won")
            break

        if num_guesses == 0:
            print("Too many incorrect guesses. Game over")
            break

        if comp_guess == 0:
            print("Computer has too many incorrect guesses. Game over")
            break
       
if __name__ == "__main__":
    # Set up game constants
    NUMBER_SHIPS = 5
    SHIP_SIZES = 3
    board_sizes = {"1": 7, "2": 9, "3": 12}
    board_size = 0
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
       #idea from the linked battleships game
        comp_board = [["O" for x in range(board_size)] for y in range(board_size)]
        empty_board = [["O" for x in range(board_size)] for y in range(board_size)]
        player_board = [["O" for x in range(board_size)] for y in range(board_size)]
        player_board, comp_board = ships(board_size, player_board, comp_board)
        game(board_size, player_board, comp_board, empty_board)
        break


