import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Cointains the overall information about fullets"""

    def __init__(self, ai_game):

        #Ocerall data
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bullet_color = self.settings.bullet_color
        self.ship = ai_game.ship

        super().__init__()

        #Bullet and bullet position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = self.ship.rect.midtop

        #Allows work with decimal values
        self.y = self.rect.y

    def update_bullet(self):
        """Update bullet position"""
        self.y -= self.settings.bullet_speed

    def draw_bullet(self):
        """Draw the bullet onto the screen"""

        pygame.draw.rect(self.screen, self.bullet_color , self.rect)

        
