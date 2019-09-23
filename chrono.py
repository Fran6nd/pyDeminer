from label import Label
#Class chrono used to count the time in seconds.
class Chrono(Label):

	def __init__(self, scene, pos, value = 0, count_down = False, running = False):
		self.pos = pos
		self.scene = scene
		self.value = value
		self.dec_value = value
		self.count_down = count_down
		self.running = False

	def update_and_draw(self, dt):
		if self.running:
			#Increment or decrement if it has to count down or not.
			if self.count_down:
				self.dec_value -= dt
			else:
				self.dec_value += dt
		#Keep only one decimal after the dot.
		self.value = int(self.dec_value * 10) / 10
		#Call the update_and_draw() function from the parent: Label.
		super().update_and_draw(dt)

	def pause(self):
		self.running = False

	def reset(self):
		self.value = 0
		self.dec_value = 0
		self.running = False

	def start(self):
		self.running = True