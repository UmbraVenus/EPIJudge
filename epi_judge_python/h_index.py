from typing import List

from test_framework import generic_test

# Notes at bottom
def h_index(citations: List[int]) -> int:
    # TODO - you fill in here.
    """ first passed code
    citations.sort()
    for x in range(len(citations)):
        if citations[x] >= len(citations) - x:
            return len(citations) - x
    return 0
    """
    citations.sort()
    n = len(citations) # assigning a variable for constant time!!!
    for index, value in enumerate(citations):
        if value >= n - index:
            return n - index
    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))

"""
My first thought:
Start from works with the largest cited number, keep adding the number of works,
and loop through the entire encounter till the works is equal to those of cited numbers. (really no matter from looping from the beginning?)
"""
"""
Book recommended method:
When the cited number equal to the number of those of lefted books
"""
"""
My second thought:
Why not do a reverse sort?
"""
"""
Conclusion: Obviously the book's algorithm is much better
"""