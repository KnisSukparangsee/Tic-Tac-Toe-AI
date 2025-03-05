def render_board(board):
    height, width = len(board), len(board[0])
    print()

    # Coordinate markers
    print("  ", end="")
    for i in range(2 * width + 1):
        if i % 2 == 1:
            print(int((i - 1) / 2), end="")
        else:
            print(" ", end="")
    print()
    print("  ", end="")

    # Top line
    for _ in range(2 * width + 1):
        print("_", end="")
    print()

    # Board rows
    for i in range(len(board)):
        print(f"{i} |", end="")
        line = " ".join(" " if x == "None" else str(x) for x in board[i])
        print(line + "|")
    print("  ", end="")

    # Bottom line
    for _ in range(2 * width + 1):
        print("‾", end="")
    print()