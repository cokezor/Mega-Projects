def lpf(n):
	i = 2
	while i < n:
		while n % i == 0 and i <= n/i:
			n = n / i
		i += 1
	return n

def lpf2(n):
	i = 2
	while n % i != 0 and i < n:
		i += 1
	if i < n:
		return lpf2(n/i)
	else:
		return n

lpf(600851475143)
lpf2(600851475143)

import timeit
print timeit.timeit('lpf(600851475143)', setup='from __main__ import lpf', number=100)
print timeit.timeit('lpf2(600851475143)', setup='from __main__ import lpf2', number=100)
