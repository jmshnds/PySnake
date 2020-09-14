class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, draw, screen, color, shape):
        raise NotImplementedError
