class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)
	
	def dequeue(self):
		return self.items.pop(0)

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

a = Queue()
print a.isEmpty()
a.enqueue(5)
a.enqueue(6)
print a.isEmpty()
print a.size()
print a.dequeue()
print a.dequeue()
