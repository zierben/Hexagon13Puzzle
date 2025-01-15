from ChessPiece import ChessPiece
from Chessboard import Chessboard

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
ChessPieceL = ChessPiece(
    [[(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)],
     [(0, 4), (0, 3), (1, 2), (2, 1), (3, 0)],
     [(0, 1), (1, 1), (2, 1), (3, 1), (4, 0)],
     [(0, 3), (1, 3), (2, 2), (3, 1), (4, 0)],
     [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3)],
     [(0, 4), (0, 3), (0, 2), (0, 1), (1, 0)]]
)
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

my_pieces = [ChessPieceL, ChessPieceY, ChessPieceR, ChessPieceB, ChessPieceM, ChessPieceW1,
          ChessPieceV, ChessPiece1, ChessPiece6, ChessPieceV3, ChessPieceN, ChessPieceW2]

right_pieces = [ChessPieceL, ChessPieceY, ChessPieceR, ChessPieceB, ChessPieceM, ChessPieceW1,
          ChessPieceV, ChessPiece1, ChessPiece6, ChessPieceV3, ChessPieceN, ChessPieceI]

