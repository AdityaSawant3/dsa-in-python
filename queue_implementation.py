class Queue:

	def __init__(self, size):
		self.size = size
		self.__container = []
		self.front = 0
		self.rear = 0

	# Either queue does not contains elements or all items are empty.
	def is_empty(self):
		return self.front == self.rear

	def is_full(self):
		return self.rear == self.size

	# Retrieve's the value at the front of the queue.
	def peek(self):
		if self.is_empty():
			print("Queue is empty cannot remove elements.")
			return
		return self.__container[self.front]

	def enqueue(self, data):
		if self.is_full():
			print("Queue is full cannot add elements")
			return
		self.__container.append(data)
		self.rear += 1

	def dequeue(self):
		if self.is_empty():
			print("Queue is empty cannot remove elements.")
			return
		removed_element = self.__container[self.front]
		self.front += 1
		return removed_element

	def print_queue(self):
		if self.is_empty():
			print("Queue is empty cannot print elements.")
			return
		for i in range(self.front, self.rear):
			print(f"{self.__container[i]}\t", end=" ")
		print()


queue = Queue(5)

queue.enqueue(41)
queue.enqueue(62)
queue.enqueue(23)
queue.enqueue(64)
queue.enqueue(54)
queue.print_queue()
print(f"Peek element at queue is {queue.peek()}")

queue.dequeue()
queue.dequeue()
queue.print_queue()
print(f"Peek element at queue is {queue.peek()}")