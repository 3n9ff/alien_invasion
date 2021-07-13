import pygame

from pygame.sprite import Sprite
from pygame.transform import chop

from settings import Settings

class Alien(Sprite):
    """Manage the overall about aliens"""

    def __init__(self, main_game):

        super().__init__()
        self.screen = main_game.screen
        self.aliens = main_game.aliens
        self.settings = main_game.settings
        

        #Alien info
        image = pygame.image.load('imagenes/alien.png')
        self.image = pygame.transform.scale(image, (100, 65))
        self.rect = self.image.get_rect()

        #Initial position/ alien position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height * 0.75

        #Store aliens original position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Manage the movement of the ovnis"""

        #Control the x movement
        self.x -= (self.settings.alien_speed * self.settings.alien_direction)

        self.rect.x = self.x

        #control the y movemen
        if self.settings.alien_down:
            
            self.y += self.settings.alien_movement_down

            self.rect.y = self.y
            
            self.settings.alien_down = False

            
            