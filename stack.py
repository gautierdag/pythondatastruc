class Stack(object):
	"""docstring for Stack"""

	def __init__(self):
		super(Stack, self).__init__()
		self.count = 0
		self.array = []

	def pop(self):
		if(self.count > 0):
			self.count= self.count - 1
			print(self.array[self.count])
		else:
			print("Stack Empty")
	def push(self, arg):
		self.array.append(arg)
		self.count = self.count + 1



a = Stack();
a.pop()
a.push(12)
a.push(13)
a.push(14)
a.push(15)
a.push(16)
a.push(17)
a.push(18)
a.push(19)
a.pop()
a.pop()
a.pop()
a.pop()
a.pop()
a.pop()
