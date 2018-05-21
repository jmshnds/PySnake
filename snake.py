
from direction import Direction
from gameObject import gameObject

class TailPiece(gameObject):
    def __init__(self, x, y):
        super().__init__(x, y) # Super ctor with x y coord of tail piece

    def toString(self):
        return "TailPiece: (%d, %d)" % (self.x, self.y)

    # Draw tail piece
    def draw(self, draw, screen, color, shape):
        draw.rect(screen, color, (shape[0]*self.x, shape[1]*self.y, shape[2], shape[3]))

class Snake(gameObject):
    def __init__(self, x, y):
        super().__init__(x, y) # Super ctor with x y coor of the head

        self.tail = [TailPiece(x,y)] # Tail piece list
        self.direction = Direction.NORTH # Direction of the head

    def changeDirection(self, new_dir):
        # do not allow backward direction changes
        if self.direction is Direction.NORTH and new_dir is Direction.SOUTH or \
            self.direction is Direction.SOUTH and new_dir is Direction.NORTH or \
            self.direction is Direction.WEST and new_dir is Direction.EAST or \
            self.direction is Direction.EAST and new_dir is Direction.WEST:
            return # Do not change direction
        else:
            self.direction = new_dir

    def move(self):
        lastPos = (self.x, self.y) # Track last position of the head

        # Move head
        if self.direction is Direction.NORTH:
            self.y -= 1
        elif self.direction is Direction.EAST:
            self.x += 1
        elif self.direction is Direction.SOUTH:
            self.y += 1
        else:
            self.x -= 1

        # Update tail piece coords for head
        self.tail[0].x = self.x
        self.tail[0].y = self.y

        # Then move each tail piece
        for i in range(1, len(self.tail)):
            tempPos = (self.tail[i].x, self.tail[i].y)
            self.tail[i].x = lastPos[0]
            self.tail[i].y = lastPos[1]
            lastPos = tempPos

    # Grow tail by n pieces
    def grow(self, n):
        lastPiece = self.tail[len(self.tail)-1]
        for i in range(n):
            self.tail.append(TailPiece(lastPiece.x, lastPiece.y))

    # Draw snake
    def draw(self, draw, screen, color, shape):
        for t in self.tail:
            t.draw(draw, screen, color, shape)

