class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize the game's settings"""
        #screen settings
        self.bg_colors = (25, 25, 112 )

        #ship settings
        self.ship_speed_x = 1.5
        self.ship_speed_y = 0.9

        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 7.5
        self.bullet_speed = 3
        self.bullet_loader = 6
        self.bullet_color = (192, 192, 192)

        #Alien speed
        self.alien_speed = 0.5
        self.alien_drop_down = 5
        self.alien_direction = -1