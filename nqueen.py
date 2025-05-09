def solve_n_queens(n):
    def is_safe(row, col, board):
        for r in range(row):
            c = board[r]
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def solve(row, board):
        if row == n:
            res.append(["".join('Q' if i == c else '.' for i in range(n)) for c in board])
            return
        for col in range(n):
            if is_safe(row, col, board):
                board[row] = col
                solve(row + 1, board)

    res = []
    solve(0, [-1] * n)
    return res

# Driver code
n = int(input("Enter N (for N-Queens): "))
solutions = solve_n_queens(n)

print(f"\nTotal solutions: {len(solutions)}\n")
for i, sol in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for row in sol:
        print(row)
    print()
