from Cell import Cell


class Chessboard:
    def __init__(self, size, board):
        self.size = size
        self.board = board
        self.cells = {}
        self.base_mask = self._create_binary_mask()
        self.add_cell_adjacent()
        self.binary_mask = self.base_mask

    def add_cell_adjacent(self):
        for (x, y) in self.cells:
            if (x, y + 1) in self.cells:
                self.cells[(x, y)].adjacent.append(self.cells[(x, y + 1)])
            if (x + 1, y) in self.cells:
                self.cells[(x, y)].adjacent.append(self.cells[(x + 1, y)])
            if (x, y - 1) in self.cells:
                self.cells[(x, y)].adjacent.append(self.cells[(x, y - 1)])
            if (x - 1, y) in self.cells:
                self.cells[(x, y)].adjacent.append(self.cells[(x - 1, y)])
            if (x + 1, y - 1) in self.cells:
                self.cells[(x, y)].adjacent.append(self.cells[(x + 1, y - 1)])
            if (x - 1, y + 1) in self.cells:
                self.cells[(x, y)].adjacent.append(self.cells[(x - 1, y + 1)])

    def count_closed_spaces(self):
        one = 0
        visited = set()
        for cell in self.cells.values():
            if cell not in visited:
                visited.add(cell)
            else:
                continue
            if cell.mask & self.binary_mask != 0:
                continue  # skip if cell has been masked
            else:
                new_closed_spaces = self.dfs(cell, visited)
                if new_closed_spaces == 1 and one == 0:
                    one = 1
                elif new_closed_spaces % 5 == 0:
                    continue
                elif new_closed_spaces % 5 == 1 and one == 0:
                    continue
                else:
                    return False
        return True

    def dfs(self, cell, visited):
        stack = [onecell for onecell in cell.adjacent]
        blank_spaces = 1
        while stack:
            cell = stack.pop()
            if cell in visited:
                continue
            visited.add(cell)
            if cell.mask & self.binary_mask == 0:
                blank_spaces += 1
                for cell in cell.adjacent:
                    if cell not in visited:
                        stack.append(cell)
        return blank_spaces

    def _create_binary_mask(self):
        mask = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    mask |= (1 << (i * self.size + j))
                else:
                    cell = Cell(i, j, (1 << (i * self.size + j)))
                    self.cells[(i, j)] = cell
        return mask

    def place(self, v):
        if self.is_valid(v):
            self.binary_mask |= v
            return True
        return False

    def is_valid(self, v):
        return (self.binary_mask & v) == 0

    def remove(self, v):
        # check if v is in the mask before removing,(self.binary_mask & v) == v 但这样影响效率，默认不增加这步
        self.binary_mask &= ~v
