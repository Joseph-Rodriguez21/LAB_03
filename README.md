# Laboratorio 3 Coctel 

1. Introducción:
   
   El problema de la "fiesta de cóctel" se refiere a la dificultad de aislar una voz específica en un entorno con múltiples fuentes sonoras. En este laboratorio, se recreará este fenómeno utilizando un arreglo de micrófonos para capturar señales mezcladas de varias fuentes sonoras. El objetivo es desarrollar técnicas que permitan separar y extraer la voz de interés, un desafío clave en aplicaciones como el reconocimiento de habla, la mejora de la voz y la cancelación de ruido.

2.  Desarrollo del sistema:

   El sistema fue pensando de manera estrategica para que cada celular (microfono) garantizara una captura óptima de las señales y una correcta aplicación del algoritmo ICA. Usamos un arreglo con tres microfonos a distancias similares simulando una fiesta de coctel con mesas ubicadas a distancias iguales y así poder analizar la captura de la señal de las diferentes voces.
De la siguiente manera:

![Imagen de WhatsApp 2025-02-28 a las 21 30 50_9cd233d9](https://github.com/user-attachments/assets/6dc46c08-6d0b-4faa-a6fc-1e4bcf8966a3)
Fig 1. Desarrollo sistema simulacion fiesta de coctel para captura y procesamiento de voces. 

Allí podemos observar las diferentes distancias de los microfonos y las personas, asi exigiendo al sistema y a cada microfono capturar señales más fuertes de dos personas para poder compararlas y analizarlas, el m1 con p1 (joseph), m2 con p2 (yader) y m3 con p3 (felipe), uno al frente del otro respectivamente como se muestra en el diagrama del sistema.

3. Metodología, desarrollo y analisis:

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

![image](https://github.com/user-attachments/assets/1913a556-dffb-4bca-98b5-cdce5d15a868)

El SNR (Signal-to-Noise Ratio o Relación Señal-Ruido) es crucial en esta práctica porque determina la calidad de las señales capturadas y la efectividad del proceso de separación de fuentes.

- Procesamiento de señales:
Para analizar las señales capturadas por los micrófonos, se realiza un análisis temporal y espectral. El análisis temporal permite observar la evolución de la señal en función del tiempo, mientras que el análisis espectral transforma la señal al dominio de la frecuencia para identificar sus componentes principales.

- La Transformada Rápida de Fourier (FFT) se usa para convertir las señales de audio del dominio del tiempo al dominio de la frecuencia, lo que permite analizar las frecuencias predominantes en cada señal.

Se calcula la frecuencia con 'np.fft.fftfreq(len(audio1), 1/sr)', lo que genera un vector de frecuencias basado en la cantidad de muestras y la frecuencia de muestreo (sr).
Se aplica la FFT a cada señal con 'np.fft.fft(audioX)', obteniendo su representación espectral.
Se grafican las magnitudes de la FFT en función de la frecuencia, usando solo la mitad del espectro, ya que la FFT es simétrica respecto al eje de Nyquis

![image](https://github.com/user-attachments/assets/28edcfe2-a858-4665-a6bf-88cad9ea4481)

Esto permite identificar las frecuencias dominantes en cada señal, ayudando a diferenciar fuentes sonoras y entender mejor la propagación del sonido en el entorno de medición, esto nos permite identificar las frecuencias características de la voz y determinar si hay ruido o interferencias no deseadas.

- Espectro de la transfromada de Fourier en escala lineal, para observar los picos de frecuencia dominantes.
- 
v![image](https://github.com/user-attachments/assets/12b2daed-94ac-4ab9-a887-ae2b387d70ab)

Se grafica el espectro de frecuencia de las señales de audio capturadas, utilizando una escala semilogarítmica en el eje y para mejorar la visualización de los valores pequeños en la amplitud de la FFT.

![image](https://github.com/user-attachments/assets/eaee0e73-9472-47fa-8372-20341c113db5)

- Espectro de la transformada de Fourier en escala logaritmica en escala logarítmica, para detectar componentes débiles de la señal.
- 
![image](https://github.com/user-attachments/assets/aad3c2d7-9d83-4ce1-ac63-5e3b562f275f)

Permite analizar el contenido espectral de las señales de audio, con una mejor visualización de frecuencias de menor amplitud gracias a la escala logarítmica en el eje y. Esto facilita la identificación de componentes de baja energía que podrían pasar desapercibidos en una escala lineal.

- Análisis de Componentes Independientes (ICA)

 Se encuentra la cantidad mínima de muestras entre las señales captadas (audio1_inicio, audio2_inicio, audio3_inicio) para asegurarse de que todas tengan la misma longitud y evitar errores al operar con matrices. Aparte se construye una matriz F con las señales de los tres micrófonos. La transposición (.T) es necesaria porque cada fila debe representar una muestra en el tiempo, y cada columna debe representar una señal captada.
 
![image](https://github.com/user-attachments/assets/c2bec2ca-2e48-4fef-8d82-7a1a162de7e1)

Se instancia el modelo FastICA para encontrar 3 componentes independientes (una por cada señal captada).
'fit_transform(F)': ajusta el modelo a los datos y devuelve las señales separadas en 'señales_separadas'.
Ahora, 'señales_separadas' contiene tres señales independientes, cada una en una columna de la matriz.
Se calcula la energía de cada señal separada, esta se obtiene como el promedio del cuadrado de la señal '(np.mean(señal**2))'. Por otro lado 'np.argmax(energias)': encuentra el índice de la señal con mayor energía, que se asume que corresponde a la voz principal.

![image](https://github.com/user-attachments/assets/1ea115f9-5873-45f8-b070-76a2949dad71)

Se extrae la señal con mayor energía, asumiendo que es la voz más fuerte, luego se calcula la potencia dpromedio de la vos extraida, tambien se calcula la potencia del ruido tomando como referencia el cuarto audio y por último hallamos el SNR.

![image](https://github.com/user-attachments/assets/6f16fa36-b6a0-49cf-a6c3-17b245241651)

![image](https://github.com/user-attachments/assets/54a20696-0251-4003-8117-8fd7e9bd64e4)

- Se normaliza la señal extraída (Se divide la señal voz_extraida entre su valor absoluto máximo; esto asegura que su amplitud esté en el rango de -1 a 1, evitando distorsión o saturación al guardarla como archivo de audio.), la guarda como un archivo de audio (voz_extraida.wav) y la grafica para visualizar su forma de onda en función del tiempo. Esto permite verificar que la separación de la señal fue exitosa y que la voz es claramente distinguible.
  
![image](https://github.com/user-attachments/assets/d5fe86c3-42a5-43ed-9b57-21309c31be9b)

Gráfica de la señal previamente extraida:

![image](https://github.com/user-attachments/assets/21c3a02c-674a-47ad-b30f-3d3ba70ddbf5)

- El objetivo del experimento fue extraer la voz de una persona en un entorno ruidoso utilizando el método de Análisis de Componentes Independientes (ICA). Se usaron varios micrófonos de celulares para capturar señales de voz mezcladas, y con ICA se logró separar las fuentes de sonido, identificando la voz predominante.

Después de extraer la voz, se realizó un análisis espectral aplicando la Transformada Rápida de Fourier (FFT) para observar su composición en frecuencia. Se graficó el espectro de la señal extraída tanto en escala lineal como logarítmica para resaltar diferentes características de las frecuencias presentes.

- Ahora, teniendo en cuenta estose visualiza la composición espectral de la voz extraída, destacando sus componentes de frecuencia y asegurando que la separación de la señal fue efectiva. Además, la comparación de las gráficas en escala lineal y logarítmica ayuda a analizar mejor las características de la señal en distintos rangos de frecuencia.

![image](https://github.com/user-attachments/assets/2af11388-4dcb-4b84-a09a-b1bcc5b58473)

Siendo así, obtenemos las siguientes gráficas correspondientes:
- Forma lineal:

![image](https://github.com/user-attachments/assets/14b10c2e-f4b0-4b94-8c09-f82c85e6892c)

- Escala logaritmica:

![image](https://github.com/user-attachments/assets/cb182894-e763-4f77-8295-8a5074033b56)

 Ya por último se extrae el archivo de voz con la fuente de audio que fue identificada como la voz predominante y se calcula el SNR.

4. Conclusiones:

- Se logró aplicar con éxito el Análisis de Componentes Independientes (ICA) para separar las señales capturadas por los micrófonos y se demostró que este método es bueno para extraer la voz más predominante en un entorno de múltiples fuentes sonoras y ruido externo.
- Se comprobó que la Relación Señal-Ruido (SNR) maneja directamente en la calidad de la separación de señales puesto que las voces con mayor SNR fueron más fáciles de aislar, mientras que las voces con menor SNR presentaron mayor contaminación con ruido, dificultando el proceso de separación. En este caso, los valores obtenidos fueron:
  


