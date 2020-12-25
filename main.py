import pygame, sys
import numpy as np
import time
from computer import random_computer, available_sqrs,\
            convert_board_config_to_score, return_best_move
from helper_functions import choose_sqr, is_sqr_available,\
            is_board_full, mouse_to_array_position,\
            draw_sign, check_win, draw_horizontal_winning_line,\
            draw_diagonal_winning_line, draw_vertical_winning_line,\
            restart, draw_winning_line


_BOARD_ROWS = 3
_BOARD_COLS = 3
board = np.zeros((_BOARD_ROWS, _BOARD_COLS))

#print('Against whom would you like to play?')
#opponent = input('human / random computer / perfect computer: ')
opponent = 'perfect computer'

#initialise pygame
pygame.init()

player = 1
game_over = False

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            #mouse position
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            clicked_row = mouse_to_array_position(mouse_y)
            clicked_col = mouse_to_array_position(mouse_x)

            #human against human
            if opponent == 'human':
                if is_sqr_available(board, clicked_row, clicked_col):
                    if player == 1:
                        choose_sqr(board, clicked_row, clicked_col, 1)
                        if check_win(board, player):
                            game_over = True
                        player = 2
                    elif player == 2:
                        choose_sqr(board, clicked_row, clicked_col, 2)
                        if check_win(board, player):
                            game_over = True
                        player = 1

                    draw_sign(board)

            #human against random computer
            if opponent == 'random computer':
                if player == 1:
                    if is_sqr_available(board, clicked_row, clicked_col):
                        choose_sqr(board, clicked_row, clicked_col, 1)
                        if check_win(board, player):
                            game_over = True
                        else:
                            player = 2
                if player == 2:
                    position_x, position_y = random_computer(board)
                    choose_sqr(board, position_x, position_y, 2)
                    if check_win(board, player):
                        game_over = True
                    player = 1
                draw_sign(board)

            #human against perfect computer
            if opponent == 'perfect computer':
                if player == 1:
                    if is_sqr_available(board, clicked_row, clicked_col):
                        choose_sqr(board, clicked_row, clicked_col, 1)
                        if check_win(board, player):
                            game_over = True
                        else:
                            player = 2
                if player == 2:
                    position_x, position_y = return_best_move(board)
                    choose_sqr(board, position_x, position_y, 2)
                    if check_win(board, player):
                        game_over = True
                    else:
                        player = 1 
                
                draw_sign(board)

        if game_over:
            if check_win(board, 1):
                draw_winning_line(board, 1)
            if check_win(board, 2):
                draw_winning_line(board, 2)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart(board)
                game_over = False
                player = 1


    #updates the display
    pygame.display.update()