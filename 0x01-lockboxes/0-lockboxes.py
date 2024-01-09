#!/usr/bin/python3
"""This Module contains canUnlockall function"""


def canUnlockAll(boxes):
    """Returns true if all the boxes are opened and false otherwise"""
    opened = [0]
    n = len(boxes)

    for box in opened:
        for key in boxes[box]:
            if key not in opened and key in range(1, n):
                opened.append(key)
                print(key)
                if len(opened) == n:
                    return True

    return False