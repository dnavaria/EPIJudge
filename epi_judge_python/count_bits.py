from test_framework import generic_test


def count_bits(x: int) -> int:
    
    # Using Brian keringhan's Algorithms
    """
        - Flipping the rightmost bit in each iterations
        - Ex: x = 5
            - itreration 1: x = 5 => 101, 5 & 4 = 4, cnt = 1, x = 4
            - itreration 2: x = 4 => 101, 4 & 3 = 3, cnt = 2, x = 0
            - Exit
    """
    cnt = 0
    while x:
        x = x & (x -1)
        cnt+=1
    return cnt


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
