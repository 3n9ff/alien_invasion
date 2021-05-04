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

        #Crear ventama
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("alien Invasion")

        #indicar los colores
        self.bg_colors = (self.settings.bg_colors)

        #call the ship
        self.ship = Ship(self)
        
    def _check_events(self):
        """ Respond to keypress and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()     

            #comprueva si se presiona una tecla
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    self.ship.movment_right = True
                
                if event.key == pygame.K_LEFT:
                    self.ship.movment_left = True

                if event.key == pygame.K_UP:
                    self.ship.movement_up = True

                if event.key == pygame.K_DOWN:
                    self.ship.movement_down = True
                

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT:
                    self.ship.movment_right = False

                if event.key == pygame.K_LEFT:
                    self.ship.movment_left = False 

                if event.key == pygame.K_UP:
                    self.ship.movement_up = False

                if event.key == pygame.K_DOWN:
                    self.ship.movement_down = False  

    def _update_screen(self):
        """ Update the screen all the time"""

        #Display background color
        self.screen.fill(self.bg_colors)

        #Draw the ship
        self.ship.blitime()

        #Make the most recently draw screen visible
        pygame.display.flip()

    def run_game(self):
        """start the main loop for the game"""
        while True:

            #respond to events
            self._check_events()

            #Update the grafics
            self._update_screen()

            #Update ship position
            self.ship.upadate_movement()
        

if __name__ == '__main__':

    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()