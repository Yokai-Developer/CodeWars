# Can you find the needle in the haystack?
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so:
# Example(Input --> Output)


def find_needle(haystack):
    for i in haystack:
        if i == 'needle':
            return 'found the needle at position {}'.format(haystack.index('needle'))

# Лучшее решение:
# def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')
