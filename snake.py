
from direction import direction

class TailPiece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return "TailPiece: (%d, %d)" % (self.x, self.y)

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tail = [TailPiece(x,y)]
        # direction of the head
        self.direction = direction['NORTH'] 

    def changeDirection(self, new_dir):
        # do not allow backward direction changes
        if self.direction is direction['NORTH'] and new_dir is direction['SOUTH'] or \
            self.direction is direction['SOUTH'] and new_dir is direction['NORTH'] or \
            self.direction is direction['WEST'] and new_dir is direction['EAST'] or \
            self.direction is direction['EAST'] and new_dir is direction['WEST']:
            return
        else:
            self.direction = new_dir

    def move(self):
        lastPos = (self.x, self.y)

        # move head
        if self.direction is direction['NORTH']:
            self.y -= 1
        elif self.direction is direction['EAST']:
            self.x += 1
        elif self.direction is direction['SOUTH']:
            self.y += 1
        else:
            self.x -= 1

        self.tail[0].x = self.x
        self.tail[0].y = self.y

        # then move each tail piece
        for i in range(1, len(self.tail)):
            tempPos = (self.tail[i].x, self.tail[i].y)
            self.tail[i].x = lastPos[0]
            self.tail[i].y = lastPos[1]
            lastPos = tempPos

    def grow(self, n):
        # grow tail by n
        lastPiece = self.tail[len(self.tail)-1]
        for i in range(n):
            self.tail.append(TailPiece(lastPiece.x, lastPiece.y))
