# Write a function to split a string and convert it into an array of words.

def string_to_array(s):
    return s.split() if s != '' else ['']

# Лучшее решение
# def string_to_array(s):
#    return s.split(' ')
