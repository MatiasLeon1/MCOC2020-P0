# Entrega 7

## 1. Complejidad algorítmica de `MATMUL`
   ### 1.1 Matriz Laplaciana llena
   ![Grafico MATMUL llena](https://user-images.githubusercontent.com/43649125/90902601-b63ad880-e39a-11ea-98fb-9c1230250c35.png)
   ### 1.2 Matriz Laplaciana Dispersa
   ![Grafico MATMUL Disp](https://user-images.githubusercontent.com/43649125/90902612-baff8c80-e39a-11ea-9973-1ff6f040edd0.png)

## 2. Complejidad algorítmica de `SOLVE`
   ### 2.1 Matriz Laplaciana llena
  ![Grafico SOLVE llena](https://user-images.githubusercontent.com/43649125/90902627-c05cd700-e39a-11ea-937c-80bfd3bf1e27.png)
   ### 2.2 Matriz Laplaciana Dispersa
  ![Grafico SOLVE Disp](https://user-images.githubusercontent.com/43649125/90902638-c3f05e00-e39a-11ea-9fdb-0fbb2bbd3641.png)

## 3. Complejidad algorítmica de `INV`
   ### 3.1 Matriz Laplaciana llena
  ![Grafico INV llena](https://user-images.githubusercontent.com/43649125/90902655-c81c7b80-e39a-11ea-83d9-cb155864961b.png)
   ### 3.2 Matriz Laplaciana Dispersa
  ![Grafico INV Dispersa](https://user-images.githubusercontent.com/43649125/90902667-cc489900-e39a-11ea-8b50-bb8f70e039ff.png)

## Analisis
* Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.
   * Como se mencionó en clases, optimizar el código es necesario y debe ser un objetivo a perseguir constantemente. El ejemplo de la matriz Laplaciana dispersa sirve mucho para contextualizar qué sucede cuando quitamos estos datos "innecesarios" (los ceros en este caso). Se observa en los 3 casos que el tiempo de cálculo de la matriz Laplaciana dispersa es muy inferior al de la matriz Laplaciana llena. En el caso de ensamblaje los tiempos son muy similares, ya que a partir de la matriz Laplaciana llena yo creo una dispersa, por lo que en primer lugar se tuvo que crear la matriz con todos los ceros y posteriormente removerlos. Lo anterior no corresponde a lo que uno esperaría en un código "optimizado", sin embargo me vi envuelto en una dificultad al momento de trabajar con `lil_matrix`.
* ¿Cual parece la complejidad asintótica (N → ∞)  para el ensamblado y solución en ambos casos y porqué?
   * Para el caso del ensamblado, la complejidad asintótica cuando N tiende al infinito se asemeja a `O(N^2)` en los 3 casos y para ambos tipos de matrices Laplacianas (llenas y dispersas). Esto significa que existe una constante (Cu por ejemplo) tal que la operación de 2 int de hasta N dígitos puede realizarse en menos tiempo que Cu_x_N^2. De la misma manera existe una constante (Cl por ejemplo) tal que las mismas operaciones pueden realizarse en mayor tiempo que Cl_x_N^2. De ambas surge `O(N^2)` y la finalidad es modelar el peor caso complejo posible y el caso complejo promedio para predecir cómo se comportará el cálculo que se desea realizar. Termino diciendo que la complejidad asintóticas era de esperarse que fuera igual en todos los casos debido a la forma en la que se ensamblo, y que fue mencionada anteriormente.
   * Para el caso del cálculo o solución, se observaron diferencias sustanciales. Todas las matrices Laplacianas llenas en los 3 métodos tuvieron una complejidad asintótica tendiendo a `O(N^3)`, lo que indica que a medida que N aumenta, el tiempo de cálculo iba creciendo de manera que la solución corresponde a la multiplicación de una constante por N^3. Esto demuestra una complejidad más elevada que la de la generación de matrices, pero es esperable ya que se deben operar elementos entre sí. Nuevamente la similitud era esperable debido a que las 3 matrices eran Laplacianas llenas de ceros.
   Para el caso de las matrices Laplacianas dispersas se observaron cambios. La complejidad asintótica de mejor resultado se dio en la complejidad algorítmica de MATMUL con la matriz Laplaciana dispersa. Su complejidad asintótica tendió a una `Constante`, lo que significa que el tiempo de cálculo cuando N tiende a infinito se mantuvo igual. Este es un resultado importante ya que significa que el PC es capaz de ejecutar esta operación al mismo tiempo sin importar el tamaño de N. Para el caso de SOLVE e INV, la matriz Laplaciana dispersa tuvo una complejidad asintótica con tendencia a `O(N)`. Si bien no es tan buen resultado como N=cte, se observa que es mucho mejor que la complejidad asintótica tanto para ensamblar matrices como para calcular matrices llenas. Esto corrobora el hecho de que trabajar con matrices dispersas ayuda enormemente a optimizar el código y su ejecución.
* ¿Cómo afecta el tamaño de las matrices al comportamiento aparente?
   * En casi todos los casos, a mayor N mayor tiempo de solución y ensamblado. Lo cual posee una concordancia lógica, pues se está aumentando el tamaño de la variable a trabajar por parte del PC
* ¿Qué tan estables son las corridas (se parecen todas entre sí siempre, nunca, en un rango)?
   * Las corridas fueron increíblemente estables, si consideramos las entregas anteriores donde se apreciaba una variación más notoria. Interesante es el hecho de poder observar claramente cuando la cache de mi computador pasa de L1 a L2, donde se logra apreciar un salto en las corridas. A medida que N aumenta la estabilidad crece, en parte porque la diferencia se vuelve poco apreciable en valores tan grandes. En valores de N chicos, se puede apreciar más claro esto debido a lo pequeños que son los límites. Si se pudiera hacer un zoom grande al gráfico se podría observar de mejor manera cómo varían las corridas entre sí.

## Codigo Ensamblaje Matriz
   **def** Matriz_Laplaciana_Llena(N, dtype=np.double):
    A= np.zeros([N,N], dtype=dtype)
    
    **for** i in range(N):
        **for** j in range(N):
            **if** i == j:
                A[i,j]= 2
            **if** i+1 == j:
                A[i,j]= -1
            **if** i-1 == j:
                A[i,j]= -1
    
    return A
