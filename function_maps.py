from ai import random_ai, finds_winning_moves_ai, finds_winning_moves_and_losing_moves_ai, human, minimax_ai


function_map = {
    "random": random_ai,
    "finds_winning": finds_winning_moves_ai,
    "finds_winning_and_losing": finds_winning_moves_and_losing_moves_ai,
    "human": human,
    "minimax": minimax_ai
}