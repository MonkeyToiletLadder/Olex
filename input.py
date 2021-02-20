import pygame
import time
from keys import Key
from copy import deepcopy

class KeyState:
	pressed: bool = False
	released: bool = False
	code: int = -1

	def __init__(self, code, pressed, released):
		self.code = code
		self.pressed = pressed
		self.released = released

	def __deepcopy__(self, memo):
		cls = self.__class__;
		result = cls.__new__(cls)
		memo[id(self)] = result
		for k, v in self.__dict__.items():
			setattr(result, k, deepcopy(v, memo))
		return result

class InputManager:
	_currkeys: dict = {}
	_prevkeys: dict = {}
	_start: float = 0

	def __init__(self):
		for key in Key:
			self._currkeys.update({int(key): KeyState(int(key), False, True)})
			self._prevkeys.update({int(key): KeyState(int(key), False, True)})

	def update(self):
		"""\
		\nMust be called after methods that\
		\ncall is_pressed is_justpressed or is_justreleased.\
		\nIn other words at the end of your update method.\
		"""
		self._prevkeys = deepcopy(self._currkeys)

	def setstate(self, event):
		if event.type == pygame.KEYDOWN:
			code = event.key
			self._currkeys[code].pressed = True
			self._currkeys[code].released = False

		if event.type == pygame.KEYUP:
			code = event.key
			self._currkeys[code].released = True
			self._currkeys[code].pressed = False

	def is_justpressed(self, key: Key):
		currstate = self._currkeys[int(key)].pressed
		prevstate = self._prevkeys[int(key)].pressed

		if currstate and currstate != prevstate:
			return True
		else:
			return False

	def is_justreleased(self, key: Key):
		currstate = self._currkeys[int(key)].released
		prevstate = self._prevkeys[int(key)].released

		if currstate and currstate != prevstate:
			return True
		else:
			return False

	def is_pressed(self, key: Key, **keywords):
		delay = keywords.get("delay", 0)
		result = self._currkeys[int(key)].pressed
		if result and (time.time() - self._start) >= delay:
			self._start = time.time()
			return True
		else:
			return False