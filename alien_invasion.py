import sys

import pygame

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

        #Make a group that manage all aliens
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
        
    def _create_fleet(self):
        """Create a fleet of aliens"""
        alien = Alien(self)
        alien_width = alien.rect.width
        number_aliens_x = self.screen_width // alien_width 
        print(number_aliens_x)

        for alien_number in range(number_aliens_x):
            alien = Alien(self)
            alien.x = alien_width // 2 +  alien_width * alien_number * 1.5
            alien.rect.x = alien.x
            self.aliens.add(alien)
        

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

            #Update the grafics
            self._update_screen()



if __name__ == '__main__':

    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()