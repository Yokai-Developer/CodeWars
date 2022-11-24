# Complete the square sum function so that it squares each number passed into it and then sums the results together.


def square_sum(numbers):
    summ = 0
    for i in numbers:
        summ += i ** 2
    return summ

# Лучшее решение
# def square_sum(numbers):
#    return sum(x ** 2 for x in numbers)