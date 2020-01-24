from same_tree import TreeNode
from level_order import tree_one, print_tree_levels

def invert_tree(tree):


	def switch_children(node):

		temp = node.left
		node.left = node.right
		node.right = temp

		if node.left:
			switch_children(node.left)

		if node.right:
			switch_children(node.right)

	switch_children(tree)

	return tree



inverted_tree = invert_tree(tree_one)

print(print_tree_levels(inverted_tree))



