class Node(object):
	"""Node class"""

	def __init__(self,data):

		self.data = data
		self.children = []

	def add_children(self,new_children):

		self.children.extend(new_children)

	def __repr__(self):
		"""Returns human readable tree"""

		return f"<Tree: {self.data}>"

class Tree(object):

	def __init__(self,root):

		self.root = root

	def __repr__(self):
		"""Returns human readable tree"""
		
		return f"<Root: {self.root.data}>"

	def in_tree(self,node):
		"""Given a node, checks whether node in tree"""

		current = self.root

		to_check = []

		to_check.extend(current.children)

		while to_check:

			print(current)

			if current == node:

				return True

			else:

				if to_check:

					current = to_check.pop()

					to_check.extend(current.children)

		return False

# create tree
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n1.add_children([n2,n3])
n2.add_children([n4,n5])
n3.add_children([n6,n7])
n4.add_children([n8])
tree = Tree(n1)

n9 = Node(9)
# print(tree.in_tree(n4))




