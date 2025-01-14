class Cell:
    def __init__(self, x, y, mask):
        self.x = x
        self.y = y
        self.adjacent = []
        self.mask = mask

    def add_adjacent(self, cell):
        self.adjacent.append(cell)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.x == other.x and self.y == other.y
        return False
