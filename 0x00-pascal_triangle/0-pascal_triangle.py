#!/usr/bin/python3
"""
This module defines the pascal triangle function
"""


def pascal_triangle(n):
    """ Returns the Pascal's Triangle for a given n """
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(n - 1):
        row = list(triangle[i])
        row.insert(0, 0)
        row.append(0)
        new_row = [row[j] + row[j + 1] for j in range(len(row) - 1)]
        triangle.append(new_row)

    return triangle
