# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
# Input will always be valid, i.e. no negative integers.


def count_sheep(n):
    stroka = ''
    if n == 0:
        return ''
    else:
        for i in range(1, n + 1):
            stroka += str(i) + ' sheep...'
        return stroka

# Лучшее решение
# def count_sheep(n):
#     return ''.join(f"{i} sheep..." for i in range(1,n+1))
