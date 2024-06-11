def is_safe(b, r, c): return all(b[i] != c and abs(b[i] - c) != r - i for i in range(r))
def solve_n_queens(N, b=[]): [solve_n_queens(N, b + [c]) for c in range(N) if len(b) == N] or [solve_n_queens(N, b + [c]) for c in range(N) if is_safe(b, len(b), c)]
solve_n_queens(8)
