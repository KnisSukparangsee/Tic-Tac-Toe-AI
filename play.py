from board import new_board
from render import render_board
from moves import make_move
from InvalidMoveException import InvalidMoveException
from get_winner import get_winner, is_draw
from sys import argv
from function_maps import function_map
from ai import finds_winning_moves_and_losing_moves_ai


def play():
    board = new_board()
    # Player X starts
    current_player = "X"
    ai_1 = function_map[argv[1]]
    ai_2 = function_map[argv[2]]
    try:
        # Loop until gameover
        while True:
            # Get coordinate from player
            if current_player == "X":
                coords = ai_1(board, current_player)
            else:
                coords = ai_2(board, current_player)
            # Make the move on the board
            board = make_move(coords, current_player, board)
            # Draw the board
            render_board(board)
            # Check if there is a winner
            winner = get_winner(board, current_player)
            # Declare winner if there is one
            if winner != None:
                print("THE WINNER IS " + winner + "!")
                if winner == "X":
                    return 1
                else:
                    return -1
            # If the board is full, then the game ends in a draw
            if is_draw(board):
                print("IT'S A DRAW!")
                return 0

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
    except InvalidMoveException as e:
        print(f"Exception: {e}")