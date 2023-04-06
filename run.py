import random

# Set up game constants
#BOARD_SIZE = 10
NUMBER_SHIPS = 5
SHIP_SIZES = 3
easy_mode = 1
medium_mode = 2
hard_mode = 3
board_sizes = {easy_mode: 7, medium_mode: 9, hard_mode: 12}

# Set up game board
print("Select your difficulty level")
print("1. easy")
print("2. medium")
print("3. hard")
difficulties = int(input("Enter desired difficulty"))
board_size = board_sizes.get(difficulties)
board = []
for i in range(board_size):
    row = ["O"] * board_size
    board.append(row)

print(f"Board size: {board_size}x{board_size}")

# Place ships randomly
for i in range(NUMBER_SHIPS):
    ship_row = random.randint(0, board_size - 1)
    ship_col = random.randint(0, board_size - 1)

    # Ensure the ship does not overlap with another ship
    while board[ship_row][ship_col] == "S":
        ship_row = random.randint(0, board_size - 1)
        ship_col = random.randint(0, board_size - 1)

    # Place the ship
    for j in range(SHIP_SIZES):
        if ship_col + j < board_size:
            board[ship_row][ship_col + j] = "S"
        else:
            board[ship_row + 1][ship_col - (board_size - j)] = "S"

# Play the game
num_guesses = 0
num_hits = 0
while num_hits < SHIP_SIZES * NUMBER_SHIPS and num_guesses < board_size ** 2:
    # Print the game board
    for row in board:
        print(" ".join(row))

    # Get user input
    guess_row = int(input("Guess row: "))
    guess_col = int(input("Guess col: "))

    # Check if the guess is a hit or a miss
    if board[guess_row][guess_col] == "S":
        print("Hit!")
        board[guess_row][guess_col] = "X"
        num_hits += 1
    else:
        print("Miss!")
        board[guess_row][guess_col] = "X"

    num_guesses += 1

# End the game
print("Game over!")
for row in board:
    print(" ".join(row))

print("Number of guesses:", num_guesses)
print("Number of hits:", num_hits)







