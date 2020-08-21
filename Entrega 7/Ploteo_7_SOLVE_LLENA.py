# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 17:06:45 2020

@author: Matias
"""
import numpy as np
from matplotlib import pyplot as plt

N=[
   2,4,8,16,
   32,64,128,256,
   512,1024,
   2048,4096,8192]


def ploteo(nombres,nombres1):
    X=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    x_label=["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
    Y=[0.01e-3,0.1e-3,1e-3,1e-2,0.1,1,10,60,60*10]
    y_label=["0.001 ms","0.1 ms","1 ms","10 ms","0,1 s","1 s","10 s", "1 min","10 min"]
    
    Nmax=8192
    DTMENS=41.53943529999924
    DTMCAL=80.49826200000098
    dtmE=[]
    dtmC=[]
    for n in N:
        dtmE.append(DTMENS)
        dtmC.append(DTMCAL)
        
    plt.figure()
    plt.subplot(2,1,1)
    for nombre in nombres: #Este va a ir cambiando
        datos=np.loadtxt(nombre)
        n= datos[:,0]
        DT=datos[:,1]
        DT1=datos[:,2]
        DT2=datos[:,3]
        DT3=datos[:,4]
        plt.loglog(n, DT.T,"k-o", alpha=0.4,markersize=3)
        plt.loglog(n, DT1.T,"k-o", alpha=0.4,markersize=3)
        plt.loglog(n, DT2.T,"k-o", alpha=0.4,markersize=3)
        plt.loglog(n, DT3.T,"k-o", alpha=0.4,markersize=3)
        plt.title("Complejidad algoritimica de SOLVE llena")
        plt.ylabel("Tiempo de ensamblado")
    
    plt.subplot(2,1,2)
    for nombre in nombres1: #Este va a ir cambiando
        datos=np.loadtxt(nombre)
        n= datos[:,0]
        DT=datos[:,1]
        DT1=datos[:,2]
        DT2=datos[:,3]
        DT3=datos[:,4]
        plt.loglog(n, DT.T,"k-o", alpha=0.4,markersize=3)
        plt.loglog(n, DT1.T,"k-o", alpha=0.4,markersize=3)
        plt.loglog(n, DT2.T,"k-o", alpha=0.4,markersize=3)
        plt.loglog(n, DT3.T,"k-o", alpha=0.4,markersize=3)
        plt.ylabel("Tiempo de solucion")
        plt.xlabel("Tamaño matriz N")
    
    plt.subplot(2,1,1)    
    plt.plot(N,dtmE, "b--")
    plt.loglog(n,n*(DTMENS/Nmax), "y--")
    plt.plot(n,n**2*(DTMENS/Nmax**2),"g--")
    plt.plot(n,n**3*(DTMENS/Nmax**3),"r--")
    plt.plot(n,n**4*(DTMENS/Nmax**4),"m--")
    plt.xticks(X,[ ])
    plt.yticks(Y,y_label)
    plt.ylim([0.000001, 600])
    plt.xlim([0, 20000])
       
    plt.subplot(2,1,2)   
    plt.plot(N,dtmC, "b--",label="Constante")
    plt.plot(n,n*(DTMCAL/Nmax), "y--",label="O(N)")
    plt.plot(n,n**2*(DTMCAL/Nmax**2),"g--",label="O(N^2)")
    plt.plot(n,n**3*(DTMCAL/Nmax**3),"r--",label="O(N^3)")
    plt.plot(n,n**4*(DTMCAL/Nmax**4),"m--",label="O(N^4)")
    plt.xticks(X,x_label,rotation=45)
    plt.yticks(Y,y_label)
    plt.ylim([0.000001, 600])
    plt.xlim([0, 20000])
    
    plt.legend(loc="upper left")
    plt.savefig("Grafico SOLVE llena.png", bbox_inches="tight")
    #plt.show()
    
nombres=["Ensamblado_SOLVE_Llena.txt"]
nombres1=["Calculo_SOLVE_Llena.txt"]
ploteo(nombres,nombres1)
