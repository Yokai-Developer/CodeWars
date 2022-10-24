# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that
# receive a list of integers as input, and return the largest and lowest number in that list, respectively.

# Examples (Input -> Output)

def minimum(arr):
    minimum = arr[0]
    for i in range(0, len(arr)):
        if minimum > arr[i]:
            minimum = arr[i]
    return minimum

def maximum(arr):
    maximum = arr[0]
    for i in range(0, len(arr)):
        if maximum < arr[i]:
            maximum = arr[i]
    return maximum

# лучшее решение
# def minimum(arr):
#     return min(arr)
#
# def maximum(arr):
#     return max(arr)