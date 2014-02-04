def palindrome(number):
	return str(number)[::-1] == str(number)

def largest():
	i = 999 * 999
	j = 999

	while i >= 100000:
		if palindrome(i):
			while j >= 100:
				if i % j == 0 and len(str(j)) == 3 and len(str(int(i/j))) == 3:
					print i
					return
				j -= 1
		j = 999
		i -= 1

largest()
