#The base class of a component: all others components have to extend it.
class Component:

	def __init__(self,scene, pos):
		self.pos = pos
		self.scene = scene

	def on_click(self, button, pos):
		pass

	def update_and_draw(self, dt):
		pass
if __name__ == "__main__":
	print("nothing to do")