#!/usr/bin/python3
"""This module contains minOperations function"""


def minOperations(n):
    """calculates the fewest number of operations needed to result
    in exactly n H characters in the file."""

    count = 0
    nh = 1
    copied = 0

    while (nh != n):
        if (n % nh == 0):
            count += 2
            copied = nh
            nh *= 2
        else:
            count += 1
            nh += copied

    return count
