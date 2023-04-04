import random

# Set up game constants
BOARD_SIZE = 10
NUM_SHIPS = 5
SHIP_SIZE = 3

# Set up game board
board = []
for i in range(BOARD_SIZE):
    row = ["O"] * BOARD_SIZE
    board.append(row)

# Place ships randomly
for i in range(NUM_SHIPS):
    ship_row = random.randint(0, BOARD_SIZE - 1)
    ship_col = random.randint(0, BOARD_SIZE - 1)

    # Ensure the ship does not overlap with another ship
    while board[ship_row][ship_col] == "S":
        ship_row = random.randint(0, BOARD_SIZE - 1)
        ship_col = random.randint(0, BOARD_SIZE - 1)

    # Place the ship
    for j in range(SHIP_SIZE):
        if ship_col + j < BOARD_SIZE:
            board[ship_row][ship_col + j] = "S"
        else:
            board[ship_row + 1][ship_col - (BOARD_SIZE - j)] = "S"

# Play the game
num_guesses = 0
num_hits = 0
while num_hits < SHIP_SIZE * NUM_SHIPS and num_guesses < BOARD_SIZE ** 2:
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







