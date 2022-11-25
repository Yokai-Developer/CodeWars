# Given a non-empty array of integers, return the result of multiplying the values together in order.

def grow(arr):
    sum = 1
    for i in arr:
        sum *= i
    return sum

# Лучшее решение
# from functools import reduce
#
# def grow(arr):
#     return reduce(lambda x, y: x * y, arr)