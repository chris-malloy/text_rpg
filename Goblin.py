from Bad_Guy import Bad_Guy

# Make Goblin a sublcass of Character
class Goblin(Bad_Guy):
	def __init__(self):
		# super allows you to access attributes and methods from the Character class
		super(Goblin,self).__init__('Goblin',6,2)
		# self.name = "Goblin"
		# self.health = 6
		# self.power = 2
		self.art =            """,      ,
					            "/(.-""-.)\
					        |\  \/      \/  /|
					        | \ / =.  .= \ / |
					        \( \   o\/o   / )/
					         \_, '-/  \-' ,_/
					           /   \__/   \
					           \ \__/\__/ /
					         ___\ \|--|/ /___
					       /`    \      /    `\
					      /       '----'       \""""
	# def take_damage(self,amount_of_damage):
	# 	self.health -= amount_of_damage
	# def get_health(self):
	# 	reutnr self.health
	# def is_alive(self):
	# 	 will return True if this statement is True, and False otherwise
	# 	return self.health > 0
	def do_a_dance(self):
		print "The goblin has done a dance. You are mezmerized and stupified, but not hurt."
	def __repr__(self):
			return "%s \n %s" % (self.name, self.art)