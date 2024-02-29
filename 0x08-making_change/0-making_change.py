#!/usr/bin/python3
"""This module contains makeChange(coins, total) function"""


def makeChange(coins, total):
    """Returns the minimum number of coins to meet a given amount total"""

    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    count = 0
    i = 0
    while change < total and i < len(coins):
        if coins[i] <= total - change:
            change += coins[i]
            count += 1
        else:
            i += 1

    if change == total:
        return count
    return -1
