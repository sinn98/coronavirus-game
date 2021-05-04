class Settings():
	"""A class to store all settings for Alien Invasion."""
	
	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 900
		self.screen_height = 600
		self.bg_colour = (140, 180, 230)
		
		# Bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_colour = 60, 60, 60
		self.bullets_allowed = 3
		
		# Ship settings
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		
		# Alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
		
