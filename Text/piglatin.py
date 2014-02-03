'''
Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant sound is
transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).
Read Wikipedia for more information on rules.
'''
def pig_latin(word):
	vowels = 'aeiou'
	for i in range(len(word)):
		if i == 0:
			if word[i] in vowels:
				return word + 'way'
			elif word[i] in 'y':
				return word[1:] + 'yay'
		else:
			if word[i] in vowels or word[i] in 'y':
				return word[i:] + word[:i] + 'ay'

if __name__ == '__main__':
	word = raw_input('Enter a word: ')
	print pig_latin(word)
