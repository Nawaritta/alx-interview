#!/usr/bin/python3
"""This module contains makeChange(coins, total) function"""


def makeChange(coins, total):
    """Returns the minimum number of coins to meet a given amount total"""

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    i = 0
    while i < len(coins):
        count += total // coins[i]
        total = total % coins[i]
        i += 1
        if total == 0:
            return count

    return -1
