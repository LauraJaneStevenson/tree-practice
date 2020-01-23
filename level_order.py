from same_tree import TreeNode

def print_tree_levels(tree):
	"""Given a binary tree, return the 
	level order traversal of its nodes' values. 
	(ie, from left to right, level by level)."""

	nodes_remaining = [[tree]]
	to_return = []


	while nodes_remaining:

		current = nodes_remaining.pop(0)

		temp_list = []

		for node in current:

			if node:

				temp_list.append(node.data)

			if node.left or node.right:

				nodes_remaining.append([node.left,node.right])

		to_return.append(temp_list)

	return to_return

		


tree_one = TreeNode(1)
tree_one.right = TreeNode(3)
tree_one.left = TreeNode(2)
tree_one.left.left = TreeNode(4)
tree_one.left.right = TreeNode(5)
tree_one.right.left = TreeNode(6)
tree_one.right.right = TreeNode(7)

print(print_tree_levels(tree_one))