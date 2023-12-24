import pygame
from pygame.locals import *
import sys
from welcome import *
from game_mode import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Connect 4 - Game")

font = pygame.font.Font(None, 36)
current_screen = WelcomeScreen()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        new_screen = current_screen.handle_event(event)
        if new_screen:
            if new_screen == "Game":
                # Add logic for transitioning to the game screen
                print("Starting Connect 4 Game")
                option_screen= GameModeScreen()
                option_screen.action(screen,font)

    current_screen.draw(screen,font)
    pygame.display.flip()

