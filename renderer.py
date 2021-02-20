from signal import *
from signals import *
from entity import *

class Renderable(Entity):

	depth: int = 0

	def render(self):
		pass

	def __init__(self):
		pass

class Renderer(Subscriber):

	entities: dict = {}

	entity_manager: EntityManager = None  # type: ignore[assignment]

	def __init__(self, entity_manager):

		self.entity_manager = entity_manager

	def process(self, event):

		if event["type"] == Signal.ENTITY_ADDED:

			entity = self.entity_manager.get_entity(event["entity_id"])

			if not issubclass(entity.__class__, Renderable):

				return

			else:

				if len(self.entities) == 0:

					self.entities.update({entity.id: {"depth": entity.depth}})

					self.entities = dict(sorted(self.entities.items(), key = lambda item: item[1]["depth"]))

					return

				for other in self.entities.values():

					if other["depth"] >= entity.depth:

						self.entities.update({entity.id: {"depth": entity.depth}})

						self.entities = dict(sorted(self.entities.items(), key = lambda item: item[1]["depth"]))

						return

		elif event["type"] == Signal.ENTITY_REMOVED:

			id = event["entity_id"]

			del self.entities[id]

			self.entities = dict(sorted(self.entities.items(), key = lambda item: item[1]["depth"]))

		elif event["type"] == Signal.ENTITY_FIXED:

			id = event["entity_id"]

			if "depth" in event["fixed"]:
			
				other = self.entities[id]

				other["depth"] = event["fixed"]["depth"]

				self.entities = dict(sorted(self.entities.items(), key = lambda item: item[1]["depth"]))

	def render(self):

		for id in self.entities.keys():

			entity = self.entity_manager.get_entity(id)

			entity.render()