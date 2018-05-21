
from gameObject import gameObject

class Food(gameObject):
	def __init__(self, x, y):
		super().__init__(x, y)

		# Represents if the food can be eaten or not
		self.isPoison = False

	def draw(self, draw, screen, color, shape):
		draw.rect(screen, color, (shape[0]*self.x, shape[1]*self.y, shape[2], shape[3]))
