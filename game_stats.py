class Gamestats:
    """manage all the statistics"""

    def __init__(self, settings):

        self.settings = settings
        self.ship_lives_left = self.settings.ship_lives
        self.player_points = 0

    def reset_stats(self):
        
        self.ship_lives_left = self.settings.ship_lives
        self.player_points = 0