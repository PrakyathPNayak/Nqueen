import time
start = time.time()


def solver(board, row, count):
    n = a
    if row == n:
        count += 1
        print(f'\nCount = {count}\n' + ''.join((''.join('Q ' if j == board[i] else '- ' for j in range(n)) + '\n') for i in range(n)))
    for col in range(n):
        if all(board[i] != col and abs(i - row) != abs(board[i] - col) for i in range(row)): solver(board + [col], row + 1, count)
    return count

a = 10
print(f'The program found {solver([],0, 0)} number of possible variations', time.time()-start)
