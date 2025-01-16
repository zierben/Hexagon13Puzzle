# 创建多进程处理的方案，
# 初始化时，第一个棋子固化，并以移动位数为全局值，执行完一个位置，则返回，重新取第下一个可能的位置，但有可能别的进程已经取了下一个，所以就取更下一个
import concurrent.futures
import multiprocessing
import copy
from ChessPiece import ChessPiece


def writeSolutionsToFile(solution, filename, lock):
    with lock:
        with open(filename, 'a') as file:  # 使用追加模式打开文件
            file.write(f"{solution}\n")  # 将解决方案写入文件，每个解决方案一行


def recursion(board, pieces, piece_index, solution, solutions, filename, lock):
    if piece_index == len(pieces):
        solutions.append(solution.copy())
        writeSolutionsToFile(solution, filename, lock)
        return
    for mask in pieces[piece_index].extension_masks:
        if board.place(mask):
            solution.append(mask)
            if not board.count_closed_spaces():
                board.remove(mask)
                solution.remove(mask)
                continue
            recursion(board, pieces, piece_index + 1, solution, solutions, filename, lock)
            board.remove(mask)
            solution.remove(mask)
    return solutions


def one_process(board, first_piece, pieces, shift, shared_solutions, lock, filename):
    # 把第一个piece 按照sort进行位移，然后合成到board中，如果可以合成，则找答案，如果不能合成，则直接返回无解
    print(f"start of the {shift}th process.")
    piece_to_add = first_piece << shift
    if board.base_mask & piece_to_add == 0:
        # 为每一个进程深度copy一个board，并把初始块合并到board中。递归从第二个块开始找
        base_mask = board.base_mask | piece_to_add
        board.base_mask = base_mask
        board.binary_mask = base_mask
        solutions = recursion(board, pieces, piece_index=0, solution=[], solutions=[], filename=filename, lock=lock)
        for solution in solutions:
            solution.insert(0, piece_to_add)
        shared_solutions.extend(solutions)
        print(f"finished the {shift}th process, and found {len(solutions)} solutions.")
    else:
        print(f"finished the {shift}th process, but cannot place it.")


def solve(chessboard, pieces, use_cores, filename):
    first_piece = ChessPiece.generate_base_mask(pieces[0].shapes[0])
    left_pieces = pieces[1:]
    solutions = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=use_cores) as executor:
        # 创建一个 Manager 来共享数据结构，比如列表
        manager = multiprocessing.Manager()
        shared_solutions = manager.list()
        filelock = manager.Lock()
        # 提交任务到进程池
        futures = []
        for shift in range(1, 81):
            # 为每个进程创建独立的棋盘和棋子副本
            board_copy = copy.deepcopy(chessboard)
            future = executor.submit(one_process, board_copy, first_piece, left_pieces, shift, shared_solutions, filelock, filename)
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
