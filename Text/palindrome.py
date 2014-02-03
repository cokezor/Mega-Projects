'''
Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like racecar
'''
def is_palindrome(word):
	return word == word[::-1]

if __name__ == '__main__':
	word = raw_input('Word to check: ')
	print is_palindrome(word)
