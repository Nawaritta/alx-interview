#!/usr/bin/python3
""" 5. Island Perimeter """


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    perim = 0
    if not grid or len(grid) == 0:
        return perim

    width = len(grid)
    height = len(grid[0])

    if width > 100 or height > 100:
        return

    for i in range(width):
        for j in range(height):
            if grid[i][j] == 1:
                if j + 1 >= height or (j + 1 < height and grid[i][j + 1] == 0):
                    perim += 1
                if j - 1 < 0 or (j - 1 >= 0 and grid[i][j - 1] == 0):
                    perim += 1
                if i + 1 >= width or (i + 1 < width and grid[i + 1][j] == 0):
                    perim += 1
                if i - 1 < 0 or (i - 1 >= 0 and grid[i - 1][j] == 0):
                    perim += 1

    return perim
