import sys
import numpy as np
import math
import pygame

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

ROW_COUNT = int(input("Enter Rows:"))
COLUMN_COUNT = int(input("Enter Columns:"))

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if(board[r][col] == 0):
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    #Check horizontal location for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if(board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece):
                return True

    #Check vertical location for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if(board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece):
                return True

    #Check positively sloped diagonal:
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if(board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece):
                return True

    #Check negatively sloped diagonal:
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if(board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece):
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * square_size, (r + 1) * square_size, square_size, square_size))
            pygame.draw.circle(screen, BLACK, (int(c  * square_size + square_size / 2), int((r + 1) * square_size + square_size / 2)), rad)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * square_size + square_size / 2), height - int(r * square_size + square_size / 2)), rad)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * square_size + square_size / 2), height - int(r * square_size + square_size / 2)), rad)
            elif board[r][c] == 3:
                pygame.draw.circle(screen, GREEN, (int(c * square_size + square_size / 2), height - int(r * square_size + square_size / 2)), rad)
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

#initialize pygame
pygame.init()

square_size = 100

rad = int(square_size / 2 - 5)

width = COLUMN_COUNT * square_size
height = (ROW_COUNT + 1) * square_size

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", int(11 * COLUMN_COUNT))

#gameloop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, square_size))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(square_size / 2)), rad)
            elif turn == 1:
                pygame.draw.circle(screen, YELLOW, (posx, int(square_size / 2)), rad)
            elif turn == 2:
                pygame.draw.circle(screen, GREEN, (posx, int(square_size / 2)), rad)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, square_size))

            #Ask player 1 input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / square_size))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (0, 0))
                        game_over = True


            #Ask player 2 input
            elif turn == 1:
                posx = event.pos[0]
                col = int(math.floor(posx / square_size))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (0, 0))
                        game_over = True

            #Ask player 3 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / square_size))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 3)

                    if winning_move(board, 3):
                        label = myfont.render("Player 3 wins!!", 1, GREEN)
                        screen.blit(label, (0, 0))
                        game_over = True


            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 3

            if game_over == True:
                pygame.time.wait(3000)
