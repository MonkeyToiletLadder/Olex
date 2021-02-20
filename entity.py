from signal import *

class EntityManagerException(Exception):

	def __init__(self, message):
	
		self.message = message

class Entity:
	
	id: int = 0

	manager: 'EntityManager' = None  # type: ignore[assignment]

	def __init__(self):
		pass

	def update(self):
		pass

class EntityManager(SignalEmitter):
	
	entities: dict = {}

	removed: list = []

	active: list = []

	def __init__(self):
		pass

	def add_entity(self, entity: Entity, **keywords) -> int:

		if len(self.removed) > 0:
	
			entity.id = self.removed.pop()
	
		else:
	
			entity.id = len(self.entities)
		
		self.entities.update({entity.id: entity})

		if entity.id in self.active:
	
			raise EntityManagerException("The id \'%i\' is already in use." % entity.id)
		
		self.active.append(entity.id)
		
		self.emit(Signal.ENTITY_ADDED, entity_id = entity.id)

		return entity.id

	def rem_entity(self, id) -> None:

		self.active.remove(id)

		del self.entities[id]

		self.emit(Signal.ENTITY_REMOVED, entity_id = id)

	def get_entity(self, id) -> Entity:
	
		return self.entities[id]

	def fix_enity(self, id, **keywords):
		entity = self.entities[id]

		for key, value in keywords.items():
			
			if key in entity.__dict__:
			
				entity[key] = value

		self.emit(Signal.ENTITY_FIXED, entity_id = entity.id, fixed = keywords)