def get_winner(board, player):
    height, width = len(board), len(board[0])
    # Check rows
    for row in board:
        if all(char == player for char in row):
            return player

    # Check columns
    for j in range(width):
        if all(player == board[i][j] for i in range(height)):
            return player

    # Check diagonal
    if all((player == board[i][i]) for i in range(height)):
        return player
    
    if all((player == board[i][width - 1 - i]) for i in range(height)):
        return player
        

def is_draw(board):
    for row in board:
        for char in row:
            if char == "None":
                return False
    return True