# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd
# argument (also a string).


def solution(string, ending):
    return True if string[len(string) - len(ending):] == ending else False

# Лучшее решение
# def solution(string, ending):
#     return string.endswith(ending)


