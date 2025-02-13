import pygame
from ..spritesheet.spriteList import *
from ..spritesheet.SpritesheetImport import SpriteSheet
from ..config import *

class MainMenu:

    def __init__(self):
        self.canvas = None
        self.startButton = None
        self.quitButton = None
        self.start_button_rect = None
        self.quit_button_rect = None

    def mainMenu(self, canvas):
        self.canvas = canvas
        self.title_screen = pygame.image.load(TITLE_SCREEN_PIC).convert_alpha()

        # Load the button image and create a SpriteSheet instance
        self.buttonImage = pygame.image.load(menubuttons).convert_alpha()
        self.buttons = SpriteSheet(self.buttonImage)
        
        # Get the start and quit button images
        self.startButton = self.buttons.get_image(0, 112, 45, 1, BLACK)
        self.quitButton = self.buttons.get_image(1, 112, 45, 1, BLACK)

        # Set the position for the start and quit buttons
        self.start_button_rect = self.startButton.get_rect(center=(self.canvas.get_width() // 2, self.canvas.get_height() // 2 - 50))
        self.quit_button_rect = self.quitButton.get_rect(center=(self.canvas.get_width() // 2, self.canvas.get_height() // 2 + 50))

        #self.jokerAnimation()

        # Draw buttons to the screen
        self.canvas.blit(self.startButton, self.start_button_rect)
        self.canvas.blit(self.quitButton, self.quit_button_rect)

    def intro_screen(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle mouse click events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect.collidepoint(event.pos):
                        self.start_game()
                    elif self.quit_button_rect.collidepoint(event.pos):
                        self.quit_game()

            # Update the screen by redrawing the main menu
            self.mainMenu(self.canvas)

            # Update the display
            pygame.display.flip()

    def start_game(self):
        """Called when the start button is clicked."""
        print("Start Game clicked!")
        # Implement logic to transition to the game screen or start the game

    def quit_game(self):
        """Called when the quit button is clicked."""
        print("Quit clicked!")
        pygame.quit()
        exit()
