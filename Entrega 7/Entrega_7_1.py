# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:26:21 2020

@author: Matias
"""

import numpy as np
from time import perf_counter

from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve, inv


N=[
   2,4,8,16,
   32,64,128,256,
   512,1024,
   2048,4096,8192
   ]


def Matriz_Laplaciana_Llena(N, dtype=np.double):
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

nombres=["Ensamblado_MATMUL_Llena.txt","Calculo_MATMUL_Llena.txt",
         "Ensamblado_MATMUL_Disp.txt","Calculo_MATMUL_Disp.txt",
         "Ensamblado_SOLVE_Llena.txt","Calculo_SOLVE_Llena.txt",
         "Ensamblado_SOLVE_Disp.txt","Calculo_SOLVE_Disp.txt",
         "Ensamblado_INV_Llena.txt","Calculo_INV_Llena.txt",
         "Ensamblado_INV_Disp.txt","Calculo_INV_Disp.txt",
         ]

archivos=[open(nombre,"w") for nombre in nombres]

for n in N:
    DT=np.zeros((Corridas, len(archivos))) #Lista vacia donde iran los dt    
    
    for i in range(Corridas):
        
        #MATMUL
            #LLENAS   
            #Ensmblaje
            t1=perf_counter()
            A=Matriz_Laplaciana_Llena(n)
            B=Matriz_Laplaciana_Llena(n)
            t2=perf_counter() 
            #Calculo
            MatMulLL=A@B
            t3=perf_counter()
            dt=t2-t1
            dt2=t3-t2
            DT[i][0]=dt #Ensamblado        
            DT[i][1]=dt2 #Calculo
            
            #DISPERSAS
            #Ensmblaje
            t1=perf_counter()
            A=csr_matrix(Matriz_Laplaciana_Llena(n)) #ESTOY TRABAJANDO CON
            B=csr_matrix(Matriz_Laplaciana_Llena(n)) #LA FUNCION LLENA
            t2=perf_counter() 
            #Calculo
            MatMulDisp=A@B
            t3=perf_counter()
            dt=t2-t1
            dt2=t3-t2
            DT[i][2]=dt #Ensamblado        
            DT[i][3]=dt2 #Calculo
            
        #SOLVE
            #LLENAS   
            #Ensmblaje
            t1=perf_counter()
            A=Matriz_Laplaciana_Llena(n)
            B=np.ones(n)
            t2=perf_counter() 
            #Calculo
            MatMulLL=np.linalg.solve(A,B)
            t3=perf_counter()
            dt=t2-t1
            dt2=t3-t2
            DT[i][4]=dt #Ensamblado        
            DT[i][5]=dt2 #Calculo
            
            #DISPERSAS
            #Ensmblaje
            t1=perf_counter()
            A=csr_matrix(Matriz_Laplaciana_Llena(n)) #ESTOY TRABAJANDO CON
            B=np.ones(n) #LA FUNCION LLENA
            t2=perf_counter() 
            #Calculo
            MatMulDisp=spsolve(A,B)
            t3=perf_counter()
            dt=t2-t1
            dt2=t3-t2
            DT[i][6]=dt #Ensamblado        
            DT[i][7]=dt2 #Calculo
        
        #INVERSA
            #LLENA
            #Ensamblaje
            t1=perf_counter()
            A=Matriz_Laplaciana_Llena(n)
            t2=perf_counter() 
            #Calculo
            Inv_A=np.linalg.inv(A)
            t3=perf_counter()
            dt=t2-t1
            dt2=t3-t2
            DT[i][8]=dt #Ensamblado        
            DT[i][9]=dt2 #Calculo
            
            #DISPERSAS
            #Ensamblaje
            t1=perf_counter()
            A1=csr_matrix(Matriz_Laplaciana_Llena(n))
            t2=perf_counter() 
            #Calculo
            Inv_A=inv(A1)
            t3=perf_counter()
            dt=t2-t1
            dt2=t3-t2
            DT[i][10]=dt #Ensamblado        
            DT[i][11]=dt2 #Calculo   
    
    print(DT)
    
    #Escritura en archivos
    for j in range(len(archivos)):
        lista_datos = [str(DT[k][j]) for k in range(Corridas)]
        datos = " ".join(lista_datos)
        archivos[j].write(f"{n} {datos}\n")
        archivos[j].flush()

[archivo.close() for archivo in archivos]
                  
  