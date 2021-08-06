import sys

import pygame

import time

from pygame.constants import FULLSCREEN

from settings import Settings 

from ship import Ship

from bullet import  Bullet

from aliens import Alien

from game_stats import Gamestats

from buttons import Startbutton

class AlienInvasion:
    """Overall vlass to manage assets an behavior"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()

        self.settings = Settings()

        #Crear ventama
        self.screen = pygame.display.set_mode((0,0), FULLSCREEN)
        pygame.display.set_caption("alien Invasion")

        self.screen_rect = self.screen.get_rect()

        #wifth and height
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        #indicar los colores
        self.bg_colors = (self.settings.bg_colors)

        #set the statistics of the game
        self.statistics = Gamestats(self.settings)

        #Button classes
        self.start_button = Startbutton(self)

        #Call characters class
        self.ship = Ship(self)        

        #Make a group that manage all bullets
        self.bullets = pygame.sprite.Group()

        #Make a group that manage all aliens and set them
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #Loop flag
        self.active = True
            
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
                
    def _check_keyup(self, event):
        """Check for keydown events"""

        if event.key == pygame.K_d:
            self.ship.movment_right = False

        if event.key == pygame.K_a:
            self.ship.movment_left = False 
    
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
        number_lines = 3

        for line in range(number_lines):

            for alien_number in range(number_aliens_x):
                self._create_alien(line, alien_number)

    def _alien_movement(self):
        """Control the movment of the aliens"""

        #Use the fuction to move the aliens        
        self.aliens.update()

        #Check the position to move properly the fleet
        self._check_fleet_direction()

    def _check_alien_bullet_col(self):

        collider = pygame.sprite.groupcollide(self.aliens, self.bullets, True, True)

        if collider:

            self._alien_shoted_down()

    def _alien_shoted_down(self):
        """What happend when an alien is shoted down"""

        self._create_new_feet()

        self.statistics.player_points += 5

    def _check_ship_alien_colliders(self):
        """ Check ship-alien collisions"""

        ship_alien_colider = pygame.sprite.spritecollideany(self.ship, self.aliens)

        if ship_alien_colider:

            self._ship_hit()
    
    def _check_alien_reach_bottom(self):
        """Check if an alien reach the bottom"""

        for alien in self.aliens:
            if alien.rect.bottom >= self.screen_rect.bottom:

                self._ship_hit()

                break

    def _ship_hit(self):
        """says what happend when the ship collide or a alien reach the bottom"""

        #substract a live
        self.statistics.ship_lives_left -= 1

        #empty the screen
        self.aliens.empty()
        self.bullets.empty()

        #move the alien to the center
        self.ship.x = self.screen_rect.centerx

        #Create a new seep
        self._create_fleet()

        #pause time
        time.sleep(0.5)

        #End game
        if self.statistics.ship_lives_left == 0:

            self.active = False

    def _check_fleet_direction(self):
        """Check if any alien has reached the edge"""
        for alien in self.aliens:
            if alien.check_edges():
                self._change_direction()
                
                break

    def _change_direction(self):
        """Change the direction of the fleet and """

        self.settings.alien_direction *= -1

        for alien in self.aliens:
            alien.rect.y += self.settings.alien_drop_down
         
    def _fire_bullet(self):
        """shot the bullets"""

        if len(self.bullets) < self.settings.bullet_loader:

            #Make a new bullet
            new_bullet = Bullet(self)

            #Add the bullets to the group
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """Update bullets position and deleat the from the sprites list"""

        self.bullets.update()
        for bullet in self.bullets:
            #Eliminar las balas si salen de la pantalla
            if bullet.rect.y == 0:
                self.bullets.remove(bullet)
        self._check_alien_bullet_col()
    
    def _create_new_feet(self):

        #Check if all the fleet has been shoted down
        if len(self.aliens) == 0:

            #Delete all bullets on the screen
            self.bullets.empty()

            #Create another fleet
            self._create_fleet()

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
        #TAMBIEN CURRA X AKIIII
        if not self.active:
            self.start_button.draw_button()


    def run_game(self):
        """start the main loop for the game"""
        
        while True:   

            #respond to events
            self._check_events()

            while self.active:

                #Update ship position
                self.ship.upadate_movement()

                #Update bullets position
                self._update_bullet()

                #Update aliens position
                self._alien_movement()

                #Colliders
                self._check_ship_alien_colliders()
                self._check_alien_reach_bottom()

                #Update the grafics
                self._update_screen()

                break

if __name__ == '__main__':

    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()