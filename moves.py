from InvalidMoveException import InvalidMoveException


def get_move():
    while True:
        try:
            y = int(input("What is your move's y coordinate?: "))
            x = int(input("What is your move's x coordinate?: "))
            if x >= 0 and x <= 2 and y >= 0 and y <= 2:
                break
            print("Coordinate is out of bounds.")
        except TypeError:
            print("Invalid coordinate")
    return (y, x)


def make_move(coords, player, board):
    new_board = [["None" for _ in range(3)] for _ in range(3)]
    height, width = len(board), len(board[0])

    # Update new board to be the same as given board
    for i in range(height):
        for j in range(width):
            new_board[i][j] = board[i][j]
    
    # Change the new board's coordinate to the current player's mark
    x, y = coords[1], coords[0]
    if new_board[y][x] != "None":
        raise InvalidMoveException(f"Can't make move ({x}, {y}), square already taken!")
    new_board[y][x] = player

    return new_board