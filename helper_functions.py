from board import screen, _BLACK, _WHITE, draw_lines
import numpy as np
import pygame

_BOARD_ROWS = 3
_BOARD_COLS = 3
_RED = (255, 0, 0)
_GREEN = (0, 255, 0)
_BLUE = (0, 0, 255)

#function that marks the field (row, col) with the entry of the player
def choose_sqr(board, row, col, player):
    board[row][col] = player

#function that returns bool for available sqr
def is_sqr_available(board, row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

#function that returns bool for full board
def is_board_full(board):
    for row in range(_BOARD_COLS):
        for col in range(_BOARD_COLS):
            if is_sqr_available(row, col):
                return False
    return True

def mouse_to_array_position(mouse_position):
    if 0 <= mouse_position <= 200:
        return 0
    elif 201 <= mouse_position <= 400:
        return 1
    elif 401 <= mouse_position <= 600:
        return 2

def draw_sign(board):
    for row in range(_BOARD_ROWS):
        for col in range(_BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen, _BLUE, (col*200+40, row*200+160), (col*200+160, row*200+40), 15)
                pygame.draw.line(screen, _BLUE, (col*200+40, row*200+40), (col*200+160, row*200+160), 15)
            if board[row][col] == 2:
                pygame.draw.circle(screen, _RED, (int(col*200+100), int(row*200+100)), 60, 10)

def check_win(board, player):
    ''''
    check if player has won or not, return boolean
    '''
    #check vertical win
    for col in range(_BOARD_COLS):
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] == player):
            #print('Player', player, 'has won!')
            return True
    #check horizontal win
    for row in range(_BOARD_ROWS):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] == player):
            #print('Player', player, 'has won!')
            return True
    #check diagonal win
    if (board[0][0] == player and  board[1][1] == player and board[2][2] == player):
        return True
    if (board[2][0] == player and  board[1][1] == player and board[0][2] == player):
        return True
    return False

def draw_winning_line(board, player):
    ''''
    check if player has won, if yes draw the winning line
    '''
    #check vertical win
    for col in range(_BOARD_COLS):
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] == player):
            draw_horizontal_winning_line(col, player)
    #check horizontal win
    for row in range(_BOARD_ROWS):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] == player):
            draw_vertical_winning_line(row, player)
    #check diagonal win
    if (board[0][0] == player and  board[1][1] == player and board[2][2] == player):
        draw_diagonal_winning_line(1, player)
    if (board[2][0] == player and  board[1][1] == player and board[0][2] == player):
        draw_diagonal_winning_line(2, player)

def draw_vertical_winning_line(col, player):
    if player == 1:
        pygame.draw.line(screen, _BLUE, (30, col*200+100), (570, col*200+100), 50)
    if player == 2:
        pygame.draw.line(screen, _RED, (30, col*200+100), (570, col*200+100), 50)


def draw_horizontal_winning_line(row, player):
    if player == 1:
        pygame.draw.line(screen, _BLUE, (row*200+100, 30), (row*200+100, 570), 50)
    if player == 2:
        pygame.draw.line(screen, _RED, (row*200+100, 30), (row*200+100, 570), 50)

        
def draw_diagonal_winning_line(diag, player):
    if diag == 1:
        if player == 1:
            pygame.draw.line(screen, _BLUE, (40, 40), (560, 560), 50)
        if player == 2:
            pygame.draw.line(screen, _RED, (40, 40), (560, 560), 50)
    if diag == 2:
        if player == 1:
            pygame.draw.line(screen, _BLUE, (40, 560), (560, 40), 50)
        if player == 2:
            pygame.draw.line(screen, _RED, (40, 560), (560, 40), 50)

def restart(board):
    screen.fill(_WHITE)
    draw_lines()    
    for row in range(3):
       for col in range(3):
           board[row][col] = 0