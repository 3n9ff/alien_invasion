import pygame

class Ship:
    """Define ship behavior"""

    def __init__(self, ai_game):

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
     
    def upadate_movement(self):
        """Update ship position besed on the flags"""
        if self.movment_right:
            self.rect.x += 1

        elif self.movment_left:
            self.rect.x -= 1
        
        elif self.movement_up:
            self.rect.y -= 1

        elif self.movement_down:
            self.rect.y += 1

    def blitime(self):
        """Draw the ship as its curretn location"""
        self.screen.blit(self.image, self.rect)

