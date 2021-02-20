"""

	First describe how the game looks and plays this will make it easier to implement.

	Think of the game in iterations.

	First iteration should be simple.

	If a problem occurs, define the problem.  The definition shouldnt be too general.

	1st iteration:
		A simple board of asterisks '*' with a movable character '#'

	Document what I've learned.

	Cyclic reference:
		If class A uses class B but class B uses class A use 'B' syntax in class A or vice versa

	Exceptions:
		Errors detected during execution.

	Add a README file and a requirements file

	Game ideas:
		Tarantula wizard plus bird partner optional
		Find words to cast spells or do actions
		Items pickup limited amount of items

	Either sort the entity array by depth or create a signal/event system
"""

import itertools
import pygame
import pygcurse  # type: ignore[import]

from entity import *
from input import *
from renderer import *
from keys import Key


class DarkMage(Renderable):

	def render(self):

		print("Hello")

	def __init__(self):
		pass

def main():
	entity_manager = EntityManager()
	renderer = Renderer(entity_manager)
	renderer.subscribe(entity_manager)
	entity_manager.add_entity(Renderable())
	id = entity_manager.add_entity(DarkMage())
	window = pygcurse.PygcurseWindow(caption = "Chittering")
	clock = pygame.time.Clock()
	is_running = True
	while is_running:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					entity_manager.fix_enity(id, depth = 5)
		renderer.update()
		renderer.render()
	print(renderer.entities)
	pygame.quit()

if __name__ == "__main__":
	main()