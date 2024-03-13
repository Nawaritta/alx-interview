#!/usr/bin/python3
"""This module contains isWinner function"""


def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """ determines the winner of a game of prime numbers."""

    nums.sort()
    cursor = 0
    count = 0
    score = {"Maria": 0, "Ben": 0}
    i = 1
    if x == 0:
        return None

    while i < nums[-1] + 1:

        if is_prime(i):
            count += 1

        if i == nums[cursor]:

            if count % 2 == 0:
                score["Ben"] += 1
            else:
                score["Maria"] += 1
            cursor += 1
            if cursor == x:
                break
        else:
            i += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    if score["Maria"] == score["Ben"]:
        return None
    return "Ben"
