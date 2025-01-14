from ChessPiece import ChessPiece
from Chessboard import Chessboard
from drawing import Drawing
import turtle, time

solution = []

times = 0


def draw_chess(sleep=1):
    for chess in pieces:
        for oneShape in chess.shapes:
            print(oneShape)
            turtle.reset()
            drawing.draw_board()
            for oneCell in oneShape:
                drawing.change_cell_color(oneCell[0] + 4, oneCell[1] + 4, new_color=1)
            turtle.update()
            time.sleep(sleep)


def draw_solution(with_print=False):
    global solution, times
    turtle.reset()
    drawing.draw_board()
    for i in range(len(solution)):
        shape = ChessPiece.get_shape_from_mask(solution[i])
        for position in shape:
            drawing.change_cell_color(position[0], position[1], i)
    turtle.update()
    if with_print:
        times += 1
        print(f"the {times} solution")
        print(solution)


def solve(board, pieces, piece_index=0):
    global solution
    if piece_index == len(pieces):
        draw_solution(True)
        time.sleep(5)
        return False
        # turtle.done()
        # return True
    for mask in pieces[piece_index].extension_masks:
        if board.place(mask):
            solution.append(mask)
            if len(solution) < 4:
                draw_solution()
            if not board.count_closed_spaces():
                board.remove(mask)
                solution.remove(mask)
                continue
            if solve(board, pieces, piece_index + 1):
                # print(mask)
                return True
            board.remove(mask)
            solution.remove(mask)
    return False


