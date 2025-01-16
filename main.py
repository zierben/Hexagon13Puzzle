import datetime

from Drawing import Drawing
from Chessboard import Chessboard
from ChessPieceResource import my_pieces, right_pieces, board, size
from SolvingProcess import solve
import psutil

if __name__ == "__main__":
    useAllVirtualCore = False
    # 获取总的核心数，logical = True 包括虚拟核心 logical = False 仅物理核心
    total_cores = psutil.cpu_count(logical=useAllVirtualCore)
    total_cores = (total_cores - 2) if total_cores > 4 else total_cores  # 排除2个核心,给其他程序使用
    # drawing = Drawing()
    pieces = my_pieces
    # 创建棋盘对象
    chessboard = Chessboard(size, board)
    allSolutions = []
    logFileName = f"solutions{datetime.datetime.now().strftime('%Y%m%d%H%M')}.txt"
    # 启动求解
    solve(chessboard, pieces, total_cores, logFileName)
