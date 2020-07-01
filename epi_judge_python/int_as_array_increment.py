from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # OMG OMG OMG I PASSED THE FIRST TIME!
    # OMG OMG OMG OMG OMG
    digit_to_change = len(A) - 1
    if A[digit_to_change] != 9:
        A[digit_to_change] += 1
        return A
    else:
        while A[digit_to_change] == 9:
            A[digit_to_change] = 0
            if digit_to_change == 0:
                A.insert(0, 1)
                return A
            elif A[digit_to_change - 1] != 9:
                A[digit_to_change - 1] += 1
                return A
            else:
                digit_to_change -= 1
            


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
