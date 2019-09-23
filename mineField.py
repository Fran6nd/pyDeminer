import math
from sizeableComponent import SizeableComponent
import pygame
import random
from point import Point
from tile import Tile
mineSize = 25
class MineField(SizeableComponent):

	#Function used to build the array storing the map.
	def buildArray(self):
		self.discoveredTiles = 0
		self.enable = True
		self.numberOfNonMines = 0
		self.numberOfMines = 0
		sizeOfLine = self.size.x/mineSize
		nbOfLines = self.size.y/mineSize
		self.map = list()
		for y in range(int(nbOfLines)):
			self.map.append(list())
			for x in range(int(sizeOfLine)):
				value = random.uniform(0, 10)
				#Change the following value to change mine's proportion
				if value<=1 :
					value = 1
					self.numberOfMines +=1
				else:
					value = 0
					self.numberOfNonMines  +=1
				self.map[y].append(Tile(value))
		for y in range(int(nbOfLines)):
			for x in range(int(sizeOfLine)):
				self.map[y][x].setAmountOfMinesAroundMe(self.getNumberOfMinesNearPoint(Point(x, y)))

	def __init__(self, scene, pos, size, label, chrono):
		self.chrono = chrono
		self.label = label
		self.pos = pos
		self.scene = scene
		self.size = size
		self.surface = pygame.Surface(size.pos())
		self.buildArray()

	def getNumberOfMinesNearPoint(self, pos):
		ls = self.getTilesNearPoint(pos)
		i = 0
		for p in ls:
			tile = self.map[p.y][p.x]
			if tile:
				if tile.value == 1:
					i = i + 1
		return i

	def getTilesNearPoint(self, pos):
		ls = [Point(pos.x, pos.y + 1), Point(pos.x, pos.y - 1), Point(pos.x + 1, pos.y + 1), Point(pos.x - 1, pos.y + 1), Point(pos.x + 1, pos.y - 1), Point(pos.x - 1, pos.y - 1), Point(pos.x + 1, pos.y), Point(pos.x - 1, pos.y)]
		outList = list()
		for p in ls:
			if p.y >= 0  and p.y < len(self.map) and p.x >= 0  and p.x < len(self.map[0]):
				outList.append(p)
		return outList

	def endGame(self, victory = False):
		self.chrono.pause()
		self.enable = False
		if victory == False:
			for y in self.map:
				for x in y:
					if x.value == 1:
						x.discovered = True
		else:
			self.label.set_value("Victory!")

	def exploreTilesNearPos(self, pos):
		tilesNearPoint = self.getTilesNearPoint(pos)
		for p in tilesNearPoint:
			tile = self.map[p.y][p.x]
			if tile.value == 0:
				if not tile.discovered:
					tile.discovered = True
					self.discoveredTiles += 1
					if tile.getAmountOfMinesAroundMe() == 0:
						self.exploreTilesNearPos(p)

	def on_click(self, button, pos):
		if self.enable == False:
			self.buildArray()
		elif self.is_point_inside_me(pos) == True:
			if self.discoveredTiles == 0:
				self.chrono.reset()
				self.chrono.start()
			x = int(pos.x/mineSize)
			y = int(pos.y/mineSize)
			tile = self.map[y][x]
			if tile.value == 1:
				tile.discovered = True
				self.endGame()
			else:
				if not tile.discovered:
					tile.discovered = True
					self.discoveredTiles +=1
					if tile.getAmountOfMinesAroundMe() == 0:
						self.exploreTilesNearPos(Point(x, y))
					self.label.set_value(str(int(self.discoveredTiles / self.numberOfNonMines * 100)) + "%")
				if self.discoveredTiles == self.numberOfNonMines:
					self.endGame(True)

	def update_and_draw(self, dt):
		self.surface.fill((255, 255, 255))
		self.scene.screen.blit(self.surface, self.pos.pos())
		for y in range(len(self.map)):
			for x in range(len(self.map[0])):
				tile = self.map[y][x]
				if tile.discovered == False:
					pygame.draw.rect(self.scene.screen, (255,255, 255), pygame.Rect(x*mineSize, y * mineSize + self.pos.y, mineSize, mineSize))
					pygame.draw.rect(self.scene.screen, (0,0, 0), pygame.Rect(x*mineSize, y * mineSize + self.pos.y, mineSize, mineSize), 5)
				elif(tile.value == 0):
					color = (255, 0, 50)
					fontColor = (255, 255, 50)
					pygame.draw.rect(self.scene.screen, color, pygame.Rect(x*mineSize, y * mineSize + self.pos.y, mineSize, mineSize))
					if tile.textRect == None:
						font = pygame.font.Font(None, 25)
						text = font.render(str(self.map[y][x].getAmountOfMinesAroundMe()), True, fontColor)
						tile.textRect = text.get_rect(center=(x * mineSize + mineSize/2, y*mineSize + mineSize/2 + self.pos.y))
						tile.text = text
					self.scene.screen.blit(tile.text,tile.textRect)
				else:
					pygame.draw.rect(self.scene.screen, (0, 0, 50), pygame.Rect(x*mineSize, y * mineSize + self.pos.y, mineSize, mineSize))
if __name__ == "__main__":
	print("nothing to do")