#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(2, [5, 5, 1])))
print("Winner: {}".format(isWinner(2, [1,2])))