from same_tree import TreeNode



def print_tree_levels(tree):

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

print(print_tree_levels(tree_one))