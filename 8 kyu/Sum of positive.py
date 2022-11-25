# You get an array of numbers, return the sum of all of the positives ones.


def positive_sum(arr):
    summ = 0
    for i in arr:
        if i > 0:
            summ += i
    return summ

# Лучшее решение
# def positive_sum(arr):
#    return sum(x for x in arr if x > 0)