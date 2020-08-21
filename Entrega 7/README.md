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
   * Como se mencionó en clases, optimizar el codigo es necesario y debe ser un objetivo a perseguir constantemente. El ejemplo de la matriz Laplaciana dispersa sirve mucho para contextualizar que sucede cuando quitamos estos datos "innecesarios" (los ceros en este caso). Se observa en los 3 casos que el tiempo de cálculo de la matriz Laplaciana dispersa es muy inferior al de la matriz Laplaciana llena. En el caso de ensamblaje los tiempos son muy similares ya que a partir de la matriz Laplaciana llena yo cree una dispersa, por lo que en primer lugar se tuvo que crear la matriz con todos los ceros y posteriormente removerlos. Lo anterior no corresponde a lo que uno esperaria en un codigo "optimizado", sin embargos me vi envuelto en una dificultad al momento de trabajar con lil_matrix.
* ¿Cual parece la complejidad asintótica (N → ∞)  para el ensamblado y solución en ambos casos y porqué?
   *
