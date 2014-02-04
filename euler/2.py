prev = 1
current = 2
total = 0

while current < 4000000:
	if current % 2 == 0:
		total += current

	current, prev = prev, current

	current += prev

print total
