def sort(seq):

	L = len(seq)
	for i in range(L):
		for n in range(1, L - i):
			if seq[n] < seq[n - 1]:
				seq[n - 1], seq[n] = seq[n], seq[n - 1]
	return seq