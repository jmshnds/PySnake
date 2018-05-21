
from gameObject import gameObject
from direction import direction

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
        self.direction = direction['NORTH'] # Direction of the head

    def changeDirection(self, new_dir):
        # do not allow backward direction changes
        if self.direction is direction['NORTH'] and new_dir is direction['SOUTH'] or \
            self.direction is direction['SOUTH'] and new_dir is direction['NORTH'] or \
            self.direction is direction['WEST'] and new_dir is direction['EAST'] or \
            self.direction is direction['EAST'] and new_dir is direction['WEST']:
            return # Do not change direction
        else:
            self.direction = new_dir

    def move(self):
        lastPos = (self.x, self.y) # Track last position of the head

        # Move head
        if self.direction is direction['NORTH']:
            self.y -= 1
        elif self.direction is direction['EAST']:
            self.x += 1
        elif self.direction is direction['SOUTH']:
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

