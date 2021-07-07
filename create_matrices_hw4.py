# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 13:59:07 2021

@author: Mane
"""

import random


def create_matrix(filename, shape):
    """
    Creates random matrix with n = shape[0], m = shape[1] and stores to filename
    """
    matrix = []

    for i in range(shape[0]):
        matrix.append([])
        for _ in range(shape[1]):
            matrix[i].append(random.randint(1, shape[1]))

    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(lambda x: str(x), row)))
            f.write('\n')


if __name__ == '__main__':
    create_matrix('A.txt', (10, 10))
    create_matrix('B.txt', (10, 10))
