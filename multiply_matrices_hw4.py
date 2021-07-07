# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 14:03:08 2021

@author: Mane
"""

def multiply_matrices(A,B):
    n=len(A)
    m=len(A[0])
    k=len(B)
    C = []
    if len(A) != len(B[0]):
        print("Two matrices can't be multiplied")
    else:
        for i in range(m):
            C.append([])
            for j in range(k):
                sum=0
                for t in range(n):
                    s=A[i][t]*B[t][j]
                    sum=sum+s
                C[i].append(sum)
        return C

def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            matrix.append(list(map(int,line.split())))
    return matrix
    
    
def write_matrix_to_file(matrix,filename):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(lambda x: str(x), row)))
            f.write('\n')

    
####check multiplication         
#A=[[1,0],[0,1]]
#B=[[1,1],[3,3]]
#C=multiply_matrices(A, B)
#print(C)

if __name__ == '__main__':
    A_matrix = read_matrix_from_file('A.txt')
    B_matrix = read_matrix_from_file('B.txt')
    C_matrix = multiply_matrices(A_matrix, B_matrix)
    write_matrix_to_file(C_matrix, 'result.txt')
    print(C_matrix)
