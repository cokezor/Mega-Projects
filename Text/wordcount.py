def count_words(string='', file=None):
	if file:
		try:
			f = open(file, 'r')
			string = f.read()
			f.close()
		except IOError:
			print 'Could not find file'
			return {}
	wordcount = {}
	for word in string.split(' '):
		if word in wordcount:
			wordcount[word] += 1
		else:
			wordcount[word] = 1
	return wordcount

if __name__ == '__main__':
	wordcount = {}
	while True:
		response = raw_input('String or file? ')
		if response == 'string':
			string = raw_input('Input string: ')
			wordcount = count_words(string)
			break
		elif response == 'file':
			string = raw_input('Input filename ')
			wordcount = count_words(file=string)
			break

	for key, value in wordcount.iteritems():
		print key, value
