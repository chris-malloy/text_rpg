from random import randint
class Store(object):
	def __init__(self, weapons, armor, potions, spells):
		self.weapons = ["Axe", "Sword", "Bow"]
		self.amor = ["Sheild", "Iron Brestplate", "Leather Chestpiece"]
		self.potions = ["Health Potion", "Power Potion", "Mana Potion"]
		self.spells = ["Fire Spell", "Weakening Spell", "Power Spell"]
	def give_weapon(self, weapon_type):
		for i in range(0, weapon_type):
			rand_num = randint(0,len(weapons))

class Weapon(Store):
	def __init__(self):
		self.weapon = weapon


