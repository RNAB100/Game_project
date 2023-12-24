import pygame
from pygame.locals import *
from colors import *


class WelcomeScreen:
    def __init__(self):
        self.start_button_rect = None

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.start_button_rect.collidepoint(event.pos):
                return "Game"

    def draw(self,screen,font):
        screen.fill(WHITE)
        
        welcome_text = font.render("Welcome to Connect 4!", True, BLACK)
        screen.blit(welcome_text, (400 - welcome_text.get_width() // 2, 200))
        
        button_text = font.render("Enter Game Mode", True, WHITE)
        pygame.draw.rect(screen, BLACK, (375 - button_text.get_width() // 2, 400,button_text.get_width()+50,50))
        self.start_button_rect = pygame.Rect(375 - button_text.get_width() // 2, 400,button_text.get_width()+50,50)
        screen.blit(button_text, (400 - button_text.get_width() // 2, 400 + 15))