#!/usr/bin/python3
import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(n):
    def backtrack(board, col):
        if col == n:
            solutions.append([board[row][:] for row in range(n)])
            return

        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                backtrack(board, col + 1)
                board[row][col] = ' '

    solutions = []
    board = init_board(n)
    backtrack(board, 0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)
