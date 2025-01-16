import datetime
from Chessboard import Chessboard
from ChessPieceResource import my_pieces, right_pieces, board, size
from SolvingProcess import solve
import psutil

if __name__ == "__main__":
    useAllVirtualCore = False
    # 获取总的核心数，logical = True 包括虚拟核心 logical = False 仅物理核心
    total_cores = psutil.cpu_count(logical=useAllVirtualCore)
    total_cores = (total_cores - 2) if total_cores > 4 else total_cores  # 排除2个核心,给其他程序使用

    pieces = my_pieces
    # 创建棋盘对象
    chessboard = Chessboard(size, board)
    allSolutions = []
    logFileName = f"solutions{datetime.datetime.now().strftime('%Y%m%d%H%M')}.txt"
    # 启动求解
    solve(chessboard, pieces, total_cores, logFileName)
    # 如果要显示任何一个solution，可以调用下面方法
    # drawing = Drawing(board)
    # drawing.draw_solution([443010652194645999616, 282026347331584, 1128111848554496, 583242540023545856, 113447620168501818294272, 18554936017882710016,
    #                        4449653358592, 2172715264, 57536, 33065806766522880753664, 3149872, 141218793127936])
