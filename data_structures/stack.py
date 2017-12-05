class Stack:

	def __init__(self):
		
		self.stack_list = []

	def add(self, value):

		self.stack_list.append(value)

	def remove(self):

		return self.stack_list.pop()

	def is_empty(self):

		return not self.size()

	def size(self):

		return len(self.stack_list)