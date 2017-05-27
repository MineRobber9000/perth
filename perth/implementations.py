class PerthError(Exception):
	pass;

class Stack:
	def __init__(self):
		self.sp = -1
		self.values = []

	def __iter__(self):
		return self

	def pushVal(self,v):
		self.values.append(v)
		self.sp += 1

	def popVal(self):
		if self.sp == -1:
			raise PerthError("Can't pop value from empty stack!")
		ret = self.values.pop(self.sp)
		self.sp -= 1
		return ret

	def next(self):
		try:
			return s.popVal()
		except PerthError as e:
			raise StopIteration
