import pytest
from get_winner import get_winner, is_draw
from board import new_board
from ai import minimax_ai


@pytest.fixture
def draw():
    return [["X", "O", "X"], ["X", "O", "X"], ["O", "X", "O"]]


def test_get_winnder_draw(draw):
    x_win = get_winner(draw, "X")
    o_win = get_winner(draw, "X")
    assert x_win == None
    assert o_win == None

    
def test_get_winner_row():
    board = new_board()
    for i in range(len(board)):
        board[i][0] = "X"
    winner = get_winner(board, "X")
    assert winner == "X"


def test_get_winner_col():
    board = new_board()
    for j in range(len(board[0])):
        board[0][j] = "X"
    winner = get_winner(board, "X")
    assert winner == "X"


def test_get_winner_diag():
    board = new_board()
    for i in range(len(board)):
        board[i][i] = "X"
    winner = get_winner(board, "X")
    assert winner == "X"


def test_get_winner_no_winner():
    board = new_board()
    winner = get_winner(board, "X")
    assert winner == None
    board[0][0] = "X"
    board[0][2] = "X"
    board[2][2] = "X"
    winner = get_winner(board, "X")
    assert winner == None


def test_is_draw():
    board = new_board()
    draw = is_draw(board)
    assert draw == False
    board[0][0] = "X"
    board[0][1] = "O"
    board[1][0] = "X"
    board[2][1] = "X"
    board[2][2] = "X"
    board[0][2] = "X"
    board[1][1] = "O"
    board[1][2] = "O"
    board[2][0] = "O"
    winner = is_draw(board)
    assert winner == True

def test_minimax():
    board = new_board()
    board[0][0] = "X"
    board[1][0] = "O"
    move = minimax_ai(board, "X")
    assert move == (0, 1)

    board = new_board()
    board[0][0] = "X"
    board[1][1] = "O"
    board[0][1] = "X"
    move = minimax_ai(board, "X")
    assert move == (0, 2)
