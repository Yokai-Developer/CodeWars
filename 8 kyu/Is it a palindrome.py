# Write a function that checks if a given string (case insensitive) is a palindrome.

def is_palindrome(s):
    s = s.lower()
    _s = s[::-1]
    return True if s == _s else False


# Лучшее решение
# def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]