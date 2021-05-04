class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize the game's settings"""
        #screen settings

        self.screen_height = 730
        self.screen_width = 1200
        self.bg_colors = (25, 25, 112 )

        #ship settings
        self.ship_speed_x = 1.5
        self.ship_speed_y = 0.9125