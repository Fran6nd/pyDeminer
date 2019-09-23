class Point:

	def copy(self):
		return Point(self.x, self.y)

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def pos(self):
		return (self.x, self.y)
