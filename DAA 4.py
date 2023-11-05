def is_safe(board, row, col):
    # Check the current column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))

def n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_n_queens(board, 0):
        print("No solution exists.")
        return

    print("N-Queens Matrix:")
    print_board(board)

# Driver code
N = 4  # Change N as needed for the desired board size
n_queens(N)

#method 2(prefer)
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
            if row - i >= 0 and board[row - i][col - i] == 1:
                return False
            if row + i < n and board[row + i][col - i] == 1:
                return False
        return True

    def place_queen(board, col):
        if col >= n:
            solutions.append(["".join("Q" if cell == 1 else "." for cell in row) for row in board])
            return
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                place_queen(board, col + 1)
                board[i][col] = 0

    solutions = []
    board = [[0] * n for _ in range(n)]
    place_queen(board, 0)
    return solutions

# Example usage:
n = 4  # Change to the desired board size
solutions = solve_n_queens(n)
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()

