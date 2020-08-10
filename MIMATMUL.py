# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def mimatmul(A,B):
    f=len(A) 
    c=len(B)
    result=np.zeros([f,c]) #Creamos una matriz de puros ceros
    for i in range(len(A)): #Itera las filas de la matriz A
        for j in range(len(B[0])): #Itera las columnas de B
            for k in range(len(B)): #Itera las filas de B
                # Utilizamos la formula de calculo de matrices ordenando
                # el calculo entre dilas y columnas respectivas
                result[i][j] += A[i][k]*B[k][j] 
    return result


