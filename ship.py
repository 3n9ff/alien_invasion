import pygame

class Ship:
    """Define ship behavior"""

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

    #Load the ship image and get its rect
        image = pygame.image.load('imagenes/nave.bmp')
        self.image = pygame.transform.scale(image, (80, 68))
        self.rect = self.image.get_rect()
        #start all the ships at the bottom center

        self.rect.midbottom = self.screen_rect.midbottom

    def blitime(self):
        """Draw the ship as its curretn location"""
        self.screen.blit(self.image, self.rect)

