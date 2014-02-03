'''
Enter a string and the program will reverse it and print it out.
'''
def reverse(text):
	return text[::-1] if type(text) is str else None

if __name__ == '__main__':
	text = raw_input('String to reverse: ')
	print reverse(text)
