#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
student: Lior Silberman
id: 316456623
‪Assignmen‫‪t no. 3
Program: matrix.py‬‬
"""

def matrix_scalar_mult(matrixA, num):
    '''
    return sum of matrix*number
    '''
    # calculate matrix*number
    c = [[i*int(num_c) for i in j] for j in matrixA]
    return c
    
def matrix_add(matrixA, matrixB):
    '''
    get two matrix and return sum
    '''
    # calculate matrix1+matrix2
    m3 = [[matrixA[i][k]+matrixB[i][k] for i in range(len(matrixA))] for k in range(len(matrixB))]
    return m3   
           
def matrix_mult(matrixA, matrixB):
    '''
    get two matrix and multiply them
    '''
    # calculate matrix1*matrix2
    m3 = [[sum(matrixA[i][k]*matrixB[k][j] for k in range(len(matrixB))) for j in range(len(matrixB[0]))] for i in range(len(matrixA))]
    return m3

def identy_matrix(num):
    '''
    get number and return identy matrix
    '''
    # calculate identy matrix
    mat = [[0]*i + [1] + [0]*(num-i-1) for i in range(num)]
    return mat

def matrix_polynom(lst,matrix):
    '''
    placing a matrix in a polynom and claculate
    '''
    mat = [identy_matrix(len(matrix)),matrix]
    prev_mat = matrix
    next_mat = matrix
    for i in range(2,len(lst)):
        mat[i] = (matrix_mult(prev_mat,next_mat))
        mat.append(mat[i])
        next_mat = mat[i]
    
    _sum = []
    for num in range(len(lst)):
        _sum.append(matrix_scalar_mult(mat[num]),lst[num])
        
    res = [[0 for x in range(n)] for y in range(n)]
    for i in _sum:
        res += matrix_add(res, i)
    

if __name__ == "__main__":
    #print(matrix_scalar_mult([[1,2,3],[4,5,6],[7,8,9]],input("num")))
    #print(matrix_add([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]))
    #print(matrix_mult([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]))
    #print(identy_matrix(int(input("num:"))))
    