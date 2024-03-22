#!/usr/bin/python3
"""
Module for 0-minoperations
"""


def minOperations(n):
    """ 
    Return the fewest operations needed to result in n H characters
    """
    if n == 1:
        return 0

    operations = 0
    clipboard = 1
    buffer = 1

    while buffer < n:
        if n % buffer == 0:
            clipboard = buffer
            operations += 1
        buffer += clipboard
        operations += 1

    if buffer == n:
        return operations
    else:
        return 0
