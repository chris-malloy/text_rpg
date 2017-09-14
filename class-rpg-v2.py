import os
from random import randint

from Bad_Guy import Bad_Guy
from Hero import Hero
from Goblin import Goblin
from Store import Store

print "What is thy name, brave adventurer?"
hero_name = raw_input("> ")

hero = Hero(hero_name)

monsters = []

for i in range(0, number_of_enemies):
	rand_num = randint(0,1)
	if (rand_num == 1):
		monsters.append(Goblin())

print "Today, you shall face %d monsters. Fight well." % number_of_enemies

# how to add number of goblins to monsters list?
monsters.append(Goblin())
print monsters

for i,monster in enumerate(monsters):
	# Run the game as long as BOTH characters have health (are alive)
	while goblin.is_alive() and hero.is_alive():
		print "Choose an option."
		print 




