class Cell(object):
	"""docstring for Cell"""
	def __init__(self, value=None, next_node=None):
		super(Cell, self).__init__()
		self.value = value
		self.next = next_node
	def get_value(self):
		return self.value
	def get_next(self):
		return self.next
	def set_next(self, new_next):
		self.next = new_next


		
class linkedlist(object):
	"""docstring for linkedlist"""
	def __init__(self, head=None):
		super(linkedlist, self).__init__()
		self.head = head

	def insert(self, value):
		new_cell = Cell(value)
		new_cell.set_next(self.head)
		self.head = new_cell

	def search(self, value):
		if (self.head == None):
			print("List empty")
		else:
			current = self.head
			found = False
			while current and found is False:
				if current.get_value() is value:
					found = True
				elif current.get_next() is None:
					current=None
				else:
					current = current.get_next()
			if current is None:
				print("Data not in list")
			else:
				print(current.get_value())
			return current


MyLL = linkedlist()
MyLL.search("HI")
MyLL.insert("HI")
MyLL.insert("HO")
MyLL.insert("HE")
MyLL.insert("HA")
MyLL.search("HP")
MyLL.search("HI")

