from test_framework import generic_test


def parity(x: int) -> int:
    b = bin(x)
    sub = "1"
    count = b.count(sub)
    if count % 2 == 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
