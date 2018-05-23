import pygame

from colors import Color
from gameObject import gameObject

class Button(gameObject):
	def __init__(self, x, y, width, height, text):
		super().__init__(x, y)

		self.width = width
		self.height = height
		self.text = text

	def draw(self, draw, screen, color):
		# Create font
		if not pygame.font.get_init():
			raise Exception("Pygame font not initialized")
		font = pygame.font.SysFont("monospace", 15)

		# Calculate font width and height
		text_w, text_h = font.size(self.text)

		# Draw button rectangle
		draw.rect(screen, color, (self.x-self.width/2, self.y-self.height/2, self.width, self.height))

		# Draw button text
		label = font.render(self.text, 1, Color.BLACK)
		screen.blit(label, (self.x-text_w/2, self.y-text_h/2))

	def isClicked(self, coordinates):
		# Check if coordinates are within the button
		x, y = coordinates
		half_w = self.width/2
		half_h = self.height/2

		if x >= self.x - half_w and x <= self.x + half_w:
			if y >= self.y - half_h and y <= self.y + half_h:
				return True
		return False

