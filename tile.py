import pygame
class Tile:

	def __init__(self, value):
		self.value = value
		self.discovered = False
		self.closesMines = 0
		self.textRect = None
		self.text = None

	def discover(self):
		self.discovered = True

	def setAmountOfMinesAroundMe(self, val):
		self.closesMines = val

	def getAmountOfMinesAroundMe(self):
		return self.closesMines
if __name__ == "__main__":
	print('Nothing to do...')