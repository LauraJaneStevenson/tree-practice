from tree import tree


def kth_smallest(t,k):

	to_visit = [t]
	elements = []

	while to_visit:

		current = to_visit.pop()
		elements.append(current.data)
		
		if current.children:
			to_visit.extend(current.children)


	elements.sort()

	return elements[k - 1]



print(kth_smallest(tree.root,2))
# print(tree.root)