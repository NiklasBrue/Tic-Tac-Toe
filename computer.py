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


#----------------------------------------------------------
#perfect computer
def convert_board_config_to_score(board):
    if check_win(board, 1):
        return -1
    if check_win(board, 2):
        return 1
    if not check_win(board, 1) and not check_win(board, 2):
        return 0

def minimax(board, depth, is_max):
    score = convert_board_config_to_score(board)
    print('#DEBUG score: ', score)
    print('#DEBUG depth: ', depth)
    avail_sqrs = available_sqrs(board)
    if score == -1:
        return score
    if score == 1:
        return score
    if not avail_sqrs:
        return 0
    if is_max:
        best_score = 2
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = 2
                    best_score = min(best_score, minimax(board, depth+1, False))
                    board[row][col] = 0
        return best_score
    else:
        best_score = -2
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = 1
                    best_score = max(best_score, minimax(board, depth+1, True))
                    board[row][col] = 0
        return best_score

def return_best_move(board):
    best_score = -2
    best_move_x = -1
    best_move_y = -1
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = 2
                eval_move = minimax(board, 0, True)
                board[row][col] = 0
                if eval_move > best_score:
                    best_move_x = row # this could be switched
                    best_move_y = col
                    best_score = eval_move
    return best_move_x, best_move_y


def perfect_computer(board):
    pass
