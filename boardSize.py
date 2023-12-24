import pygame
import sys
from colors import *

class BoardSize:
    def __init__(self, font, initial_text=""):
        self.text = initial_text
        self.font = font
        self.cursor_visible = True
        self.cursor_timer = 0
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Entered name:", self.text)
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def controlBoard(self,screen,rc):
        clock = pygame.time.Clock()
        running = True
        cursor_frequency = 500
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Pass events to the TextInput instance
                self.handle_event(event)
                    
            # Draw the text on the screen
            screen.fill(WHITE)

            rc_no = self.font.render(f'Enter {rc} between 4 to 15:', True, WHITE)
            pygame.draw.rect(screen, BLACK, (375 - rc_no.get_width() // 2, 200,rc_no.get_width()+50,50))
            screen.blit(rc_no, (400 - rc_no.get_width() // 2, 200 + 15))

            # Draw the user-entered rc on the screen
            input_text = self.font.render(self.text, True, BLACK)
            screen.blit(input_text, (400 - input_text.get_width() // 2, 400 + 15))

            self.cursor_timer += clock.get_rawtime()
            if self.cursor_timer >= cursor_frequency:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = 0

            if self.cursor_visible:
                cursor_x = 400 - input_text.get_width() // 2 + input_text.get_width()
                pygame.draw.line(screen, BLACK, (cursor_x, 400 + 15), (cursor_x, 400 + 15 + self.font.get_linesize()))

            if pygame.key.get_pressed()[pygame.K_RETURN]:
                if self.text:
                    self.text=int(self.text)
                    running = False
                    
            # Update the display
            pygame.display.flip()


