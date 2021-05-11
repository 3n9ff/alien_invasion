import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """Manage the overall about aliens"""

    def __init__(self, main_game):

        super().__init__()
        self.screen = main_game.screen

        #Alien info
        image = pygame.image.load('imagenes/nave.png')
        self.image = pygame.transform.scale(self.screen, (100, 100))
        self.rect = self.image.get_rect()

        #Initial position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store aliens original position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)



