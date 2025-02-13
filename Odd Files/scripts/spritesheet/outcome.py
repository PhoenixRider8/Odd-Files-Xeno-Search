import pygame as pg

from scripts.spritesheet.spriteList import game_over,game_won

import pygame as pg
from scripts.spritesheet.spriteList import game_over, game_won

import pygame as pg
from scripts.spritesheet.spriteList import game_over, game_won

class Outcome:
    def __init__(self, screen):
        self.screen = screen
        self.font = pg.font.SysFont('Arial', 48)
        self.gameOver = pg.image.load(game_over)  # Load the image for game over
        self.gameWon = pg.image.load(game_won)  # Load the image for game won

    def show_game_over(self):
        """Function to display the 'Game Over' screen"""
        self.screen.fill((0, 0, 0))  # Clear screen with black background
        
        # Get the rect of the image and center it on the screen
        game_over_rect = self.gameOver.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(self.gameOver, game_over_rect)  # Blit the image
        
        pg.display.flip()  # Update display

    def show_game_won(self):
        """Function to display the 'Game Won' screen"""
        self.screen.fill((0, 0, 0))  # Clear screen with black background
        
        # Get the rect of the image and center it on the screen
        game_won_rect = self.gameWon.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(self.gameWon, game_won_rect)  # Blit the image
        
        pg.display.flip()  # Update display
