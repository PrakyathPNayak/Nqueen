import time
s = time.time()


def solve(row, ld, rd):
    global count
    if row == all_set:
        count += 1
        return

    available_positions = (~(row | ld | rd)) & col_set

    while available_positions:
        position = -available_positions & available_positions
        available_positions ^= position
        solve(row | position, (ld | position) << 1, (rd | position) >> 1)


n = 13
count = 0
all_set = (1 << n) - 1
col_set = all_set
solve(0, 0, 0)
print("Solution does not exist."*(count<=0) + f"Number of solutions: {count}"*(count>0))
print(time.time()-s)
