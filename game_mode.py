import pygame
import sys
from pygame.locals import *
from colors import *
from threePlayers import Connect4Game3
from twoPlayers import Connect4Game2
from inputName import *
from boardSize import BoardSize

class GameModeScreen:
    def __init__(self):
        self.two_players_button_rect = None
        self.three_players_button_rect = None

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.two_players_button_rect.collidepoint(event.pos):
                return "TwoPlayers"
            elif self.three_players_button_rect.collidepoint(event.pos):
                return "ThreePlayers"

    def draw(self,screen,font):
        screen.fill(WHITE)

        two_players_text = font.render("Two Players", True, WHITE)
        pygame.draw.rect(screen, BLACK, (375 - two_players_text.get_width() // 2, 200,two_players_text.get_width()+50,50))
        self.two_players_button_rect = pygame.Rect(375 - two_players_text.get_width() // 2, 200,two_players_text.get_width()+50,50)
        screen.blit(two_players_text, (400 - two_players_text.get_width() // 2, 200 + 15))

        three_players_text = font.render("Three Players", True, WHITE)
        pygame.draw.rect(screen, BLACK, (375 - three_players_text.get_width() // 2, 400,three_players_text.get_width()+50,50))
        self.three_players_button_rect = pygame.Rect(375 - three_players_text.get_width() // 2, 400,three_players_text.get_width()+50,50)
        screen.blit(three_players_text, (400 - three_players_text.get_width() // 2, 400 + 15))

    def action(self,screen,font):

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                new_screen = self.handle_event(event)
                if new_screen:
                    # Add logic for transitioning based on the selected game mode
                    print(f"Selected Game Mode: {new_screen}")
                    if new_screen == "ThreePlayers":
                        player1=TextInput(font)
                        player1.controlName(screen,"1st Player's")
                        player2=TextInput(font)
                        player2.controlName(screen,"2nd Player's")
                        player3=TextInput(font)
                        player3.controlName(screen,"3rd Player's")
                        
                        row=BoardSize(font)
                        row.controlBoard(screen,'row')
                        column=BoardSize(font)
                        column.controlBoard(screen,'column')

                        game = Connect4Game3(row.text,column.text)
                        game.draw_board()
                        game.run_game(font,player1.text,player2.text,player3.text)
                        
                        screen = pygame.display.set_mode((800, 700))
                        pygame.display.flip()

                    elif new_screen == "TwoPlayers":
                        player1=TextInput(font)
                        player1.controlName(screen,"1st Player's")
                        player2=TextInput(font)
                        player2.controlName(screen,"2nd Player's")
                        print(player1.text)
                        print(player2.text)

                        row=BoardSize(font)
                        row.controlBoard(screen,'row')
                        column=BoardSize(font)
                        column.controlBoard(screen,'column')

                        game = Connect4Game2(row.text,column.text)
                        game.draw_board()
                        game.run_game(font,player1.text,player2.text)

                        screen = pygame.display.set_mode((800, 700))
                        pygame.display.flip()

            self.draw(screen,font)

            # Refresh the display
            pygame.display.flip()
