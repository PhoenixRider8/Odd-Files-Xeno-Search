from ..spritesheet.spriteList import *
from ..spritesheet.SpritesheetImport import SpriteSheet
from ..config import *
import pygame as pg
import sys
from ..dialogue.dialogueSys import DialogueSystem

class Scene1:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.counter = 0

        #Animation index
        self.playerIndex1 = 0
        self.playerIndex2 = 0
        self.jokerIndex = 0

        # Load player sprite sheet and joker sprite sheet
        self.playerUp = pg.image.load(playerGetUp).convert_alpha()
        self.playerImage = SpriteSheet(self.playerUp)
        self.playerAnim1 = self.playerImage.get_image(0, 128, 147, 1, BLACK)

        self.joker = pg.image.load(jokerSmile).convert_alpha()  # Assuming Joker uses the same sprite sheet
        self.jokerImage = SpriteSheet(self.joker)
        self.jokerAnim = self.jokerImage.get_image(0, 128, 147, 1, BLACK)

        self.scene1Playing = True
        self.isSpace = False
        self.FPS = 5

        # Dialogue system
        self.dialogue_system = DialogueSystem(self.screen, FONT)
        self.dialogue_system.change_font_size(25)
        self.setDialogue1()

    def setDialogue1(self):
        """Set up initial dialogues."""
        self.dialogue_system.add_dialogue("Xeno", "uhh.. ")
        self.dialogue_system.add_dialogue("Xeno", "huh?!")
        self.dialogue_system.add_dialogue("Xeno", "where am I? ")
        self.dialogue_system.add_dialogue("Joker", "Greetings, traveler.")
        self.dialogue_system.add_dialogue("Xeno", "What is this place?!")
        self.dialogue_system.add_dialogue("Joker", "You are trapped here.")
        self.dialogue_system.add_dialogue("Xeno", "Trapped?!")
        self.dialogue_system.add_dialogue("Xeno", "What do I do to get out? ")

    def playerAnimation(self):
        # Draw player sprite (for now using playerAnim1 as an example)
        
        # Increment the index but loop it between 2 and 3
        if self.playerIndex1 < 3 and self.isSpace:
            self.playerIndex1 += 1
        elif self.playerIndex1 >= 3:
            self.playerIndex1 = 2  # Reset to 2 when reaching 3

        
        player_rect = self.playerAnim1.get_rect(center=(400, 300))  # Place player in center    
        self.playerAnim1 = self.playerImage.get_image(self.playerIndex1, 128, 147, 1, BLACK) 
        self.screen.blit(self.playerAnim1, player_rect)

    def jokerAnimation(self):
        # Draw the Joker sprite
        if(self.jokerIndex>2):
            self.jokerIndex=0
        else:
            self.jokerAnim = self.jokerImage.get_image(self.jokerIndex, 128,128, 1 , BLACK)
            self.jokerIndex+=1
        joker_rect = self.jokerAnim.get_rect(center=(WIN_WIDTH/2, 100))  # Position Joker at another spot
        self.screen.blit(self.jokerAnim, joker_rect)

    def play(self):
        """Main scene rendering loop."""
        # Ensure that the display surface is still available (not quit)
        if not pg.get_init():
            return  # Pygame is quit, exit the method to prevent further actions

        # Clear the screen and set up the scene elements
        self.screen.fill(BLACK)

        self.playerAnimation()
        

        self.jokerAnimation()

        # Update the dialogue system to render text
        self.dialogue_system.update()
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
                    if self.counter==8:
                        self.scene1Playing = False
                        
                    self.dialogue_system.display_next_dialogue()  # Display next dialogue when space is pressed
                    self.isSpace = True
                    self.counter +=1
