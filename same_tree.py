class TreeNode(object):

	def __init__(self, data):

		self.data = data
		self.left = None
		self.right = None

	def __repr__(self):
		"""Returns human readable tree"""

		return f"<{self.data}>"


def same_tree(tree1,tree2):
	"""Given two binary trees returns T/F depending on if they're equal"""

	to_check1 = [tree1.left,tree1.right,tree1]
	to_check2 = [tree2.left,tree2.right,tree2]

	while to_check1 and to_check2:

		current1 = to_check1.pop()
		current2 = to_check2.pop()

		if current1.data != current2.data:

			return False

		else:

			if current1.left and current1.right:
				to_check1.append(current1.left)
				to_check1.append(current1.right)

			if current2.left and current2.right:
				to_check2.append(current2.left)
				to_check2.append(current2.right)

		

	return True


tree_one = TreeNode(1)
tree_one.right = TreeNode(3)
tree_one.left = TreeNode(2)

tree_two = TreeNode(5)
tree_two.right = TreeNode(1)
tree_two.left = TreeNode(2)

tree_two.right.left = TreeNode(2)
tree_two.right.right = TreeNode(3)


print(same_tree(tree_one,tree_two))

