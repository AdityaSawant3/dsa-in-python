class Stack:

	def __init__(self, length):
		self.length = length
		self.__container = []


	def is_empty(self):
		return self.__container == []

	def is_full(self):
		return len(self.__container) == self.length

	def push(self, data):
		if self.is_full():
			print("Stack is full")
			return
		self.__container.append(data)

	def pop(self):
		if self.is_empty():
			print("Stack is empty")
			return
		return self.__container.pop()

	def print_items(self):
		if self.is_empty():
			print("Stack is empty")
			return
		for item in self.__container:
			print(item)

stack = Stack(5)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.print_items()