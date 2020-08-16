# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:25:14 2020

@author: Matias
"""

import numpy as np
from time import perf_counter
import scipy.linalg as spLinalg
N=[
   2,4,5,10,
   12, 15,18, 20,
   30, 40, 45, 50, 55,
   60, 75, 100,
   125, 160, 200,
   250, 350, 500, 600, 800,
   1000, 1500, 2000,
   3000,5000, 7500, 10000]

def Matriz_Laplaciana(N, dtype=np.single):
    A= np.zeros([N,N], dtype=dtype)
    
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i,j]= 2
            if i+1 == j:
                A[i,j]= -1
            if i-1 == j:
                A[i,j]= -1
    
    return A

Corridas=5

nombres=["Ainv_X_B.txt","Ainv_X_npSolve.txt","Ainv_X_spSolve.txt","Ainv_X_spSolve_symmetric.txt","Ainv_X_spSolve_pos.txt","Ainv_X_spSolve_pos_overwrite.txt"]

archivos=[open(nombre,"w") for nombre in nombres]

for n in N:
    DT=np.zeros((Corridas, len(archivos))) #Lista vacia donde iran los dt    
    
    for i in range(Corridas):
        
        #INVIRTIENDO
        A=Matriz_Laplaciana(n)
        B=np.ones(n)
        t1=perf_counter()
        Inv_A=np.linalg.inv(A)
        Inv_AxB=A@B
        t2=perf_counter()
        dt=t2-t1
        DT[i][0]=dt
        
        #NP.LINALG.SOLVE
        A=Matriz_Laplaciana(n)
        B=np.ones(n)
        t1=perf_counter()
        Inv_AxB=np.linalg.solve(A,B)
        t2=perf_counter()
        dt=t2-t1
        DT[i][1]=dt
        
        #CAMBIAR VARIABLES
        
        #SP.SOLVE
        A=Matriz_Laplaciana(n)
        B=np.ones(n)
        t1=perf_counter()
        Inv_AxB_sc=spLinalg.solve(A,B)
        t2=perf_counter()
        dt=t2-t1
        DT[i][2]=dt
        
        #SP.SOLVE_SYMMETRIC
        A=Matriz_Laplaciana(n)
        B=np.ones(n)
        t1=perf_counter()
        Inv_AxB_sym=spLinalg.solve(A, B, assume_a='sym')
        t2=perf_counter()
        dt=t2-t1
        DT[i][3]=dt
        
        #SP.SOLVE_POS
        A=Matriz_Laplaciana(n)
        B=np.ones(n)
        t1=perf_counter()
        Inv_AxB_pos= spLinalg.solve(A, B, assume_a='pos')
        t2=perf_counter()
        dt=t2-t1
        DT[i][4]=dt
        
        #SP.SOLVE_POS_OVERWRITE
        A=Matriz_Laplaciana(n)
        B=np.ones(n)
        t1=perf_counter()
        Inv_AxB_pos_owrt= spLinalg.solve(A, B, assume_a='pos', overwrite_a=True )
        t2=perf_counter()
        dt=t2-t1
        DT[i][5]=dt
    
    print(f"dt's: {DT}")
       
    DT_promedio= [np.mean(DT[:,j]) for j in range(len(archivos))]
    #DT_promedio= np.mean(DT, axis=0)
    print(f"Promedio: {DT_promedio}")
    
    #Escritura en archivos
    for j in range(len(archivos)):
        archivos[j].write(f"{n} {DT_promedio[j]}\n")
        archivos[j].flush()

[archivo.close() for archivo in archivos]