if __name__ == "__main__":
    # 定义所有棋子的形状
    # 示例使用
    # 创建一个9x9的棋盘掩码，假设所有格子都是可用的
    board_mask = 2270874908986167672966671  # 这将创建一个默认棋盘的掩码
    size = 9
    board = [
        [1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 1]
    ]
    # 创建棋子l形状的棋子
    # ChessPieceL = ChessPiece(
    #     [[(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)],
    #      [(0, 4), (0, 3), (1, 2), (2, 1), (3, 0)],
    #      [(0, 1), (1, 1), (2, 1), (3, 1), (4, 0)],
    #      [(0, 3), (1, 3), (2, 2), (3, 1), (4, 0)],
    #      [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3)],
    #      [(0, 4), (0, 3), (0, 2), (0, 1), (1, 0)]]
    # )
    ChessPieceL = ChessPiece([[(0, 4), (0, 3), (1, 2), (2, 1), (3, 0)]])
    # 创建棋子Y形状的棋子
    ChessPieceY = ChessPiece(
        [[(0, 2), (1, 1), (1, 0), (2, 1), (3, 1)],
         [(0, 3), (1, 2), (2, 1), (2, 0), (3, 1)],
         [(0, 3), (1, 2), (1, 1), (1, 0), (2, 2)]]
    )
    # 创建棋子R形状的棋子
    ChessPieceR = ChessPiece(
        [[(0, 3), (1, 2), (1, 1), (1, 0), (2, 1)],
         [(0, 2), (0, 1), (0, 0), (1, 1), (2, 1)],
         [(0, 2), (1, 1), (1, 0), (2, 0), (3, 0)],
         [(0, 3), (1, 2), (2, 1), (2, 0), (2, 2)],
         [(0, 2), (1, 1), (2, 0), (2, 1), (3, 1)],
         [(0, 2), (1, 2), (1, 1), (1, 0), (2, 2)]]
    )
    # 创建棋子b形状的棋子
    ChessPieceB = ChessPiece(
        [[(0, 3), (0, 2), (1, 2), (1, 1), (2, 0)],
         [(0, 1), (0, 0), (1, 2), (1, 1), (1, 0)],
         [(0, 1), (1, 1), (2, 1), (2, 0), (3, 0)],
         [(0, 0), (1, 0), (2, 0), (1, 1), (2, 1)],
         [(0, 3), (0, 2), (0, 1), (1, 1), (1, 0)],
         [(0, 2), (1, 2), (1, 1), (2, 1), (3, 0)]]
    )

    # 创建棋子m形状的棋子
    ChessPieceM = ChessPiece(
        [[(0, 2), (1, 2), (2, 1), (3, 0), (3, 1)],
         [(0, 3), (1, 3), (1, 2), (1, 1), (2, 0)],
         [(0, 0), (1, 0), (1, 1), (1, 2), (2, 1)],
         [(0, 1), (1, 1), (1, 0), (2, 1), (2, 2)],
         [(0, 3), (0, 2), (1, 1), (1, 0), (2, 0)],
         [(0, 2), (0, 1), (1, 1), (2, 1), (3, 0)]]
    )
    # 创建棋子w形状的棋子 有2个
    ChessPieceW1 = ChessPiece(
        [[(0, 2), (0, 1), (1, 1), (2, 0), (3, 0)],
         [(0, 2), (1, 1), (2, 1), (3, 0), (3, 1)],
         [(0, 3), (1, 2), (1, 1), (1, 0), (2, 0)],
         [(0, 1), (1, 2), (1, 1), (1, 0), (2, 2)],
         [(0, 1), (0, 0), (1, 1), (1, 2), (2, 1)],
         [(0, 3), (1, 3), (1, 2), (2, 1), (2, 0)]]
    )
    # 创建棋子w形状的棋子 有2个
    ChessPieceW2 = ChessPiece(
        [[(0, 2), (0, 1), (1, 1), (2, 0), (3, 0)],
         [(0, 2), (1, 1), (2, 1), (3, 0), (3, 1)],
         [(0, 3), (1, 2), (1, 1), (1, 0), (2, 0)],
         [(0, 1), (1, 2), (1, 1), (1, 0), (2, 2)],
         [(0, 1), (0, 0), (1, 1), (1, 2), (2, 1)],
         [(0, 3), (1, 3), (1, 2), (2, 1), (2, 0)]]
    )
    # 创建棋子V形状的棋子
    ChessPieceV = ChessPiece(
        [[(0, 2), (1, 2), (2, 2), (2, 1), (3, 0)],
         [(0, 2), (1, 1), (1, 2), (1, 3), (2, 0)],
         [(0, 1), (1, 1), (2, 1), (2, 2), (2, 0)],
         [(0, 2), (0, 3), (0, 1), (1, 1), (2, 0)],
         [(0, 1), (1, 1), (2, 1), (1, 2), (3, 0)],
         [(0, 0), (1, 0), (1, 1), (1, 2), (2, 0)]]
    )

    # 创建棋子1形状的棋子
    ChessPiece1 = ChessPiece(
        [[(0, 1), (1, 1), (2, 0), (3, 0), (4, 0)],
         [(0, 4), (1, 3), (2, 2), (2, 1), (3, 0)],
         [(0, 3), (1, 2), (2, 1), (3, 1), (4, 0)],
         [(0, 4), (0, 3), (1, 2), (1, 1), (1, 0)],
         [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)],
         [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1)]]
    )

    # 创建棋子6形状的棋子
    ChessPiece6 = ChessPiece(
        [[(0, 2), (1, 1), (2, 0), (2, 1), (3, 0)],
         [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)],
         [(0, 3), (0, 2), (1, 2), (1, 1), (1, 0)],
         [(0, 0), (0, 1), (1, 0), (1, 1), (2, 1)],
         [(0, 3), (1, 2), (1, 1), (2, 0), (2, 1)],
         [(0, 1), (1, 0), (1, 1), (2, 0), (3, 0)]]
    )
    # 创建棋子V3形状的棋子
    ChessPieceV3 = ChessPiece(
        [[(0, 2), (1, 2), (2, 2), (3, 1), (4, 0)],
         [(0, 4), (0, 3), (0, 2), (1, 1), (2, 0)],
         [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]]
    )
    # 创建棋子N形状的棋子
    ChessPieceN = ChessPiece(
        [[(0, 1), (1, 1), (1, 0), (2, 1), (3, 0)],
         [(0, 2), (1, 2), (2, 1), (2, 0), (3, 0)],
         [(0, 3), (0, 2), (0, 1), (1, 2), (1, 0)],
         [(0, 3), (0, 2), (1, 1), (2, 0), (2, 1)],
         [(0, 1), (0, 0), (1, 0), (2, 0), (2, 1)],
         [(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)]]
    )
    # 创建棋子I形状的棋子
    ChessPieceI = ChessPiece(
        [[(0, 1), (0, 2), (0, 3), (0, 0), (1, 2)],
         [(0, 3), (1, 2), (2, 1), (2, 0), (3, 0)],
         [(0, 0), (0, 1), (1, 0), (2, 0), (3, 0)],
         [(0, 3), (1, 2), (2, 1), (3, 0), (3, 1)],
         [(0, 2), (1, 0), (1, 1), (1, 2), (1, 3)],
         [(0, 1), (1, 0), (1, 1), (2, 1), (3, 1)]]
    )
    pieces = [ChessPieceL, ChessPieceY, ChessPieceR, ChessPieceB, ChessPieceM, ChessPieceW1,
              ChessPieceV, ChessPiece1, ChessPiece6, ChessPieceV3, ChessPieceN, ChessPieceW2]
    #
    # , ChessPieceN]

    # 创建棋盘对象
    chessboard = Chessboard(size, board)
    drawing = Drawing()
    # draw_chess()

    # 启动求解
    solve(chessboard, pieces)
    #
    # if solution:
    #     draw_solution()

    turtle.done()
