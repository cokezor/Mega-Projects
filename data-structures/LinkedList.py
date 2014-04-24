class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

		
class UnorderedList():
	def __init__(self, head=None):
		self.head = head

	def isEmpty(self):
		return self.head == None

	def add(self, data):
		head = self.head
		self.head = Node(data)
		self.head.next = head	

	def size(self):
		size = 0
		current = self.head
		while current != None:
			size += 1
			current = current.next

		return size

	def search(self, data):
		current = self.head
		while current != None:
			if current.data == data:
				return True
			current = current.next	
		return False

	def remove(self, data):
		if (self.head.data == data):
			self.head = self.head.next
			return True

		previous = self.head
		current = self.head.next

		while current != None:
			if current.data == data:
				previous.next = current.next
				return True
			previous = previous.next
			current = current.next

		return False

	def append(self, data):
		current = self.head 
		while current.next != None:
			current = current.next
		current.next = Node(data)

	def __str__(self):
		current = self.head
		returnStr = ""
		if current == None:
			return "Empty list"

		while current != None:
			returnStr += "%s" %current.data
			if current.next != None:
				returnStr += ", "
			current = current.next

		return returnStr

a = UnorderedList()
a.add(5)
a.add(6)
print a
print a.size()
print a.search(10)
print a.search(5)
print a.remove(6)
print a.size()
print a.append(7)
print a
