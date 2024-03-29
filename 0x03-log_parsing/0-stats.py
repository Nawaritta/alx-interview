#!/usr/bin/python3
"""This module contains compute metrics function"""


def print_stats(size, status_codes):
    """Reads from standard input and computes metrics"""
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


def parse_line(line, status_codes):
    """Parses the line"""
    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line = line.split()
    try:
        size = int(line[-1])
    except (IndexError, ValueError):
        size = 0

    try:
        if line[-2] in possible_codes:
            if line[-2] in status_codes:
                status_codes[line[-2]] += 1
            else:
                status_codes[line[-2]] = 1
    except IndexError:
        pass

    return size


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    count = 0
    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:

            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1
            size += parse_line(line, status_codes)

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
