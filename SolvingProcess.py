# 创建多进程处理的方案，
# 初始化时，第一个棋子固化，并以移动位数为全局值，执行完一个位置，则返回，重新取第下一个可能的位置，但有可能别的进程已经取了下一个，所以就取更下一个
import concurrent.futures
import multiprocessing
from ChessPiece import ChessPiece


def recursion(board, pieces, piece_index, solution, solutions):
    if piece_index == len(pieces):
        solutions.append(solution.copy())
        return
    for mask in pieces[piece_index].extension_masks:
        if board.place(mask):
            solution.append(mask)
            if not board.count_closed_spaces():
                board.remove(mask)
                solution.remove(mask)
                continue
            recursion(board, pieces, piece_index + 1, solution, solutions)
            board.remove(mask)
            solution.remove(mask)
    return solutions


def one_process(board, first_piece, pieces, process_sort):
    # 把第一个piece 按照sort进行位移，然后合成到board中，如果可以合成，则找答案，如果不能合成，则直接返回无解
    piece_2_add = first_piece << process_sort
    if board.base_mask & piece_2_add == 0:
        base_mask = board.base_mask | piece_2_add
        board_copy = board.copy()
        board_copy.base_mask = base_mask
        board_copy.binary_mask = base_mask
        solutions = recursion(board_copy, pieces, piece_index=0, solution=[], solutions=[])
        # TODO 每个solution还必须加上第一个元素
        return solutions
    else:
        return None


def solve(chessboard, pieces):
    first_piece = ChessPiece.generate_base_mask(pieces[0].shape[0])
    left_pieces = pieces[1:]
    solutions = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        # 创建一个 Manager 来共享数据结构，比如列表
        manager = multiprocessing.Manager()
        shared_solutions = manager.list()

        # 提交任务到进程池
        futures = []
        for shift in range(1, 81):
            # 为每个进程创建独立的棋盘和棋子副本
            board_copy = chessboard.copy()
            pieces_copy = [piece.copy() for piece in left_pieces]
            future = executor.submit(one_process, board_copy, first_piece, pieces_copy, shift, shared_solutions)
            futures.append(future)

        # 等待所有进程完成
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # 获取结果，如果发生异常，将会在这里抛出
            except Exception as exc:
                print(f'Generated an exception: {exc}')

        # 将共享列表转换为普通列表
        solutions.extend(list(shared_solutions))

    # 打印结果
    print(solutions)
