import multiprocessing, time
s = time.time()


def solve_nqueens_parallel(n):
    def is_safe(row, ld, rd):
        return not (row & ld or row & rd or row & col_set)

    def solve(row, ld, rd, positions, result_queue):
        nonlocal count
        if row == all_set:
            count += 1
            result_queue.put(positions)
            return

        available_positions = (~(row | ld | rd)) & col_set

        while available_positions:
            position = available_positions & -available_positions
            available_positions ^= position
            solve(row | position, (ld | position) << 1, (rd | position) >> 1, positions + [position], result_queue)

    count = 0
    all_set = (1 << n) - 1
    col_set = all_set


    result_queue = multiprocessing.Queue()
    processes = []

    for i in range(n):
        process = multiprocessing.Process(target=solve, args=(1 << i, 1 << (i + 1), 1 << (i - 1)*(i>0), [1 << i], result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    solutions = []
    while not result_queue.empty():
        solutions.append(result_queue.get())

    if count == 0:
        print("Solution does not exist.")
    else:
        print(f"Number of solutions: {count}")
        print("Solutions:")
        for sol in solutions:
            board = [['.' for _ in range(n)] for _ in range(n)]
            for pos in sol:
                row = bin(pos)[2:].rjust(n, '0')
                for j, char in enumerate(row):
                    if char == '1':
                        board[j][sol.index(pos)] = 'Q'
            for row in board:
                print(' '.join(row))
            print()


n = 8
solve_nqueens_parallel(n)


print(time.time()-s)
