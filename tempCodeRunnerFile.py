while True:
    welcome()
    rules()
    difficulties = set_diff()
    board_size = board_sizes[difficulties]
    comp_board = [['O' for x in range(board_size)] for y in range(board_size)]
    player_board = [['O' for x in range(board_size)] for y in range(board_size)]
    player_board, comp_board = ships(board_size, player_board, comp_board)

    game(board_size, comp_board)
    break