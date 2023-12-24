import pygame
import sys
import shelve
from colors import *
class TextInput:
    def __init__(self,font, initial_text=""):
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

    def save_name(self):
        with shelve.open('scores') as shelf:
            # Retrieve existing data from the shelf
            name_score = shelf.get('name_score', {})
            for name, score in name_score.items():
                print(f"Name: {name}, Score: {score}")
            # Update the data
            if self.text not in name_score:
                name_score[self.text] = 0

            # Save the updated data back to the shelf
            shelf['name_score'] = name_score

    def controlName(self,screen,player_no):
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

            enter_name = self.font.render(f"Enter {player_no} Name", True, WHITE)
            pygame.draw.rect(screen, BLACK, (375 - enter_name.get_width() // 2, 200,enter_name.get_width()+50,50))
            screen.blit(enter_name, (400 - enter_name.get_width() // 2, 200 + 15))

            # Draw the user-entered text on the screen
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
                    running = False
                    self.save_name()
                    
            # Update the display
            pygame.display.flip()


