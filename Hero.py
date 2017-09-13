class Hero(object):
	def __init__(self, name = "Incognito"):
		# set up the object ot remember it's name
		self.name = name
		self.health = 10
		self.power = 6
	def take_damage(self,amount_of_damage):
		self.health -= amount_of_damagex
	def cheer_for_hero(self):
		print "Fight hard, valiant %s" % self.name
	def is_alive(self):
		# will return True if this statement is True, and False otherwise
		return self.health > 0
