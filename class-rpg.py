# Contrib modules
# Core
import os
from random import randint
# 3rd party
# pygame for instance here

# Custom modules
from Good_Guy import Good_Guy
from Bad_Guy import Bad_Guy
from Battle import Battle
from Store import Store
from Hero import Hero
from Medic import Medic
from Goblin import Goblin
from Vampire import Vampire
from Dragon import Dragon


# instantiate a hero object from the Hero class
hero = Hero("Chris")
medic = "Gill"
goblin = Goblin()

# make a list to hold all our monsters
monsters = []

# Before the game starts, let's ask the hero for his or her name.
print "What is thy name, brave adventurer?"
hero_name = raw_input("> ")
# hero.cheer_for_hero()

print "How many monsters are you willing to fight, brave %s?" % hero.name
number_of_enemies = int(raw_input("> "))

# print "And where shall you be taking your adventure?"
# location = raw_input("Choose 'Cave'\n>")

for i in range(0, number_of_enemies):
	rand_num = randint(0,2)
	if (rand_num == 1):
		monsters.append(Goblin())
	elif (rand_num == 2):
		monsters.append(Vampire())
	else:
		monsters.append(Dragon())



for i,monster in enumerate(monsters):
	# Run the game as long as BOTH characters have health (are alive)
	while monster.is_alive() and hero.is_alive():
		# game is on!
		os.system("clear")
		print "You have %d health and %d power." % (hero.health,hero.power)
		print "The %s has %d health and %d power." % (monster.name,monster.health,monster.power)
		print "What do you want to do?"
		print "1. fight %s" % monsters
		print "2. Heal Hero"
		print "3. Heal Medic"
	 	print "2. do nothing"
	 	print "4. flee"
	 	print "> "
	 	user_input = raw_input()
	 	if user_input == "1":
	 		# User has chosen to attack.
	 		# Take away health from the goblin based on hero power
	 		# the goblin class should be managing the goblins health
	 		# the hero is going to do hero.power damage to the goblin
	 		attack_damage = hero.get_attack_power(monster)
	 		print attack_damage
	 		monster.take_damage(attack_damage)
	 	elif user_input == "2":
	 		if hero.health < Good_Guy:
	 			medic.heal_other(hero.health)
	 		else:
	 			"Hero at full health.:"
	 	elif user_input == "3":
	 		if Medic.health < Good_Guy.health:
	 			medic.heal()
	 		else: 
	 			"Medic at full health."
		elif user_input == "4":
	 		# Hero is going to stand there like an idiot
	 		pass
	 	elif user_input == "5":
	 		print "Goodbye, coward! You remind me of Goober."
	 		os.system("say Goodbye, coward! You remind me of Goober.")
	 		break
	 	else:
	 		print "Invalid input %s" % user_input
	 

	 	# goblins turn to attack!! (only if he's still alive)
	 	if goblin.health > 0:
	 		# just like the goblin, the hero should be changing its own stuff
	 		# so... clas take_damage on the hero
	 		# hero.health -= goblin.power
	 		hero.take_damage(goblin.power)

	 		print "The goblin hits you for %d damage" % goblin.power
	 		# goblin has attacked, now check to see if hero is still alive...
	 		if hero.health <=0:
	 			print "You have died just like that one time in Dark Souls"
	 			# os.system("say You have been killed by the weak goblin, shame on you.")








