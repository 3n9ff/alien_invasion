import pygame

class Startbutton:
    """Create all the butons"""
    
    def __init__(self, ai_game):
        pygame.init()

        #windows info
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Text info
        self.msg = "star"
        self.txcolor = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 50)
        self.position = self.screen_rect.center
        self.txrender = self.font.render( self.msg, True, self.txcolor)
        self.txdimenisons = self.txrender.get_rect()

        #Rect info
        self.reccolor = (0,0,0)        
        self.rect = ((self.position), (self.txdimenisons))
    #TRABAJA X AKI, NO FUNCIONA

    def draw_button(self):
        """Draw the start button"""
        #Display the text
        pygame.Surface.blit(self.position, self.txrender)

        #Display the rect
        pygame.draw.rect(self.position, self.reccolor, self.rect, border_radius=10)

