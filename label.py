#The Label class used to display texts.
from component import Component
import pygame
class Label(Component):

	def __init__(self,scene, pos, value = 0):
		self.pos = pos
		self.scene = scene
		self.value = value

	def update_and_draw(self, dt):
		font = pygame.font.Font(None, 25)
		text = font.render( str(self.value), True, (255,0,255))
		self.text_rect = text.get_rect(center=(self.pos.x, self.pos.y))
		self.text = text
		self.scene.screen.blit(self.text, self.text_rect)

	def set_value(self, v):
		self.value = v