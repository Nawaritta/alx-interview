#!/usr/bin/python3
""" This module contains validUTF8(data) function """


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False"""

    def num_following_bytes(byte):
        if (byte & 0b11110000) == 0b11110000:
            return 3
        elif (byte & 0b11100000) == 0b11100000:
            return 2
        elif (byte & 0b11000000) == 0b11000000:
            return 1
        else:
            return 0

    i = 0
    while i < len(data):
        current_byte = data[i]

        if current_byte & 0b10000000 != 0b00000000:
            return False

        num_bytes = num_following_bytes(current_byte)

        if i + num_bytes >= len(data):
            return False

        for j in range(i + 1, i + 1 + num_bytes):
            if (data[j] & 0b11000000) != 0b10000000:
                return False

        i += num_bytes + 1

    return True
