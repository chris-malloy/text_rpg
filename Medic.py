from Good_Guy import Good_Guy
from random import randint

class Medic(Good_Guy):
	def __init__(self):
		super(Medic,self).__init__(name,10,10)
		self.name = "Medic"
	def heal(self):
		self.health += self.power
	def heal_other(self):
		health += (self.power / 2)


