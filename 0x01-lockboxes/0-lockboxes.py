#!/usr/bin/python3
"""This Module contains canUnlockall function"""


def canUnlockAll(boxes):
    """Returns true if all the boxes are opened and false otherwise"""

    opened = [0]
    n = len(boxes)

    if n <= 1:
        return True

    for box in opened:
        for key in boxes[box]:
            if key not in opened and key in range(1, n):
                opened.append(key)
                if len(opened) == n:
                    return True

    return False
