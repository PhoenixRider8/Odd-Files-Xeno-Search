import pygame
from ..config import *
from ..spritesheet.spriteList import *
from ..spritesheet.SpritesheetImport import SpriteSheet

# Virus class using SpriteSheet
class Virus(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, scale, colour):
        super().__init__()
        self.virusImg = pygame.image.load(virus_idle).convert_alpha()

        self.sprite_sheet = SpriteSheet(self.virusImg)
        self.width = width
        self.height = height
        self.scale = scale
        self.colour = colour
        self.frames = [self.sprite_sheet.get_image(0, width, height, scale, colour),
                       self.sprite_sheet.get_image(1, width, height, scale, colour)]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.animation_speed = 0.1  # Speed of frame change
        self.time = 0

    def update(self, dt):
        # Handle animation frame change based on time
        self.time += dt
        if self.time >= self.animation_speed:
            self.time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]


#IMPORTANT UPDATES:
'''
in __init__():
self.virus = Virus(100, 100, 128, 128, 2, (0, 0, 0))
self.virus_sprites = pygame.sprite.Group()
self.virus_sprites.add(self.virus)

in update():
self.dt = self.clock.tick(60) / 1000  # Delta time in seconds

in draw():
self.virus_sprites.update(self.dt)
self.screen.fill(BLACK)

self.virus_sprites.draw(self.screen)
'''