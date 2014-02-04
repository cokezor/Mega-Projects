def isDivisible(number):
	for i in range(20,1,-1):
		if number % i != 0:
			return False

	return True

i = 2
while not isDivisible(i):
	i += 2
print i
