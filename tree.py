class Node(object):
	"""docstring for Node"""
	def __init__(self, value=None, Parent=None, left=None, right=None):
		super(Node, self).__init__()
		self.value = value
		self.Parent =Parent
		self.right = right
		self.left = left

class Tree(object):
	"""docstring for Tree"""
	def __init__(self, root=None):
		super(Tree, self).__init__()
		self.root = root
	def BreadthFirst(self):
		print(self.root.value)
		left = self.root.left
		while left is True:
			print(left) 
		
		
		