number = 0
total = 0

while number < 1000:
	if number % 3 == 0:
		total += number
	elif number % 5 == 0:
		total += number
	number += 1

print total