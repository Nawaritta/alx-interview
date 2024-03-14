#!/usr/bin/python3
"""This module contains isWinner function"""


def count_primes(n):
    is_prime = [True] * (n+1)
    count = 0

    for num in range(2, int(n**0.5)+1):
        if is_prime[num]:
            count += 1
            for multiple in range(num*num, n+1, num):
                is_prime[multiple] = False

    for num in range(int(n**0.5)+1, n+1):
        if is_prime[num]:
            count += 1

    return count


def isWinner(x, nums):
    """ determines the winner of a game of prime numbers."""

    score = {"Maria": 0, "Ben": 0}

    if x > len(nums) or x < 1 or not nums:
        return None

    for i in nums:
        if count_primes(i) % 2 == 0:
            score["Ben"] += 1
        else:
            score["Maria"] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    if score["Maria"] == score["Ben"]:
        return None
    return "Ben"
