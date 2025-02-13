import pygame as pg
import time
import sys

from scripts.config import *
from scripts.dialogue.timerMin import Timer

from scripts.enemies.virus import Virus
from scripts.player.player import Player
from scripts.spritesheet.outcome import Outcome
from scripts.scan.scanner import FileChecker

class Scene3:
    def __init__(self, screen, clock):
        self.screen = screen
        self.all_sprites = pg.sprite.LayeredUpdates()

        self.clock = clock
        self.font = pg.font.Font(FONT, 36)  # Load the font using pg.font.Font
        self.timer = Timer(self.screen, self.font, 600,30)
        self.timer.set_time(0,40)

        #Player
        self.player = Player(self, 2, 2)  # Positioned at (32, 64)

        #virus
        self.virus = Virus(WIN_WIDTH/2, 50, 128, 128, 2, (0, 0, 0))
        self.virusPlaying = False

        self.virus_sprites = pg.sprite.Group()
        self.virus_sprites.add(self.virus)

        #File checking
        self.folder_path = 'filesDel/boss1'
        self.filesToCheck = ['33','73']
        self.file_check = FileChecker(self.folder_path,self.filesToCheck)

        #Outcome
        self.outcome = Outcome(self.screen)

    def events(self):
        """Event loop for the game."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.virusPlaying = False
                #Quit Game
                pg.quit()
                sys.exit()

    def update(self):
        self.dt = self.clock.tick(60) / 1000  # Delta time in seconds
        
        # Check for game over (timer runs out)
        if self.timer.time_left == 0:
            self.outcome.show_game_over()
            time.sleep(7)
            self.virusPlaying = False  # End the game after showing game over screen

        #Check if files deleted or not
        elif self.file_check.check_files_deleted():  # If files are deleted, player wins
            self.outcome.show_game_won()
            time.sleep(3)
            self.virusPlaying = False  # End the game after showing game won screen



    def draw(self):
        """Draw the game elements to the screen."""
        self.virus_sprites.update(self.dt)
        self.screen.fill(BLACK)
        self.screen.blit(self.player.playerAnim, (WIN_WIDTH/2, WIN_HEIGHT / 1.3))
        self.virus_sprites.draw(self.screen)
        self.timer.update()

        self.clock.tick(FPS)
        
        pg.display.update()  # Update pygame screen 

    def main(self):
        self.events();
        
        self.update()
        self.draw()