import sys

import pygame

from settings import Settings 

from ship import Ship

from bullet import Bullet

class AlienInvasion:
    """Overall vlass to manage assets an behavior"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()

        self.settings = Settings()

        #Crear ventama
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("alien Invasion")

        self.screen_rect = self.screen.get_rect()

        #wifth and height
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        #indicar los colores
        self.bg_colors = (self.settings.bg_colors)

        #Call characters class
        self.ship = Ship(self)        

        #Make a group that manage all bullets
        self.bullets = pygame.sprite.Group()
        
    def _check_events(self):
        """ Respond to keypress and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()     

            #comprueva si se presiona una tecla
            elif event.type == pygame.KEYDOWN:
                
                self._check_keydown(event)

            elif event.type == pygame.KEYUP:

                self._check_keyup(event)

    def _check_keydown(self, event):
        """Check for keydown events"""

        if event.key == pygame.K_q:
            sys.exit()

        if event.key == pygame.K_SPACE:
            self._fire_bullet()

        if event.key == pygame.K_RIGHT:
            self.ship.movment_right = True
                
        if event.key == pygame.K_LEFT:
            self.ship.movment_left = True

        if event.key == pygame.K_UP:
            self.ship.movement_up = True

        if event.key == pygame.K_DOWN:
            self.ship.movement_down = True
                
    def _check_keyup(self, event):
        """Check for keydown events"""

        if event.key == pygame.K_RIGHT:
            self.ship.movment_right = False

        if event.key == pygame.K_LEFT:
            self.ship.movment_left = False 

        if event.key == pygame.K_UP:
            self.ship.movement_up = False

        if event.key == pygame.K_DOWN:
            self.ship.movement_down = False

    def _fire_bullet(self):
        """shot the bullets"""

        #Make a new bullet
        new_bullet = Bullet(self)

        #Add the bullets to the group
        self.bullets.add(new_bullet)
        

    def _update_screen(self):
        """ Update the screen all the time"""

        #Display background color
        self.screen.fill(self.bg_colors)

        #Draw the ship
        self.ship.blitime()

        #Draw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #Make the most recently draw screen visible
        pygame.display.flip()

    def run_game(self):
        """start the main loop for the game"""
        while True:

            #respond to events
            self._check_events()

            #Update ship position
            self.ship.upadate_movement()

            #Update bullets position
            self.bullets.update()
    
            #Update the grafics
            self._update_screen()


if __name__ == '__main__':

    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()