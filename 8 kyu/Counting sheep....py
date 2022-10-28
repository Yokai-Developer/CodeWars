# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the
# number of sheep present in the array (true means present).

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count += 1
    return count

# Лучшее решение
# def count_sheeps(arrayOfSheeps):
#   return arrayOfSheeps.count(True)