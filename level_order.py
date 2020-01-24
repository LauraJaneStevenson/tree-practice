from same_tree import TreeNode

def print_tree_levels(tree):
	"""Given a binary tree, return the 
	level order traversal of its nodes' values. 
	(ie, from left to right, level by level)."""


	levels = []

	if not tree:
		return levels

	def create_levels(node,level):

		if level == len(levels):
			# start a new level as empty list
			levels.append([])

		# add value to nested list
		levels[level].append(node.data)

		# recursively call left and right children 
		# and add to level
		if node.left:
			create_levels(node.left,level + 1)

		if node.right:
			create_levels(node.right,level + 1)



	create_levels(tree,0)
	return levels



tree_one = TreeNode(1)
tree_one.right = TreeNode(3)
tree_one.left = TreeNode(2)
tree_one.left.left = TreeNode(4)
tree_one.left.right = TreeNode(5)
tree_one.right.left = TreeNode(6)
tree_one.right.right = TreeNode(7)

print(print_tree_levels(tree_one))