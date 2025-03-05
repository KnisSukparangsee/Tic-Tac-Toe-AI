from ai import finds_winning_moves_ai, finds_winning_moves_and_losing_moves_ai
from board import new_board


def test_finds_winning_moves_ai_col():
    board = new_board()
    board[0][0] = "X"
    board[1][0] = "X"
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (2, 0)
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (2, 0)

    board[1][0] = "None"
    board[2][0] = "X"
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (1, 0)
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (1, 0)

    board[0][0] = "None"
    board[1][0] = "X"
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (0, 0)
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (0, 0)
    

def test_finds_winning_moves_ai_row():
    board = new_board()
    board[0][0] = "X"
    board[0][1] = "X"
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (0, 2)
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (0, 2)


def test_finds_winning_moves_ai_diag():
    board = new_board()
    board[0][0] = "X"
    board[1][1] = "X"
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (2, 2)
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (2, 2)

    board[0][0] = "None"
    board[2][0] = "X"
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (0, 2)
    coord = finds_winning_moves_ai(board, "X")
    assert coord == (0, 2)    


# Finds winning and blocks losing moves ai
def test_finds_winning_moves_and_losing_moves_ai():
    board = new_board()
    board[0][0] = "X"
    board[1][0] = "X"
    coord = finds_winning_moves_and_losing_moves_ai(board, "X")
    assert coord == (2, 0)
    board[0][0] = "O"
    board[1][1] = "O"
    coord = finds_winning_moves_and_losing_moves_ai(board, "X")
    assert coord == (2, 2)
    coord = finds_winning_moves_and_losing_moves_ai(board, "X")
    assert coord == (2, 2)
    coord = finds_winning_moves_and_losing_moves_ai(board, "X")
    assert coord == (2, 2)
    board[0][0] = "None"
    board[0][1] = "O"
    coord = finds_winning_moves_and_losing_moves_ai(board, "X")
    assert coord == (2, 1)
    coord = finds_winning_moves_and_losing_moves_ai(board, "X")
    assert coord == (2, 1)
    coord = finds_winning_moves_and_losing_moves_ai(board, "X")
    assert coord == (2, 1)

