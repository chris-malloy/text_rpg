import os

from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from random import randint

# instantiate a hero object from the Hero class
hero = Hero("Chris")
# ditto
goblin = Goblin()

# make a list to hold all our monsters
monsters = []

# Before the game starts, let's ask the hero for his or her name.
print "What is thy name, brave adventurer?"
hero_name = raw_input("> ")
hero.cheer_for_hero()

print "How many monsters are you willing to fight, brave %s?" % hero.name
number_of_enemies = int(raw_input("> "))

for i in range(0, number_of_enemies):
	rand_num = randint(0,1)
	if (rand_num == 1):
		monsters.append(Goblin())
	else:
		monsters.append(Vampire())

# Run the game as long as BOTH characters have health (are alive)
while goblin.is_alive() and hero.is_alive():
	# game is on!
	# os.system("clear")
	print "You have %d health and %d power." % (hero.health, hero.power)
	print "The goblin has %d health and %d power." % (goblin.health, goblin.power)
	print "What do you want to do?"
	print "1. fight %s" % monster.name 
 	print "2. do nothing"
 	print "3. flee"
 	print "> "
 	user_input = raw_input()
 	if user_input == "1":
 		# User has chosen to attack.
 		# Take away health from the goblin based on hero power
 		# the goblin class should be managing the goblins health
 		# the hero is going to do hero.power damage to the goblin
 		goblin.take_damage(hero.power)


 	elif user_input == "2":
 		# Hero is going to stand there like an idiot
 		pass
 	elif user_input == "3":
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
 		hero.health.take_damage(goblin.power)

 		print "The goblin hits you for %d damage" % goblin.power
 		# goblin has attacked, now check to see if hero is still alive...
 		if hero.health <=0:
 			print "You have been killed by the weak goblin, shame on you."
 			# os.system("say You have been killed by the weak goblin, shame on you.")








