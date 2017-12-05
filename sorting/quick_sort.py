def sort(seq):

	if len(seq) <= 1:
		return seq
	else:
		pivot = seq[0]
		left, right = [], []
		for x in seq[1:]:
			if x < pivot:
				left.append(x)
			else:
				right.append(x)
		return sort(left) + [pivot] + sort(right)