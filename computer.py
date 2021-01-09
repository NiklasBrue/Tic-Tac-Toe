import numpy as np
import random
from helper_functions import is_sqr_available, check_win
   
def available_sqrs(board):
    available_sqrs = []
    for row in range(3):
        for col in range(3):
            if is_sqr_available(board, row, col):
                available_sqrs.append([row, col])
    return available_sqrs

#random computer moves
def random_computer(board):
    avail_sqrs = available_sqrs(board)
    if not avail_sqrs:
        print('Game over')
    else:
        random_move = random.choice(avail_sqrs)
        return random_move[0], random_move[1]
