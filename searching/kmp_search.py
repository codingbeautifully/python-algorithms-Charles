def search(string, word):

	word_length = len(word)
	string_length = len(string)
	offsets = []

	if word_length > string_length:
		return offsets

	prefix = compute_prefix(word)
	q = 0
	
	for index, letter in enumerate(string):
		while q > 0 and word[q] != letter:
			q = prefix[q - 1]
		if word[q] == letter:
			q += 1
		if q == word_length:
			offsets.append(index - word_length + 1)
			q = prefix[q - 1]
	return offsets


def compute_prefix(word):

	word_length = len(word)
	prefix = [0] * word_length
	k = 0

	for q in range(1, word_length):
		while k > 0 and word[k] != word[q]:
			k = prefix[k - 1]

		if word[k + 1] == word[q]:
			k = k + 1
		prefix[q] = k
	return prefix