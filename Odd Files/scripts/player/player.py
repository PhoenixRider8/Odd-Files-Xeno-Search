import pygame as pg
from ..config import *
from ..spritesheet.spriteList import *
from ..spritesheet.SpritesheetImport import SpriteSheet

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        # changes in player
        self.x_change = 0
        self.y_change = 0
        self.facing = 'down'

        # player sprites
        self.playerIdle = pg.image.load(player_up).convert_alpha()
        self.playerImage = SpriteSheet(self.playerIdle)
        self.playerAnim = self.playerImage.get_image(0, 64, 120, 1, BLACK)

        self.index = 0
        self.animation_timer = 0  # Timer for frame control

        # HITBOX of Player
        self.rect = self.playerIdle.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        # UPDATE player movement and hitbox
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        # Reset x and y change
        self.x_change = 0
        self.y_change = 0

        # Update the animation based on the current state (idle or moving)
        self.animate_idle()

    def movement(self):
        self.keys = pg.key.get_pressed()  # list of keys pressed

        if self.keys[pg.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = 'left'
        elif self.keys[pg.K_a]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'right'
        elif self.keys[pg.K_w]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        elif self.keys[pg.K_s]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    def animate_idle(self):
        # If no keys are pressed, update the idle animation
        if self.x_change == 0 and self.y_change == 0:
            self.animation_timer += 1

            # Switch animation frame every 10 frames (you can adjust this number)
            if self.animation_timer >= 10:
                self.animation_timer = 0
                self.index = 1 if self.index == 0 else 0  # Toggle between 0 and 1

            # Update the animation based on the index
            self.playerAnim = self.playerImage.get_image(self.index, 64, 120, 1, BLACK)
