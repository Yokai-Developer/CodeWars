# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.


def abbrev_name(name):
    name = name.upper()
    str = name.split()
    return str[0][0] + '.' + str[1][0]

# Лучшее решение
# def abbrevName(name):
#     return '.'.join(w[0] for w in name.split()).upper()
