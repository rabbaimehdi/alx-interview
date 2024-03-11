#!/usr/bin/python3

def pascal_triangle(n):
    """returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    result = []
    if n > 0:
        for i in range(1, n + 1):
            niveau = []
            C = 1
            for j in range(1, i + 1):
                niveau.append(C)
                C = C * (i - j) // j
            result.append(niveau)
    return result
