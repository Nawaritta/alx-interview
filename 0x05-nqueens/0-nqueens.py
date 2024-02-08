#!/usr/bin/python3
"""
Solves the N queens puzzle which is the challenge of placing
N non-attacking queens on an NN chessboard.
"""

import sys


def not_attacked(board, row, col, N):
    """
    Check if it's safe to place a queen at the given position on the board.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def backtracking_algo(board, col, N):
    """
    Solve the N-Queens problem using backtracking.
    """
    if col == N:
        print_solution(board, N)
        return True

    for i in range(N):
        if not_attacked(board, i, col, N):
            board[i][col] = 1
            backtracking_algo(board, col + 1, N)
            board[i][col] = 0


def print_solution(board, N):
    """
    Print a valid solution to the N-Queens problem.
    """
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def main():
    """
    Main function: solve N-Queens puzzle
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]

    backtracking_algo(board, 0, N)


if __name__ == '__main__':
    main()
