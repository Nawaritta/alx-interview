#!/usr/bin/python3
"""This module contains rotate_2d_matrix function"""


def rotate_2d_matrix(mat):
    """rotates a mat 90 degrees clockwise """
    n = len(mat)

    for r in range(n):
        for c in range(r, n):
            mat[c][r], mat[r][c] = mat[r][c], mat[c][r]

    for r in range(n):
        for c in range(n//2):
            mat[r][c], mat[r][n - c - 1] = mat[r][n - c - 1], mat[r][c]
