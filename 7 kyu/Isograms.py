# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
# Ignore letter case.


def is_isogram(string):
    lower = string.lower()
    for i in lower:
        count = 0
        count += lower.count(i)
        if count > 1:
            return False
    return True

# Лучшее решение
# def is_isogram(string):
#    return len(string) == len(set(string.lower()))
