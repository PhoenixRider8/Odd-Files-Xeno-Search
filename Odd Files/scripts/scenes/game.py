#import classes and functions
import pygame as pg
import sys

from scripts.config import *
from scripts.mainmenu.menu import *
from scripts.player.player import *
from scripts.dialogue.dialogueSys import DialogueSystem
from scripts.automate.folder import FolderOpen

from scripts.enemies.virus import Virus
from scripts.dialogue.timerMin import Timer

class Game(MainMenu):
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.canvas = pg.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(FONT, 32)  # Set font

        self.running = False
        self.menuRunning = True
        self.playing = False

        self.dialogue_system = DialogueSystem(self.screen, FONT)
        self.dialogue_system.change_font_size(25)
        self.setDialogue1()

        self.folder = FolderOpen() 
        self.counter = 0
        
    '''------------------------------------------------------------------------------------------------------------------------'''
    def setDialogue1(self):
        """Set up initial dialogues."""
        self.dialogue_system.add_dialogue("Virus", "in fileDel ")
        self.dialogue_system.add_dialogue("Virus", "open task.txt")
        self.dialogue_system.add_dialogue("Xeno", "TIME TO SEARCH! ")

    def new(self):
        """Start a new game."""
        self.playing = True
        # Objects containing all sprites in the game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.blocks = pg.sprite.LayeredUpdates()
        self.enemies = pg.sprite.LayeredUpdates()
        self.attacks = pg.sprite.LayeredUpdates()

        self.player = Player(self, 2, 2)  # Positioned at (32, 64)
        self.virus = Virus(100, 100, 128, 128, 2, (0, 0, 0))

        self.virus_sprites = pygame.sprite.Group()
        self.virus_sprites.add(self.virus)

    def events(self):
        """Event loop for the game."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if self.counter==1:
                        self.folder.open_folder('filesDel') 
                        self.playing = False
                        self.running = False
                    self.dialogue_system.display_next_dialogue()  # Display next dialogue when space is pressed
                    self.isSpace = True
                    self.counter +=1
                    #print(self.counter)

    def update(self):
        """Update all sprite objects."""
        self.all_sprites.update()
        self.dt = self.clock.tick(60) / 1000  # Delta time in seconds

    def draw(self):
        """Draw the game elements to the screen."""
        self.virus_sprites.update(self.dt)
        self.screen.fill(BLACK)
        self.screen.blit(self.player.playerAnim, (WIN_WIDTH/2, WIN_HEIGHT / 2))
        self.virus_sprites.draw(self.screen)

        self.clock.tick(FPS)

        self.dialogue_system.update()
        
        pg.display.update()  # Update pygame screen
        

    def main(self):
        """Main game loop."""
        #play
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False


    '''-----------------------------------------------------------------------------------------------------------------------'''

    # MAIN MENU
    def events2(self):
        """Event loop for the menu."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.menuRunning = False
                self.playing = True
                

    def drawMenu(self):
        """Draw the menu elements to the screen."""
        self.screen.fill(BLACK)
        self.screen.blit(self.title_screen, (0,0))
        self.screen.blit(self.startButton, (WIN_WIDTH / 2 - self.startButton.get_width() / 2, WIN_HEIGHT / 2 - 50))
        self.screen.blit(self.quitButton, (WIN_WIDTH / 2 - self.quitButton.get_width() / 2, WIN_HEIGHT / 2 + 50))
        self.clock.tick(FPS)
        pg.display.update()  # Update pygame screen

    def menu(self):
        """Menu loop."""
        self.events2()
        self.drawMenu()

    def start_game(self):
        """Start the game when the start button is clicked."""
        self.menuRunning = False  # Exit the menu loop
        self.new()

    def quit_game(self):
        """Quit the game when the quit button is clicked."""
        pg.quit()
        sys.exit()

    def handle_menu_clicks(self):
        """Detect button clicks and handle actions."""
        mouse_pos = pg.mouse.get_pos()
        mouse_pressed = pg.mouse.get_pressed()

        if self.start_button_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            self.start_game()
        elif self.quit_button_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            self.quit_game()
