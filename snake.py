from gameObject import GameObject
from utils import Direction


class TailPiece(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "TailPiece: (%d, %d)" % (self.x, self.y)

    # Draw tail piece
    def draw(self, draw, screen, color, shape):
        draw.rect(screen, color, (shape[0]*self.x, shape[1]*self.y, shape[2], shape[3]))


class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)  # Super ctor with x y coor of the head

        self.tail = [TailPiece(x, y)]  # Tail piece list
        self.direction = Direction.NORTH  # Direction of the head

    def change_direction(self, new_direction):
        """
        Change the direction of the snake. Do not allow backward direction changes
        :param new_direction: New Direction to change the snake to
        """
        if {self.direction, new_direction} not in [
            {Direction.NORTH, Direction.SOUTH}, {Direction.WEST, Direction.EAST}
        ]:
            self.direction = new_direction

    def move(self):
        last_position = (self.x, self.y)  # Track last position of the head

        # Move head
        if self.direction is Direction.NORTH:
            self.y -= 1
        elif self.direction is Direction.EAST:
            self.x += 1
        elif self.direction is Direction.SOUTH:
            self.y += 1
        else:
            self.x -= 1

        # Update tail piece coordinates for head
        self.tail[0].x = self.x
        self.tail[0].y = self.y

        # Then move each tail piece
        for i in range(1, len(self.tail)):
            temp_position = (self.tail[i].x, self.tail[i].y)
            self.tail[i].x = last_position[0]
            self.tail[i].y = last_position[1]
            last_position = temp_position

    def grow(self, n):
        # Grow tail by n pieces
        last_piece = self.tail[len(self.tail)-1]
        for i in range(n):
            self.tail.append(TailPiece(last_piece.x, last_piece.y))

    def draw(self, draw, screen, color, shape):
        for t in self.tail:
            t.draw(draw, screen, color, shape)
