import time
start = time.time()


def solver(board, row, count, n):
    if row == n: return count[0] + 1, print(f'\nCount = {count[0] + 1}\n' + ''.join((''.join('Q 'if j == board[i] else '- ' for j in range(n)) + '\n') for i in range(n)))
    for col in range(n):
        if all(board[i] != col and abs(i - row) != abs(board[i] - col) for i in range(row)): count = solver(board + [col], row + 1, [count[0]], n)
    return count



print(f'The program found {solver([],0, [0], 13)[0]} number of possible variations', time.time()-start)

