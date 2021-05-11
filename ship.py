import pygame

from settings import Settings

class Ship:
    """Define ship behavior"""

    def __init__(self, ai_game):

        #call main data
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        image = pygame.image.load('imagenes/nave.png')
        self.image = pygame.transform.scale(image, (80, 68))
        self.rect = self.image.get_rect()

        #start all the ships at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        #Moviment flag
        self.movment_right = False

        self.movment_left = False

        self.movement_up = False

        self.movement_down = False

        #Call settings
        self.setting = Settings()

        #Allow handel floats
        self.x = float(self.rect.x)
        self.y = float(self.rect.y) 
     
    def upadate_movement(self):
        """Update ship position besed on the flags"""
        if (self.movment_right) and (self.x < 1300):
            self.x += self.setting.ship_speed_x

        if (self.movment_left) and (self.x > 0):
            self.x -= self.setting.ship_speed_x
        
        if (self.movement_up) and (self.y > 0):
            self.y -= self.setting.ship_speed_y

        if (self.movement_down) and (self.y < 730):
            self.y += self.setting.ship_speed_y

        #return the original variable name
        self.rect.x = self.x
        self.rect.y = self.y


    def blitime(self):
        """Draw the ship as its curretn location"""
        self.screen.blit(self.image, self.rect)