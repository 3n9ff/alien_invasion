class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize the game's settings"""
        #screen settings
        self.bg_colors = (25, 25, 112)

        #ship settings
        self.ship_speed_x = 4.5
        self.ship_lives = 3

        #Bullet settings
        self.bullet_width = 4
        self.bullet_height = 7.5
        self.bullet_speed = 8.5
        self.bullet_loader = 3
        self.bullet_color = (192, 192, 192)

        #Alien speed
        self.alien_speed_o = 0.5

        self.alien_drop_down = 15
        self.alien_direction = -1
        
        #Puntuation
        self.alien_reached_o = 5
        self.round_passed_o = 200

        #Multiplicators
        self.speed_increase = 1.35

        #dynamics

        self.alien_reached = 5
        self.round_passed = 200       
        self.alien_speed = 0.5 * 10

        