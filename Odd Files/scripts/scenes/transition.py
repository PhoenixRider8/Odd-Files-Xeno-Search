from ..spritesheet.spriteList import *
from ..spritesheet.SpritesheetImport import SpriteSheet
import pygame as pg

class Transition:
    def __init__(self,screen,clock):
        self.screen = screen
        self.clock = clock
        self.FPS = 8

        self.index = 0 #9 frames for transition
        self.transitionPlaying = False

        self.transition = pg.image.load(transition_scene).convert_alpha()
        self.transitionImg = SpriteSheet(self.transition)
        self.transitionAnim = self.transitionImg.get_image(0, 128, 147, 1, (0,0,0))

    def draw(self):
        self.screen.fill((0,0,0))

        if(self.index < 9):
            self.index+=1
        else:
            self.transitionPlaying = False

        player_rect = self.transitionAnim.get_rect(center=(400, 300))  # Place player in center    
        self.transitionAnim = self.transitionImg.get_image(self.index, 800, 600, 1, (0,0,0)) 
        self.screen.blit(self.transitionAnim, player_rect)

        #update screen
        

        # Update the display after drawing
        pg.display.flip()
        pg.display.update()

    def event(self):
        """Event handling for this scene."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.transitionPlaying = False  # Stop the scene loop             

    def main2(self):
        self.event()  # Handle events
        self.draw()  # Render the scene

        # Limit frame rate
        self.clock.tick(self.FPS)

