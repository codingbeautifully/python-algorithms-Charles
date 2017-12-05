from collections import deque


class Queue:

	def __init__(self):
		
		self._queue = deque([])

	def add(self, value):

		self._queue.append(value)

	def remove(self):

		return self._queue.popleft()

	def is_empty(self):

		return not len(self._queue)

	def size(self):

		return len(self._queue)