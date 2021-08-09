import pygame
from pygame.sprite import Sprite

class LivesIndicator(Sprite):
    """Drae on the screen how many lives are left"""

    def __init__(self,ai_game):

        super().__init__()

        #screen info
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #image 
        image = pygame.image.load('imagenes/nave.png')
        self.image = pygame.transform.scale(image, (67,57))
        self.rect = self.image.get_rect()

        #image position
        self.image_width = self.rect.width




