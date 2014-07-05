def sieve1(limit):
    numbers = range(2, limit+1)
    length = len(numbers)

    for index, p in enumerate(numbers):
        if p != 0:
            while index + p < length:
                index = index + p
                numbers[index] = 0

    return [x for x in numbers if x != 0]

def sieve2(limit):
    numbers = [0,0]
    numbers.extend(range(2, limit + 1))
    length = len(numbers)

    for index, p in enumerate(numbers):
        if p != 0:
            index = p ** 2
            if index < length:
                numbers[index] = 0

                while index + p < length:
                    index = index + p
                    numbers[index] = 0

    return [x for x in numbers if x != 0]

def sieve3(limit):
    numbers = [0, 0]
    numbers.extend(range(2, limit + 1))
    length = len(numbers)

    for index, p in enumerate(numbers):
        if p != 0:
            if p != 2 and p % 2 == 0:
                numbers[index] = 0
            else:
                index = p ** 2
                if index < length:
                    numbers[index] = 0

                    while index + p < length:
                        index = index + p
                        numbers[index] = 0

    return [x for x in numbers if x != 0]

def sieve4(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for index, prime in enumerate(a):
        if prime:
            yield index
            for index in xrange(index * index, limit, index):
                a[index] = False

"""
print sieve1(1000)
print sieve2(1000)
print sieve3(1000)
print [x for x in sieve4(1000)]
"""
#print list(sieve4(1000))

import timeit
print timeit.timeit("sieve1(1000000)", setup="from __main__ import sieve1", number = 10)
print timeit.timeit("sieve2(1000000)", setup="from __main__ import sieve2", number = 10)
print timeit.timeit("sieve3(1000000)", setup="from __main__ import sieve3", number = 10)
print timeit.timeit("list(sieve4(1000000))", setup="from __main__ import sieve4", number = 10)
