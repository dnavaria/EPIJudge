from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if len(square_matrix) == 0:
        return []
    nRows = len(square_matrix)
    mCols = len(square_matrix[0])
    if nRows == 0 and mCols == 0:
        return
    tn = 0
    x,y = 0,0
    fy = 1
    dx = 1
    by = 1
    ux = 1
    arr = []
    while tn < nRows:
        while y < mCols - fy:
            arr.append(square_matrix[x][y])
            y+=1

        fy+=1
        while x < nRows - dx:
            arr.append(square_matrix[x][y])
            x+=1
        dx+=1

        while y >= by:
            arr.append(square_matrix[x][y])
            y-=1
        by+=1

        while x > ux:
            arr.append(square_matrix[x][y])
            x-=1
        ux+=1    

        tn+=1
        
    arr.append(square_matrix[x][y])
    return arr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
