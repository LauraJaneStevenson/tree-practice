class TreeNode(object):

	def __init__(self, data):

		self.data = data
		self.left = None
		self.right = None

	def __repr__(self):
		"""Returns human readable tree"""

		return f"<Node:\nData:{self.data}, Left:{self.left}, Right:{self.right}>"


def same_tree(tree1,tree2):
	"""Given two binary trees returns T/F if they're equal"""

	current1 = tree1
	current2 = tree2
	to_check1 = [current1.left,current1.right]
	to_check2 = [current2.left,current2.right]

	while to_check1 and to_check2:

		if current1 != current2:

			return False

		else:

			current1 = to_check1.pop()
			current2 = to_check2.pop()

			to_check1.append(current1.left)
			to_check1.append(current1.right)
			to_check2.append(current2.left)
			to_check2.append(current2.right)

		return True









tree_one = TreeNode(1)
tree_one.right = 3
tree_one.left = 2

tree_two = TreeNode(1)
tree_two.right = 3
tree_two.left = 2

print(same_tree(tree_one,tree_two))

