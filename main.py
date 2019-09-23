#Main file to run the project.
#Import section.
import pygame
from mineField import MineField
from point import Point
from label import Label
from chrono import Chrono
#Main class.
class Deminer:

	#Initialization: set the differents screen params.
	def __init__(self):
		#Change the height and width values to change the window  and the grid size.
		self.width = 400
		self.height = 600
		self.map_size = Point(self.width, self.height)
		self.frame_rate = 60
		self.done = False	
		pygame.init()
		size = (self.width, self.height)
		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption("pyDeminer")
		#This list will contain all the graphical components.
		self.game_components = list()
		chrono = Chrono(self, Point(self.width / 4, 50))
		pui = Label(self, Point(self.width / 4 * 3, 50), "0%")
		self.game_components.append(pui)
		self.game_components.append(chrono)
		self.game_components.append(MineField(self, Point(0, 100), Point(self.width, self.height - 100), pui, chrono))
		self.game_loop()

	#Game Loop: handle events and redraw the screen 60 times per seconds.
	def game_loop(self):
		self.done = False
		clock = pygame.time.Clock()
		while not self.done:
			self.screen.fill((255, 255, 255))
			dt = clock.tick(self.frame_rate) / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.done = True
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						self.paused = not self.paused
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					pos = Point(pos[0], pos[1])
					for gc in self.game_components:
						gc.on_click(event.button, pos)
			for gc in self.game_components:
				gc.update_and_draw(dt)
			pygame.display.flip()
if __name__ == "__main__":
	Deminer()