import sys

import pygame
from pygame.constants import RESIZABLE

from settings import Settings 

from ship import Ship

from bullet import Bullet

from aliens import Alien

class AlienInvasion:
    """Overall vlass to manage assets an behavior"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()

        self.settings = Settings()

        #Crear ventama
        self.screen = pygame.display.set_mode((1100,700), RESIZABLE)
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

        #Make a group that manage all aliens and set them
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
            
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

        if event.key == pygame.K_d:
            self.ship.movment_right = True
                
        if event.key == pygame.K_a:
            self.ship.movment_left = True

        if event.key == pygame.K_w:
            self.ship.movement_up = True

        if event.key == pygame.K_s:
            self.ship.movement_down = True
                
    def _check_keyup(self, event):
        """Check for keydown events"""

        if event.key == pygame.K_d:
            self.ship.movment_right = False

        if event.key == pygame.K_a:
            self.ship.movment_left = False 

        if event.key == pygame.K_w:
            self.ship.movement_up = False

        if event.key == pygame.K_s:
            self.ship.movement_down = False
    
    def _create_alien(self, line, alien_number):
        """Create an alien"""
        alien = Alien( self )
        alien_width, alien_height = alien.rect.size
        
        #Set y data
        alien.y = alien_height + 2 * alien_height * line 
        alien.rect.y = alien.y
        #set x data
        alien.x = alien_width // 2 +  alien_width * alien_number * 1.5
        alien.rect.x = alien.x
        #add aliens to sprite to be drawn
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create a fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        #Calculates the x parameters
        number_aliens_x = 9
        #Calculates the y parameters
        aviliable_space = self.screen_height - (3 * alien.rect.y)
        number_lines = aviliable_space // (alien_height * 2)

        for line in range(number_lines):

            for alien_number in range(number_aliens_x):
                self._create_alien(line, alien_number)

    def _alien_movement(self):
        """Control the movment of the aliens"""

        #Use the fuction to move the aliens        
        self.aliens.update()

        #Cgange the direction and move down the aliens when touch 
        #the edge of the screen
        self._change_alien_direction()

    def _change_alien_direction(self):
        """Change the alien direction and go dawn the alien"""

        for alien in self.aliens:

            if alien.rect.x == 0:

                self.settings.alien_down = True
                self.settings.alien_direction = -1
            
            if alien.rect.x == 1270:

                self.settings.alien_down = True
                self.settings.alien_direction = 1
                
                
    def _fire_bullet(self):
        """shot the bullets"""

        if len(self.bullets) < 3:

            #Make a new bullet
            new_bullet = Bullet(self)

            #Add the bullets to the group
            self.bullets.add(new_bullet)
        
        else:
            pass

    def _update_bullet(self):
        """Update bullets position and deleat the from the sprites list"""

        self.bullets.update()
        for bullet in self.bullets:
            #Eliminar las balas si salen de la pantalla
            if bullet.rect.y == 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """ Update the screen all the time"""

        #Display background color
        self.screen.fill(self.bg_colors)

        #Draw the ship
        self.ship.blitime()

        #Draw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #Draw the aliens
        self.aliens.draw(self.screen)

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
            self._update_bullet()

            #Update aliens position
            self._alien_movement()

            #Update the grafics
            self._update_screen()



if __name__ == '__main__':

    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()