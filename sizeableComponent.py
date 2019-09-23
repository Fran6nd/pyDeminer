import math
from component import Component
class SizeableComponent(Component):

	def __init__(self,scene, pos, size):
		self.pos = pos
		self.scene = scene
		self.size = size

	def is_point_inside_me(self, p):
		p.x = p.x- self.pos.x
		p.y = p.y - self.pos.y
		if p.x <0 or p.y < 0 or p.y >self.size.y or p.x > self.size.x:
			return False
		return True


if __name__ == "__main__":
	print("nothing to do")
