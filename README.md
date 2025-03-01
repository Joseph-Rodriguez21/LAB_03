# Laboratorio 3 Coctel 

1. Introducción:
   
   El problema de la "fiesta de cóctel" se refiere a la dificultad de aislar una voz específica en un entorno con múltiples fuentes sonoras. En este laboratorio, se recreará este fenómeno utilizando un arreglo de micrófonos para capturar señales mezcladas de varias fuentes sonoras. El objetivo es desarrollar técnicas que permitan separar y extraer la voz de interés, un desafío clave en aplicaciones como el reconocimiento de habla, la mejora de la voz y la cancelación de ruido.

2.  Desarrollo del sistema:

   El sistema fue pensando de manera estrategica para que cada celular (microfono) garantizara una captura óptima de las señales y una correcta aplicación del algoritmo ICA. Usamos un arreglo con tres microfonos a distancias similares simulando una fiesta de coctel con mesas ubicadas a distancias iguales y así poder analizar la captura de la señal de las diferentes voces.
De la siguiente manera:

![Imagen de WhatsApp 2025-02-28 a las 21 30 50_9cd233d9](https://github.com/user-attachments/assets/6dc46c08-6d0b-4faa-a6fc-1e4bcf8966a3)
Fig 1. Desarrollo sistema simulacion fiesta de coctel para captura y procesamiento de voces. 

Allí podemos observar las diferentes distancias de los microfonos y las personas, asi exigiendo al sistema y a cada microfono capturar señales más fuertes de dos personas para poder compararlas y analizarlas, el m1 con p1 (joseph), m2 con p2 (yader) y m3 con p3 (felipe), uno al frente del otro respectivamente como se muestra en el diagrama del sistema.

3. Metodología y desarrollo:

   Se conectaron tres micrófonos a un sistema de adquisición de datos y se ubicaron de acuerdo con la distribución mencionada.

Se grabaron las señales de audio mientras las personas conversaban simultáneamente.

Se preprocesaron las señales, eliminando posibles ruidos no deseados y normalizando su amplitud.

 - Primero se graban los audios previamente establecidos por el sistema y se convierten en archivo '.wav' para que sean leidos por la libreria 'librosa' en spyder, luego importamos las siguientes bibliotecas para poder procesarlas y nombramos cada archivo en los distintos audios 'audio1 (joseph), audio2 (yader), audio 3 (felipe), audio4 (ruido_blanco)', 'sr' corresponde a los 44.1 khz.
![image](https://github.com/user-attachments/assets/6189cedd-a51e-433b-8c56-9182f403b985)

- Los audios grabados fueron de aproximadamente 15 a 30 segundos, en donde extraemos los primeros 10 segundos que son los más claros y precisos para analizar y trabajar en este laboratorio, con esto analizamos esta parte de la señal de cada microfono, y luego hallamos el SNR de los tres audios de la siguiente manera.
- Se halla la potencia promedio de cada señal (promedio de los valores al cuadrado).
![image](https://github.com/user-attachments/assets/801801cf-8db7-46d3-be9d-c1ad85cb7fa4)




