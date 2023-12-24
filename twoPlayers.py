import sys
import numpy as np
import math
import pygame
import shelve
from colors import *

class Connect4Game2:
    def __init__(self, row_count, column_count):
        self.row_count = row_count
        self.column_count = column_count
        self.board = np.zeros((row_count, column_count))

        self.game_over = False
        self.turn = 0

        self.screen = pygame.display.set_mode((column_count*60, row_count*60+60))

        self.square_size = 60
        self.rad = int(self.square_size / 2 - 5)

        self.width = column_count * self.square_size
        self.height = (row_count + 1) * self.square_size

        self.size = (self.width, self.height)


    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[self.row_count - 1][col] == 0

    def get_next_open_row(self, col):
        for r in range(self.row_count):
            if self.board[r][col] == 0:
                return r

    def print_board(self):
        print(np.flip(self.board, 0))

    def winning_move(self, piece):
        # Check horizontal location for win
        for c in range(self.column_count - 3):
            for r in range(self.row_count):
                if (
                    self.board[r][c] == piece
                    and self.board[r][c + 1] == piece
                    and self.board[r][c + 2] == piece
                    and self.board[r][c + 3] == piece
                ):
                    return True

        # Check vertical location for win
        for c in range(self.column_count):
            for r in range(self.row_count - 3):
                if (
                    self.board[r][c] == piece
                    and self.board[r + 1][c] == piece
                    and self.board[r + 2][c] == piece
                    and self.board[r + 3][c] == piece
                ):
                    return True

        # Check positively sloped diagonal:
        for c in range(self.column_count - 3):
            for r in range(self.row_count - 3):
                if (
                    self.board[r][c] == piece
                    and self.board[r + 1][c + 1] == piece
                    and self.board[r + 2][c + 2] == piece
                    and self.board[r + 3][c + 3] == piece
                ):
                    return True

        # Check negatively sloped diagonal:
        for c in range(self.column_count - 3):
            for r in range(3, self.row_count):
                if (
                    self.board[r][c] == piece
                    and self.board[r - 1][c + 1] == piece
                    and self.board[r - 2][c + 2] == piece
                    and self.board[r - 3][c + 3] == piece
                ):
                    return True

    def draw_board(self):
        for c in range(self.column_count):
            for r in range(self.row_count):
                pygame.draw.rect(
                    self.screen,
                    WHITE,
                    (c * self.square_size, (r + 1) * self.square_size, self.square_size, self.square_size),
                )
                pygame.draw.circle(
                    self.screen,
                    BLACK,
                    (int(c * self.square_size + self.square_size / 2), int((r + 1) * self.square_size + self.square_size / 2)),
                    self.rad,
                )
        pygame.display.update()

        for c in range(self.column_count):
            for r in range(self.row_count):
                if self.board[r][c] == 1:
                    pygame.draw.circle(
                        self.screen,
                        RED,
                        (int(c * self.square_size + self.square_size / 2), self.height - int(r * self.square_size + self.square_size / 2)),
                        self.rad,
                    )
                elif self.board[r][c] == 2:
                    pygame.draw.circle(
                        self.screen,
                        GREEN,
                        (int(c * self.square_size + self.square_size / 2), self.height - int(r * self.square_size + self.square_size / 2)),
                        self.rad,
                    )
                
        pygame.display.update()

    def run_game(self,myfont,p1name,p2name):

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, BLACK, (0, 0, self.width, self.square_size))
                    posx = event.pos[0]
                    if self.turn == 0:
                        pygame.draw.circle(self.screen, RED, (posx, int(self.square_size / 2)), self.rad)
                    elif self.turn == 1:
                        pygame.draw.circle(self.screen, GREEN, (posx, int(self.square_size / 2)), self.rad)
                    
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, BLACK, (0, 0, self.width, self.square_size))

                    # Ask player 1 input
                    if self.turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / self.square_size))
                        if self.is_valid_location(col):
                            row = self.get_next_open_row(col)
                            self.drop_piece(row, col, 1)

                            if self.winning_move(1):
                                total_wins=0
                                with shelve.open('scores') as shelf:
                                    name_score = shelf.get('name_score', {})
                                    name_score[p1name] += 1
                                    total_wins = name_score[p1name]
                                    shelf['name_score'] = name_score

                                winner = myfont.render(f"{p1name} wins!!", 1, RED)
                                winner_total_win = myfont.render(f"Total Wins: {total_wins}", 1, RED)
                                self.screen.blit(winner, (self.width//2 - winner.get_width()//2, 5))
                                self.screen.blit(winner_total_win, (self.width//2 - winner_total_win.get_width()//2, 30))
                                self.game_over = True

                    # Ask player 2 input
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx / self.square_size))
                        if self.is_valid_location(col):
                            row = self.get_next_open_row(col)
                            self.drop_piece(row, col, 2)

                            if self.winning_move(2):
                                total_wins=0
                                with shelve.open('scores') as shelf:
                                    name_score = shelf.get('name_score', {})
                                    name_score[p2name] += 1
                                    total_wins = name_score[p2name]
                                    shelf['name_score'] = name_score
                                winner = myfont.render(f"{p2name} wins!!", 1, GREEN)
                                winner_total_win = myfont.render(f"Total Wins: {total_wins}", 1, GREEN)
                                self.screen.blit(winner, (self.width//2 - winner.get_width()//2, 5))
                                self.screen.blit(winner_total_win, (self.width//2 - winner_total_win.get_width()//2, 30))
                                self.game_over = True

                    self.print_board()
                    self.draw_board()
                    self.turn += 1
                    self.turn = self.turn % 2

                    if self.game_over:
                        pygame.time.wait(5000)
                        return
