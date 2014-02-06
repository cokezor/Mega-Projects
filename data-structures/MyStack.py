class MyStack():
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return self.stack == []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		index = len(self.stack)-1
		returnValue = self.stack[index]
		del self.stack[index]
		return returnValue

	def peek(self):
		index = len(self.stack) - 1
		return self.stack[index]

	def size(self):
		return len(self.stack)

def balanced_parens(input_string):
	stack = MyStack()
	for letter in input_string:
		if letter in '[{(':
			stack.push(letter)
		elif letter in ']})':
			try:
				popped = stack.pop()
			except:
				return False

			if not matches(popped, letter):
				return False

	return True if stack.isEmpty() else False

def matches(open, close):
	openers = '([{'
	closers = ')]}'
	return openers.index(open) == closers.index(close)

def dec_to_base(decimal, base):
	digits = '0123456789ABCDEF'
	stack = MyStack()
	while decimal > 0:
		stack.push(digits[decimal % base])
		decimal /= base

	returnString = ''
	while not stack.isEmpty():
		returnString +=  str(stack.pop())

	return returnString

if __name__ == "__main__":
	a = MyStack()
	print a.isEmpty()
	a.push(4)
	a.push('dog')
	print a.peek()
	a.push(True)
	print a.size()
	print a.isEmpty()
	a.push(8.4)
	print a.pop()
	print a.pop()
	print a.size()

	print balanced_parens('((())())')
	print balanced_parens('((()))')
	print balanced_parens(')))')
	print balanced_parens('(((()')
	print balanced_parens('{{([][])}()}')
	print balanced_parens('[{()]')

	print dec_to_base(233, 8)
	print dec_to_base(256, 16)
