# This is our super (parent) class. All other characers, will be subclasses of this class
class Bad_Guy(object):
	def __init__(self,name,health,power):
		self.name = name
		self.health = health
		self.power = power
	def take_damage(self,amount_of_damage):
		self.health -= amount_of_damage
	def get_health(self):
		return self.health
	def is_alive(self):
		return self.health > 0
	def is_alive(self):
		# will return True if this statement is True, and False otherwise
		return self.health > 0
	def attack(self,Good_Guy):
		for i in range(0,5):
			rand_num = randint(0,5)
			if rand_num == 1:
				self.power * 2
				print "%s lands a critical strike on %s!" % (self.name,enemy.name)
			else:
				self.power = self.power
				print "%s attacks %s" % (self.name, enemy.name)
	def receive_damage(self, points):
		self.health -= points
		print "%s received %d damage." % (self.name, points)
		if self.health <= 0:
			print "YOU HAVE DIED"
	def print_status(self):
		print "%s has %d health and %d power." % (self.name, self.health, self.power)
