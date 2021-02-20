from signals import *

class SignalEmitter:

	subscribers: list = []

	def __init__(self):
		pass

	def emit(self, signal: Signal, **keywords) -> int:

		for subscriber in self.subscribers:

			subscriber.set({"type": signal, **keywords})

		return len(self.subscribers)

class Subscriber:
	events: list = []

	def __init__(self):
		pass

	def subscribe(self, emitter: SignalEmitter) -> bool:

		if not self in emitter.subscribers:

			emitter.subscribers.append(self)

			return True

		else:

			return False

	def unsubscribe(self, emitter: SignalEmitter) -> bool:

		if self in emitter.subscribers:

			emitter.subscribers.remove(self)

			return True

		else:

			return False

	def set(self, event):

		self.events.append(event)

	def get(self):

		if len(self.events) == 0:

			return None

		return self.events.pop()

	def update(self):

		if len(self.events) == 0:

			return

		event = self.get()

		while event:

			self.process(event)
			
			event = self.get()

	def process(self, event):
		pass