# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:49:51 2020

@author: Matias
"""
import numpy as np
from matplotlib import pyplot as plt

N=[
   2,4,5,10,
   12, 15,18, 20,
   30, 40, 45, 50, 55,
   60, 75, 100,
   125, 160, 200,
   250, 350, 500, 600, 800,
   1000, 2000, 5000, 10000]


def ploteo(nombres):
    X=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    x_label=["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
    Y=[0.1e-3,1e-3,1e-2,0.1,1,10,60,60*10]
    y_label=["0.1 ms","1 ms","10 ms","0,1 s","1 s","10 s", "1 min","10 min"]
    
    plt.figure()
    
    for nombre in nombres:
        datos=np.loadtxt(nombre)
        n= datos[:,0]
        DT=datos[:,1]
        plt.loglog(n, DT.T, marker = "o", label = nombre)
        plt.ylabel("Tiempo transcurrido [s]")
        plt.xlabel("Tamaño matriz N")
        plt.grid(True)
        plt.xticks(X,x_label,rotation=45)
        plt.yticks(Y,y_label)
    
    plt.tight_layout()
    plt.legend()
    plt.show()
  
nombres=["Ainv_X_B.txt-2","Ainv_X_npSolve-2.txt"]
ploteo(nombres)