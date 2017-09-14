from Bad_Guy import Bad_Guy

class Vampire(Bad_Guy):
	def __init__(self):
		super(Vampire,self).__init__('Vampire',6,2)
	# 	self.name = "Vampire"
	# 	self.health = 6
	# 	self.power = 2
	# def take_damage(self,amount_of_damage):
	# 	self.health -= amount_of_damage
	# def is_alive(self):
	# 	# will return True if this statement is True, and False otherwise
	# 	return self.health > 0
	def death_stare(self):
		print "The vampire freezes your blood with his deaht stare."
	def __repr__(self):
			return "%s" % (self.name)