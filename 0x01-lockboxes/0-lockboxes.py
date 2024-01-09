#!/usr/bin/python3

def canUnlockAll(boxes):
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

