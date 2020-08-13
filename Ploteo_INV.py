# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:35:33 2020

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

#ARCHIVO HALF
archivo=open("Iteracion_Half.txt","r")
DT_SCF0=[]
DT_SCT0=[]
MEM0=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT_SCF0.append(S1[0])
    DT_SCF0.append(S2[0])
    DT_SCT0.append(S1[1])
    DT_SCT0.append(S2[1])
    MEM0.append(S1[2])
    MEM0.append(S2[2])
    DT_SCF0F=[float(x) for x in DT_SCF0]
    DT_SCT0F=[float(x) for x in DT_SCT0]
    MEM0F=[int(x) for x in MEM0 ]


#ARCHIVO SINGLE
archivo=open("Iteracion_Single.txt","r")
DT_NP1=[]
DT_SCF1=[]
DT_SCT1=[]
MEM1=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT_NP1.append(S1[0])
    DT_NP1.append(S2[0])
    DT_SCF1.append(S1[1])
    DT_SCF1.append(S2[1])
    DT_SCT1.append(S1[2])
    DT_SCT1.append(S2[2])
    MEM1.append(S1[3])
    MEM1.append(S2[3])
    DT_NP1F=[float(x) for x in DT_NP1]
    DT_SCF1F=[float(x) for x in DT_SCF1]
    DT_SCT1F=[float(x) for x in DT_SCT1]
    MEM1F=[int(x) for x in MEM1 ]

#ARCHIVO DOUBLE
archivo=open("Iteracion_Double.txt","r")
DT_NP2=[]
DT_SCF2=[]
DT_SCT2=[]
MEM2=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT_NP2.append(S1[0])
    DT_NP2.append(S2[0])
    DT_SCF2.append(S1[1])
    DT_SCF2.append(S2[1])
    DT_SCT2.append(S1[2])
    DT_SCT2.append(S2[2])
    MEM2.append(S1[3])
    MEM2.append(S2[3])
    DT_NP2F=[float(x) for x in DT_NP2]
    DT_SCF2F=[float(x) for x in DT_SCF2]
    DT_SCT2F=[float(x) for x in DT_SCT2]
    MEM2F=[int(x) for x in MEM2 ]

#ARCHIVO LONGDOUBLE
archivo=open("Iteracion_LongDouble.txt","r")
DT_SCF3=[]
DT_SCT3=[]
MEM3=[]
for i in archivo:
    idea=archivo.readline()
    S2=idea.split(" ")
    S1=i.split(" ")
    DT_SCF3.append(S1[0])
    DT_SCF3.append(S2[0])
    DT_SCT3.append(S1[1])
    DT_SCT3.append(S2[1])
    MEM3.append(S1[2])
    MEM3.append(S2[2])
    DT_SCF3F=[float(x) for x in DT_SCF3]
    DT_SCT3F=[float(x) for x in DT_SCT3]
    MEM3F=[int(x) for x in MEM3 ]
   
#Tricks para dejarlo IDENTICO al del profesor
X=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
x_label=["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
Y=[0.1e-3,1e-3,1e-2,0.1,1,10,60,60*10]
y_label=["0.1 ms","1 ms","10 ms","0,1 s","1 s","10 s", "1 min","10 min"]

#GRAFICO HALF
#Tiempo
plt.figure()
plt.subplot(2,1,1)
#plt.loglog(N,DT_NP3F, marker = "o", label = "Numpy.linalg")        #Voy cambiando
#EJEMPLO DE COMO NO PLOTEO LOS NP QUE NO PUDE TRABAJAR
plt.loglog(N,DT_SCF3F, marker = "o", label="Scipy.linalg False")    #variables
plt.loglog(N,DT_SCT3F, marker = "o", label="Scipy.linalg True")     #a medida
plt.legend(loc="upper left")                                        #que grafico
plt.yticks(Y,y_label)
plt.title("Desempeño INV con np.Longdouble")
plt.ylabel("Tiempo transcurrido (s)")
plt.grid()
plt.xticks(X,[ ]) #Elimino los valores dle eje x en el grafico 1
#Grafico memoria
plt.subplot(2,1,2)
Y2=[10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10,10**11]
y2=["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100GB"]
plt.loglog(N,MEM3F, marker="o")
plt.xticks(X,x_label,rotation=45)
plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria")
plt.yticks(Y2,y2)
plt.axhline(y=256000, xmin=0.001, xmax=0.9999,color="black",ls="--")
plt.axhline(y=2000000, xmin=0.001, xmax=0.9999,color="black",ls="--")
plt.axhline(y=max(MEM3F), xmin=0.001, xmax=0.9999,color="black",ls="--")
plt.grid()
plt.savefig("Desempeño_NPLONGDOUBLE.png", bbox_inches="tight")
