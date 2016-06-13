class listqueue(object):
	"""docstring for listqueue"""
	def __init__(self, size):
		super(listqueue, self).__init__()
		self.list = ['']*size

		self.head = 0
		self.tail = 0	

	def enqueue(self, value):
		self.list[self.tail] = value
		self.tail = (self.tail+1)%len(self.list)
	def dequeue(self):
		item = self.list[self.head]
		self.head = (self.head+1)%len(self.list)
		print(item)

Queue = listqueue(5)
Queue.enqueue(5)
Queue.enqueue(6)
Queue.enqueue(7)
Queue.enqueue(8)
Queue.enqueue(9)
Queue.enqueue(10)
Queue.enqueue(11)
Queue.dequeue()
Queue.dequeue()
Queue.dequeue()
Queue.dequeue()
