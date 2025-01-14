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

    def reset(self):
        self.binary_mask = self.base_mask

    def remove(self, v):
        # check if v is in the mask before removing,(self.binary_mask & v) == v 但这样影响效率，默认不增加这步
        self.binary_mask &= ~v

    def _update_board_from_mask(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.binary_mask & (1 << (i * self.size + j)):
                    self.board[i][j] = 1
                else:
                    self.board[i][j] = 0

    def display_board(self):
        self._update_board_from_mask()
        for row in self.board:
            print(row)
        print('----------')

# chessboard.display_board()
#
# # 假设棋子的掩码已经保存在棋子对象中
# piece_mask = 7 << (4 * size + 4)  # 例如，放置在(4,4)的位置
#
# # 放置一个棋子
# if chessboard.place(piece_mask):
#     print("棋子已放置")
# else:
#     print("无法放置棋子")
#
# chessboard.display_board()
#
# # 尝试放置一个已经在棋盘上的棋子
# if chessboard.place(piece_mask):
#     print("依然可以放置")
#     chessboard.display_board()
# else:
#     print("棋子已经存在，无法放置")
#
# # 还原棋局
# chessboard.reset()
# chessboard.display_board()
