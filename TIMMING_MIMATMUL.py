# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 08:48:03 2020

@author: Matías
"""

import numpy as np
from time import perf_counter
from matplotlib import pyplot as plt

N=[
   2,5,10,
   12, 15, 20,
   30, 40, 45, 50, 55,
   60, 75, 100,
   125, 160, 200,
   250, 350, 500,] 

#Por un tema de tiempo lo hare hasta 500
#Deje corriendo el programa una noche entera y no supero N=1000

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

Ciclos=11
"""
for l in range(Ciclos):
    Lista_DT=[]
    Lista_N=[]
    archivo_DT=open(f"Iteracion_{l}.txt","w")
    
    for i in N :
        A = np.array(np.random.rand(i,i))
        B = np.array(np.random.rand(i,i))
        t1 = perf_counter()
        C = mimatmul(A,B)
        t2 = perf_counter()
        dt = t2 - t1
        size = 3*(i**2)*8 
        Lista_DT.append(dt)
        Lista_N.append(size)        
        archivo_DT.write(f"{i} {dt} {size}\n")
        archivo_DT.flush()
    archivo_DT.close()
"""

#0
archivo=open("Iteracion_0.txt","r")
DT0=[]
Memoria=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT0.append(S1[1])
    DT0.append(S2[1])
    Memoria.append(S1[2])
    Memoria.append(S2[2])
    DTF0=[float(x) for x in DT0]
    MF=[int(x) for x in Memoria]
    
#1  
archivo=open("Iteracion_1.txt","r")
DT1=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT1.append(S1[1])
    DT1.append(S2[1])
    DTF1=[float(x) for x in DT1]

#2
archivo=open("Iteracion_2.txt","r")
DT2=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT2.append(S1[1])
    DT2.append(S2[1])
    DTF2=[float(x) for x in DT2]

#3
archivo=open("Iteracion_3.txt","r")
DT3=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT3.append(S1[1])
    DT3.append(S2[1])
    DTF3=[float(x) for x in DT3]

#4
archivo=open("Iteracion_4.txt","r")
DT4=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT4.append(S1[1])
    DT4.append(S2[1])
    DTF4=[float(x) for x in DT4]
    
#5
archivo=open("Iteracion_5.txt","r")
DT5=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT5.append(S1[1])
    DT5.append(S2[1])
    DTF5=[float(x) for x in DT5]
    
#6
archivo=open("Iteracion_6.txt","r")
DT6=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT6.append(S1[1])
    DT6.append(S2[1])
    DTF6=[float(x) for x in DT6]

#7
archivo=open("Iteracion_7.txt","r")
DT7=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT7.append(S1[1])
    DT7.append(S2[1])
    DTF7=[float(x) for x in DT7]
    
#8
archivo=open("Iteracion_8.txt","r")
DT8=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT8.append(S1[1])
    DT8.append(S2[1])
    DTF8=[float(x) for x in DT8]
    
#9
archivo=open("Iteracion_9.txt","r")
DT9=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT9.append(S1[1])
    DT9.append(S2[1])
    DTF9=[float(x) for x in DT9]
    
#Tricks para dejarlo IDENTICO al del profesor
X=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
x_label=["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
Y=[0.1e-3,1e-3,1e-2,0.1,1,10,60,60*10]
y_label=["0.1 ms","1 ms","10 ms","0,1 s","1 s","10 s", "1 min","10 min"]


#Grafico tiempo
plt.figure()
plt.subplot(2,1,1)
plt.loglog(N,DTF0, marker = "o")
plt.loglog(N,DTF1, marker = "o")
plt.loglog(N,DTF2, marker = "o")
plt.loglog(N,DTF3, marker = "o")
plt.loglog(N,DTF4, marker = "o")
plt.loglog(N,DTF5, marker = "o")
plt.loglog(N,DTF6, marker = "o")
plt.loglog(N,DTF7, marker = "o")
plt.loglog(N,DTF8, marker = "o")
plt.loglog(N,DTF9, marker = "o")
plt.yticks(Y,y_label)
plt.title("Rendimiendo A@B")
plt.ylabel("Tiempo transcurrido (s)")
plt.grid()
plt.xticks(X,[ ]) #Elimino los valores dle eje x en el grafico 1

#Grafico memoria
plt.subplot(2,1,2)
Y2=[10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
y2=["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]
plt.loglog(N,MF, marker="o")
plt.xticks(X,x_label,rotation=45)
plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria (s)")
plt.yticks(Y2,y2)
plt.axhline(y=max(MF), xmin=0.001, xmax=0.9999,color="black",ls="--")
plt.grid()
plt.savefig("matmul1.png", bbox_inches="tight")