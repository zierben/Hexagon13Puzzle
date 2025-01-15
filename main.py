from Drawing import Drawing
from Chessboard import Chessboard
from ChessPieceResource import my_pieces, right_pieces, board, size
from SolvingProcess import solve

#
# def draw_chess(sleep=1):
#     for chess in pieces:
#         for oneShape in chess.shapes:
#             print(oneShape)
#             turtle.reset()
#             drawing.draw_board()
#             for oneCell in oneShape:
#                 drawing.change_cell_color(oneCell[0] + 4, oneCell[1] + 4, new_color=1)
#             turtle.update()
#             time.sleep(sleep)


if __name__ == "__main__":
    drawing = Drawing()
    pieces = my_pieces
    # 创建棋盘对象
    chessboard = Chessboard(size, board)
    allSolutions = []
    # 启动求解
    solve(chessboard, pieces)
