import pygame

class LivesIndicator:
    """Drae on the screen how many lives are left"""

    def __init__(self,ai_game):

        #Sats
        self.lives = ai_game.statistics.ship_lives_left

        #screen info
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #image 
        image = pygame.image.load('imagenes/nave.png')
        self.image = pygame.transform.scale(image, (67,57))
        self.image_rect = self.image.get_rect()

        #image position
        self.image_width = self.image_rect.width


    def draw_lives(self):
        """Blit the lives"""

        for live in range(self.lives):

            self.position_x = (self.image_width + 5) * live

            self.screen.blit(self.image, (self.position_x, 20))
