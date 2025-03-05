import numpy as np
from moves import get_move
from board import new_board


def random_ai(board, player):
    height, width = len(board), len(board[0])
    coords = []
    for i in range(height):
        for j in range(width):
            if board[i][j] == "None":
                coords.append((i, j))
    if len(coords) == 0:
        return None
    rng = np.random.default_rng()
    idx = rng.integers(low=0, high=len(coords))
    return coords[idx]


def finds_winning_moves_ai(board, player):
    height, width = len(board), len(board[0])
    # Check for winning move
    coords = winning_move(board, player)
    if coords != None:
        return coords
    return random_ai(board, player)


def winning_move(board, player):
    height, width = len(board), len(board[0])

    # Check row
    for i in range(height):
        if winning_state(board[i][0], board[i][1], board[i][2], player):
            empty_col = find_empty_cell(board[i])
            if empty_col != None:
                return (i, empty_col)
    # Check col
    for j in range(width):
        cols = [board[i][j] for i in range(height)]
        if winning_state(board[0][j], board[1][j], board[2][j], player):
            empty_row = find_empty_cell(cols)
            if empty_row != None:
                return (empty_row, j)
    # Check diag
    diag_1 = [board[i][i] for i in range(height)]
    if winning_state(board[0][0], board[1][1], board[2][2], player):
        empty_cell = find_empty_cell(diag_1)
        if empty_cell != None:
            return (empty_cell, empty_cell)
        
    diag_2 = [board[i][width - 1 - i] for i in range(height)]
    if winning_state(board[0][2], board[1][1], board[2][0], player):
        empty_cell = find_empty_cell(diag_2)
        if empty_cell != None:
            return (empty_cell, width - empty_cell - 1)
        
    return None


def find_empty_cell(cells):
    for idx, cell in enumerate(cells):
        if cell == "None":
            return idx
    return None


def winning_state(a, b, c, player):
    cond1 = a == player and b == player and c == "None";
    cond2 = a == player and b == "None" and c == player;
    cond3 = a == "None" and b == player and c == player;
    return cond1 or cond2 or cond3


def finds_winning_moves_and_losing_moves_ai(board, player):
    height, width = len(board), len(board[0])
    # Check for winning move
    coords = winning_move(board, player)
    if coords != None:
        return coords
    # Check for losing move
    coords = block_losing_move(board, player)
    if coords != None:
        return coords
    return random_ai(board, player)

        
def block_losing_move(board, player):
    if player == "X":
        player = "O"
    else :
        player = "X"
    return winning_move(board, player)


def human(board, player):
    return get_move()


def minimax_ai(board, player):
    moves = get_legal_moves(board)
    scores = []
    for move in moves:
        next_board = make_move(board, move, player)
        opponent = get_opponent(player)
        score = minimax_score(next_board, opponent)
        scores.append(score)
    coord = get_coord_for_minmax(moves, scores, player)
    return coord

def get_coord_for_minmax(moves, scores, player):
    if player == "X":
        best_score = -float("inf")
        best_move = None
        for i in range(len(moves)):
            if scores[i] > best_score:
                best_score = scores[i]
                best_move = moves[i]
    else:
        best_score = float("inf")
        best_move = None
        for i in range(len(moves)):
            if scores[i] < best_score:
                best_score = scores[i]
                best_move = moves[i]
    return best_move



def minimax_score(board, player):
    if x_wins(board):
        return 10
    elif o_wins(board):
        return -10
    elif is_draw(board):
        return 0
    
    legal_moves = get_legal_moves(board)
    scores = []
    cache = {}
    for move in legal_moves:
        new_board = make_move(board, move, player)
        string = board_to_string(new_board)
        if string not in cache:
            opponent = get_opponent(player)
            score = minimax_score(new_board, opponent)
            cache[string] = score
        else:
            score = cache[new_board]
        scores.append(score)
    if player == "X":
        return max(scores)
    else:
        return min(scores)
    

def board_to_string(board):
    string = ""
    for row in board:
        for cell in row:
            string += cell
    return string


def x_wins(board):
    return is_winning_move(board, "X")
    

def o_wins(board):
    return is_winning_move(board, "O")

def is_winning_move(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(len(board)):
        if all(board[row][col] == player for row in range(len(board))):
            return True
    if all(board[i][i] == player for i in range(len(board))):
        return True
    if all(board[i][2 - i] == player for i in range(len(board))):
        return True
    return False
    


def is_draw(board):
    for row in board:
        for cell in row:
            if cell == "None":
                return False
    return True


def get_legal_moves(board):
    moves = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "None":
                moves.append((i, j))
    return moves


def make_move(board, move, player):
    n_board = [row[:] for row in board]
    n_board[move[0]][move[1]] = player
    return n_board


def get_opponent(player):
    if player == "X":
        return "O"
    else:
        return "X"
