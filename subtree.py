from same_tree import tree_one, tree_two

def subtree(t,s):
	# check if current nodes are the same by traversing both trees, 
	# when they're not the same reset current2 back to root of t
	# if traversed the whole t, return true 

	# larger tree
	to_visit_s = [s] 

	# constant subtree
	to_visit_t = [t]

	while to_visit_s:

		current_s = to_visit_s.pop(0)
		current_t = to_visit_t.pop(0)
		print('T:', current_t)
		print('S:', current_s)

		# if nodes not equal, reset current_t to t.root
		# so sub tree of s will be compaired to 
		# whole tree t 
		if current_s.data != current_t.data:

			to_visit_t = [t]

		# if we have traversed all of t, and nodes are equal
		# return true
		elif current_t.left == None and current_t.right == None:

			return True

		else: 

			if current_t.left:
				to_visit_t.append(current_t.left)

			if current_t.right:
				to_visit_t.append(current_t.right)


		if current_s.left:
				to_visit_s.append(current_s.left)

		if current_s.right:
			to_visit_s.append(current_s.right)



	return False

print(subtree(tree_one,tree_two))



