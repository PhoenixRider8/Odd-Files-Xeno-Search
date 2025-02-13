from ..spritesheet.spriteList import *
from ..spritesheet.SpritesheetImport import SpriteSheet
from ..config import *
import pygame as pg
import sys
from ..dialogue.dialogueSys import DialogueSystem

class Scene2:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.counter = 0
        self.FPS = 5
        
        # Player
        self.playerIndex = 0
        self.playerIndex2 = 0
        self.playerDown = pg.image.load(player_idle).convert_alpha()
        self.playerImage = SpriteSheet(self.playerDown)
        self.playerAnim1 = self.playerImage.get_image(0, 70, 120, 1, BLACK)

        self.playerSearch = pg.image.load(player_search).convert_alpha()
        self.playerImage2 = SpriteSheet(self.playerSearch)
        self.playerAnim2 = self.playerImage2.get_image(0, 70, 120, 1, BLACK)

        # Dialogue System
        self.dialogue_system = DialogueSystem(self.screen, FONT)
        self.dialogue_system.change_font_size(25)
        self.setDialogue1()

        self.scene1Playing = True
        self.isSpace = False

    def setDialogue1(self):
        self.dialogue_system.add_dialogue("Xeno", "Help me defeat him!")
        self.dialogue_system.add_dialogue("Xeno", "Time to search")

    def playerAnimation(self):
        # Player animation logic
        if not self.isSpace:  # If space hasn't been pressed yet, show idle animation
            if self.playerIndex > 1:  # PlayerIdle has 2 frames
                self.playerIndex = 0  # Reset to the first frame
            else:
                self.playerAnim = self.playerImage.get_image(self.playerIndex, 70, 120, 1, BLACK)
                self.playerIndex += 1
            player_rect = self.playerAnim.get_rect(center=(WIN_WIDTH / 2, 100))
            self.screen.blit(self.playerAnim, player_rect)
        else:  # Once space is pressed, show playerSearch animation
            if self.playerIndex2 >= 5:  # playerSearch has 5 frames
                self.playerIndex2 = 4  # Reset to the first frame
            self.playerAnim2 = self.playerImage2.get_image(self.playerIndex2, 70, 120, 1, BLACK)
            self.playerIndex2 += 1
            player_rect = self.playerAnim2.get_rect(center=(WIN_WIDTH / 2, 100))
            self.screen.blit(self.playerAnim2, player_rect)

    def play(self):
        """Main scene rendering loop."""
        if not pg.get_init():
            return  # Pygame is quit, exit the method to prevent further actions

        # Clear the screen and set up the scene elements
        self.screen.fill(BLACK)

        # Handle player animation
        self.playerAnimation()

        # Update the dialogue system to render text
        self.dialogue_system.update()
        self.clock.tick(self.FPS)
        
        # Update the display after drawing
        pg.display.flip()

    def main2(self):
        self.event()  # Handle events
        self.play()  # Render the scene

        # Limit frame rate
        self.clock.tick(self.FPS)

    def event(self):
        """Event handling for this scene."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.scene1Playing = False  # Stop the scene loop
                #Quit Game
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if self.counter == 2:
                        self.scene1Playing = False
                    self.dialogue_system.display_next_dialogue()  # Display next dialogue when space is pressed
                    self.isSpace = True  # Change the flag to play playerSearch animation
                    self.counter += 1
