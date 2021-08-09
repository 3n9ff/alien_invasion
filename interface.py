import pygame
from pygame.sprite import Sprite

class Button:
    """Create all the butons"""
    
    def __init__(self, ai_game, msg, letter_size = 50):

        #windows info
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Text info
        self.txcolor = (0, 255, 0)
        self.font = pygame.font.SysFont(None, letter_size)
        self.txrender = self.font.render( msg, True, self.txcolor, (0,0,0))

        #text rect info
        self.txrect = self.txrender.get_rect()
        self.txrect.centerx = self.screen_rect.centerx
        self.txrect.centery = self.screen_rect.centery

        #Rect info
        self.reccolor = (0,0,0) 
        self.rectangulo = pygame.draw.rect(self.screen, self.reccolor, self.txrect, border_radius=10)       

    def draw_button(self):
        """Draw the start button"""

        #Display the text
        self.screen.blit(self.txrender, self.txrect)

class ScoreBoard:
    """Create a scoreboard by inputing the score"""

    def __init__(self, ai_game, stats , font):

        #Screen info
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Text info
        self.score = str(stats)
        self.font = pygame.font.SysFont(None, font)
        self.text = self.font.render(self.score, True, (0, 0, 0))
        self.txrect = self.text.get_rect()

        #txrect data
        self.rect = pygame.Rect(self.txrect)
        pygame.draw.rect(self.screen, (25, 25, 112), self.rect)

    def _show_scoreboard(self):
        """Draw the scoreboard onto the screen, 
        change the self.txrect value to set the position"""

        #Set the position
        self.x, self.y = self.txrect.x, self.txrect.y + 20

        #draw
        self.screen.blit(self.text, (self.x, self.y))   

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
