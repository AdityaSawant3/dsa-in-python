class Circular_Queue:

	def __init__(self, size):
		self.size = size
		# we can initialize the size of the queue in python.
		self.__queue_container = [None] * size
		# For the sake of simplicity assign front and rear to -1.
		self.front = self.rear = -1

	def is_empty(self):
		return self.front == -1

	def is_full(self):
		return (self.rear + 1) % self.size == self.front

	def enqueue(self, data):
		if self.is_full():
			print("Queue is full cannot add element")
			return
		if self.is_empty():
			self.front = 0
			self.rear = 0
		else:
			self.rear = (self.rear + 1) % self.size
		self.__queue_container[self.rear] = data

	def dequeue(self):
		if self.is_empty():
			print("Queue is empty cannot remove element")
			return
		removed_element = self.__queue_container[self.front]
		if self.front == self.rear:
			self.front = self.rear = -1
		else:
			self.front = (self.front + 1) % self.size

		return removed_element

	def print_queue(self):
		if self.is_empty():
			print("Queue is empty cannot print elements")
			return
		i = self.front
		while True:
			print(f"{self.__queue_container[i]}\t", end=" ")
			if i == self.rear:
				break
			i = (i + 1) % self.size
		print()

queue = Circular_Queue(5)
queue.enqueue(41)
queue.enqueue(62)
queue.enqueue(23)
queue.enqueue(64)
queue.enqueue(54)
queue.print_queue()

queue.dequeue()
queue.dequeue()
queue.enqueue(22)
queue.enqueue(90)
queue.print_queue()
