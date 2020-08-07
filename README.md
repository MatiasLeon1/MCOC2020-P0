## MCOC2020-P0

## Mi computador

* Marca/Modelo: Hp Pavilion 

* Tipo: Notebook

* Año Adquisición: 2020

* Procesador:
  * Marca/Modelo: AMD A8-7410 APU with AMD radeon R5 Graphics 2.20 GHz
  * Velocidad Base: 2,20 GHz
  * Velocidad Máxima: 2,40 GHz
  * Nucleos: 4
  * Procesadores logicos: 4
  * Arquitectura: AMD64
  * Set de instrucciones: Intel SSE4.1, Intel SSE4,2, INtel AVX2
  
  * Tamaño de las caches del procesador
  * L1: 256 kB
  * L2: 2,0 MB
  
 * Memoria
  * Total: 8 Gb   
  * Tipo de memoria: DDR3
  * Velocidad: 1855 MHz
  * Numero de (SO)DIMM: 1 de 2 usadas
  
 * Tarjeta Gráfica
  * Marca/Modelo: AMD radeon R5 Graphics
  * Memoria dedicada: 4568 MB
  * Resolución: 1366 x 768 x 60 hericos
  
 * Disco
  * Marca:(Unidades de disco estandar) Microsoft
  * Tipo: Disco duro  
  * Tamaño: 1TB
  * Particiones: 4
  * Sistema de archivos: NTFS
 
 * Dirección MAC de la tarjeta wifi: C8-FF-28-F6-E7-2B
 * Direccion IP (Interna del router): 192.168.1.136
 * Direccion IP (Externa, del ISP): 190.215.242.187
 * Proveedor internet: GTD Manquehue, fibra optica
 
  ## DESEMPEÑO MATMUL
 
 ![image](https://user-images.githubusercontent.com/43649125/89683457-926d9200-d8c6-11ea-8797-fda0481dc760.png)


 * Preguntas:
  * ¿Como difiere del grafico del profesor/ayudante?
    - La principal diferencia que se aprecia es el tiempo que demora mi computador en realizar los calculos de matrices,
      mientras mas grande la matriz, mas se demora mi computador en calcularla.
  * ¿A que pueden deberse las diferencias?
    - La principal diferencia es el procesador de mi computador, versus el del profesor/ayudante. Siendo el mio claramente
      menos poderoso. Lo segundo probablemente sea la memoria RAM, yo poseo 8G RAM y el pc del profesor 32G RAM
  * El grafico de uso de memoria es lineal con el tamaño de la matriz, pero el tiempo transcurrido no lo es ¿Por que puede ser?
    - Ningun delta tiempo es igual al anterior. Lo comprobé al inicio cuando el profesor adjunto el codigo, se comprueba de igual
      manera al ver que ninguno de los ciclos realizados (10) es identico entre sí. Asumo que el procesador del computador esta
      constantemente realizando acciones en segundo plano, ya sean pequeñas como autoguardar un archivo, o grandes como por
      ejemplo descargar Anaconda. Debido a esta diferencia que puede ser infima o notoria, los tiempos de calculo no van a ser
      iguales entre si. Para los primeros calculos esta diferencia es muy pequeña, sin embargo para las matrices mas grandes
      la diferencia puede ser (y en mi computador lo es) de una cuestion de segundos.
  * ¿Que versión de Python esta usando?
    - 3.8.3
  * ¿Que version Numpy esta usando?
    - 1.18.5
  * ¿Durante la ejecución de su codigo, se utiliza mas de un procesador? Muestre una imagen de su uso de procesador
    durante alguna corrida para confirmar
    - Se utilizan 4 procesadores. Lo revise con el comando import multiprocessing, print(multiprocessing.cpu_count())
     Retorno: 4
     Imagen de uso de procesador durante corrida de iteracion 1:
     ![image](https://user-images.githubusercontent.com/43649125/89685924-4d982a00-d8cb-11ea-9416-173a766f889c.png)

    
 
 
 
 
 
 
 
 
 
 
