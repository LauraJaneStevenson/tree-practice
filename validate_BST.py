from same_tree import TreeNode
from level_order import print_tree_levels
import math

def is_valid_bst(node,lower_val = - math.inf, higher_val = math.inf):
	"""Given a BST, returns T/F depending on if tree is valid"""

	# check if node is none
	# if so we have traversed the whole tree/sub tree
	# without failing and we can return true
	if not node:
		return True

	val = node.data

	# lower value should be lower and higher value 
	# should be higher
	if val <= lower_val or val >= higher_val:
		print("we in the weird conditional")
		return False

	# recursivelt check if child mode is higher than
	# parent, pass parent in place of lower value
	if not is_valid_bst(node.right,val,higher_val):
		return False

	# recursively check if left child node is less than 
	# parent, pass parent in place of higher value
	if not is_valid_bst(node.left,lower_val,val):
		return False

	return True

t = TreeNode(5)

t.left = TreeNode(2)
t.right = TreeNode(8)

t.left.left = TreeNode(1)
t.left.right = TreeNode(4)

t.right.left = TreeNode(6)
t.right.right = TreeNode(9)


print("t is valid: ",is_valid_bst(t))

