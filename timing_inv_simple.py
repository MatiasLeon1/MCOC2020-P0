# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:50:41 2020

@author: Matías
"""

import numpy as np
from time import perf_counter
import scipy as sc
from scipy import linalg
from matplotlib import pyplot as plt

N=[
   3,4,5,10,
   12, 15,18, 20,
   30, 40, 45, 50, 55,
   60, 75, 100,
   125, 160, 200,
   250, 350, 500, 600, 800,
   1000, 2000, 5000, 10000]

def Matriz_Laplaciana(N, dtype=np.simple):
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
   

DT21=[]   
DT22=[]
DT23=[]
Memoria=[]
archivo=open("Iteracion_simple.txt","w")  #Guarde 4 archivos para los 4 tipos
for i in N:                               #Half
    Matriz3 = Matriz_Laplaciana(i)        #Single
    t01=perf_counter()                   #Double
    InvNP1=np.linalg.inv(Matriz3)        #Longdouble
    t02=perf_counter()
    dt01=t02-t01
    t011=perf_counter()
    InvSC=sc.linalg.inv(Matriz3)
    t022=perf_counter()
    dt02=t022-t011
    t031=perf_counter()
    InvSC1=sc.linalg.inv(Matriz3, overwrite_a=True, check_finite=True)
    t032=perf_counter()
    dt03=t032-t031
    size=2*(i**2)*32 #Cambie el calculo dependiendo del tipo.
    archivo.write(f"{dt01} {dt02} {dt03} {size}\n")
    DT21.append(dt01)
    DT22.append(dt02)
    DT23.append(dt03) 
    
    Memoria.append(size)
    archivo.flush()
archivo.close()

#Memoria:
   #HALF:
       #2*(i**2)*16
   #SINGLE:
       #2*(i**2)*32
   #DOUBLE:
       #2*(i**2)*64
   #LONG DOUBLE:
       #2*(i**2)*128
