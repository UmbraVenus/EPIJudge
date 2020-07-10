from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    end = [0]
    digit = 0
    #reverse num1 and num2 the first time
    for j in reversed(range(len(num2))):
        for i in reversed(range(len(num1))):
            result = num1[i] * num2[j]
            if result + end[digit] >= 10:
                end[digit] = end[digit] + result % 10
                end[digit + 1] = result // 10
            else:
                end[digit] = end[digit] + result
            digit += 1
    end.reverse()
    end[0] = sign * end[0]
    return end
    
                

    



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
