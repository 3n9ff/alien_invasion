import sys

import pygame

from settings import Settings 

from ship import Ship

class AlienInvasion:
    """Overall vlass to manage assets an behavior"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("alien Invasion")

        #indicar los colores
        self.bg_colors = (self.settings.bg_colors)

        #call the ship
        self.ship = Ship(self)
        
    def run_game(self):
        """start the main loop for the game"""
        while True:
            #watch for a keyboard and mous events"""

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Display background color
            self.screen.fill(self.bg_colors)

            #Draw the ship
            self.ship.blitime()

        #Make the most recently draw screen visible
            pygame.display.flip()
if __name__ == '__main__':

    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
    
            
        