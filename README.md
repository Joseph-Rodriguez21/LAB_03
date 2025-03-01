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

Realizando el proceso mencionado anteriormente obtenemos los valores de SNR de cada audio, siendo estos:

SNR del audio 1 es:  11.717942953109741 dB
SNR del audio 2 es:  16.274336576461792 dB
SNR del audio 3 es:  16.810566186904907 db

- Como se menciono en el apartado [2] se establecen las distancias entre las personas y los celulares para calcular el retardo de cada señal de audio, usando la fórmula:

![image](https://github.com/user-attachments/assets/32e99964-6c0a-4c29-b81b-8cad581b3431)
Fig 2. Fórmula tiempo de retardo.

![image](https://github.com/user-attachments/assets/94a68259-0192-49c1-b050-7361ef397055)

- Este tiempo se convierte en número de muestras multiplicándolo por la frecuencia de muestreo (sr) y se usa np.pad() para agregar ceros al inicio de la señal, simulando la propagación del sonido antes de ser captado.

![image](https://github.com/user-attachments/assets/666207fb-008e-4a7f-86b7-67fa7486250f)

- Además, se calcula un factor de atenuación según la distancia y se ajusta la longitud de las señales para que coincidan antes de graficarlas.

![image](https://github.com/user-attachments/assets/5205e910-631d-4dc9-8c08-5c22816c0472)

- Finalmente, se grafican las señales con matplotlib y librosa.display, asignando colores, etiquetas y leyenda para una mejor identificación.

![image](https://github.com/user-attachments/assets/a0b36fdf-c1d8-4d0f-ae66-e325e3d79a13)

-

![image](https://github.com/user-attachments/assets/4ff8ef21-179f-4f52-86b9-51aadc6356b6)

-

![image](https://github.com/user-attachments/assets/0b1033ad-e0e3-4e8d-be97-259023a2526e)

-

![image](https://github.com/user-attachments/assets/32dbaf53-7b72-4613-8fc6-dee383e304df)

-

![image](https://github.com/user-attachments/assets/3168048d-f276-4373-ae72-8fe6bc0092e4)

-

![image](https://github.com/user-attachments/assets/ac8b5405-c321-429c-8a8d-9d682f1a1bfb)




![image](https://github.com/user-attachments/assets/1913a556-dffb-4bca-98b5-cdce5d15a868)
El SNR (Signal-to-Noise Ratio o Relación Señal-Ruido) es crucial en esta práctica porque determina la calidad de las señales capturadas y la efectividad del proceso de separación de fuentes.

- Procesamiento de señales:
  
