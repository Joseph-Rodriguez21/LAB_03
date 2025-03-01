import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA
import soundfile as sf


audio1,sr=librosa.load("joseph.wav",sr=None)
audio2,sr=librosa.load("yader.wav",sr=None)
audio3,sr=librosa.load("pipe.wav",sr=None)
audio4,sr=librosa.load("ruido_blanco.wav",sr=None)

muestras_10seg = 10 * sr  

audio1_inicio = audio1[:muestras_10seg]  
audio2_inicio = audio2[:muestras_10seg]
audio3_inicio = audio3[:muestras_10seg]
audio4_inicio = audio4[:muestras_10seg]

potencia_señal1=np.mean(audio1**2)
potencia_señal2=np.mean(audio2**2)
potencia_señal3=np.mean(audio3**2)
potencia_señal4=np.mean(audio4**2)

SNR1=10*np.log10(potencia_señal1/potencia_señal4)
SNR2=10*np.log10(potencia_señal2/potencia_señal4)
SNR3=10*np.log10(potencia_señal3/potencia_señal4)

print ("el SNR del audio 1 es: ",SNR1,"dB")
print ("el SNR del audio 2 es: ",SNR2,"dB")
print ("el SNR del audio 3 es: ",SNR3,"db")

#definimos a las personas como p1, p2 y p3, siendo correspondientemente:
    #joseph = p1 
    #pipe = p2 
    #yader = p3

distanciap1_m1 = 1.92
distanciap2_m2 = 1.92
distanciap3_m3 = 1.92 

distanciap1_m2 = 1.6
distanciap1_m3 = 1.6
distanciap2_m1 = 1.6
distanciap2_m3 = 1.92
distanciap3_m1 = 1.6
distanciap3_m2 = 1.92

distanciam1_m2 = 2.49
distanciam1_m3 = 2.49
distanciam2_m3 = 3.2

vel_sonido = 343  


retardop1_m1 = int((distanciap1_m1 / vel_sonido) * sr)
retardop2_m2 = int((distanciap2_m2 / vel_sonido) * sr)
retardop3_m3 = int((distanciap3_m3 / vel_sonido) * sr)

retardop1_m2 = int((distanciap1_m2 / vel_sonido) * sr)
retardop1_m3 = int((distanciap1_m3 / vel_sonido) * sr)
retardop2_m1 = int((distanciap2_m1 / vel_sonido) * sr)
retardop2_m3 = int((distanciap2_m3 / vel_sonido) * sr)
retardop3_m1 = int((distanciap3_m1 / vel_sonido) * sr)
retardop3_m2 = int((distanciap3_m2 / vel_sonido) * sr)

audio1 = np.pad(audio1, (retardop1_m1, 0))[:len(audio1)]
audio2 = np.pad(audio2, (retardop2_m2, 0))[:len(audio2)]
audio3 = np.pad(audio3, (retardop3_m3, 0))[:len(audio3)]

audio1 *= 1 / (distanciap1_m1 ** 2 + distanciap1_m2 ** 2 + distanciap1_m3 ** 2)
audio2 *= 1 / (distanciap2_m2 ** 2 + distanciap2_m1 ** 2 + distanciap2_m3 ** 2)
audio3 *= 1 / (distanciap3_m3 ** 2 + distanciap3_m1 ** 2 + distanciap3_m2 ** 2)

total_muestras = min(len(audio1), len(audio2), len(audio3))


plt.figure(figsize=(10, 4))
librosa.display.waveshow(audio1, sr=sr, alpha=0.5, color="blue", label="Audio 1")
librosa.display.waveshow(audio2, sr=sr, color="brown", alpha=0.5, label="Audio 2")
librosa.display.waveshow(audio3, sr=sr, color="yellow", alpha=0.5, label="Audio 3")

plt.legend()
plt.title("Señales capturadas por los micrófonos")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()



frecuencia=np.fft.fftfreq(len(audio1), 1/sr)
trans_audio1=np.fft.fft(audio1)
trans_audio2=np.fft.fft(audio2)
trans_audio3=np.fft.fft(audio3)

plt.figure(figsize=(10, 4))
plt.plot(frecuencia[:len(frecuencia)//2], np.abs(trans_audio1[:len(frecuencia)//2]), color='#98FB98', label="Audio 1")
plt.plot(frecuencia[:len(frecuencia)//2], np.abs(trans_audio2[:len(frecuencia)//2]), color='#D3D3D3', label="Audio 2")
plt.plot(frecuencia[:len(frecuencia)//2], np.abs(trans_audio3[:len(frecuencia)//2]), color='#FFDAB9', label="Audio 3")

plt.legend()
plt.title("Espectro de Frecuencia (FFT)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.show()

plt.figure(figsize=(10, 4))
plt.semilogy(frecuencia[:len(frecuencia)//2], np.abs(trans_audio1[:len(frecuencia)//2]), color='#98FB98', label="Audio 1")
plt.semilogy(frecuencia[:len(frecuencia)//2], np.abs(trans_audio2[:len(frecuencia)//2]), color='#D3D3D3', label="Audio 2")
plt.semilogy(frecuencia[:len(frecuencia)//2], np.abs(trans_audio3[:len(frecuencia)//2]), color='#FFDAB9', label="Audio 2")
plt.legend()
plt.title("Espectro de Frecuencia (FFT)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.show()

total_muestras = min(len(audio1_inicio), len(audio2_inicio), len(audio3_inicio))
F = np.array([audio1[:total_muestras], audio2[:total_muestras], audio3[:total_muestras]]).T

ica = FastICA(n_components=3, random_state=42)
señales_separadas = ica.fit_transform(F)

energias = [np.mean(señal**2) for señal in señales_separadas.T]
indice_voz = np.argmax(energias)  

voz_extraida = señales_separadas[:, indice_voz]

potencia_voz = np.mean(voz_extraida**2)
potencia_ruido = np.mean(audio3[:total_muestras]**2)

snr_voz = 10 * np.log10(potencia_voz / potencia_ruido)

voz_extraida /= np.max(np.abs(voz_extraida))

sf.write("voz_extraida.wav", voz_extraida, sr)

plt.figure(figsize=(10, 4))
librosa.display.waveshow(voz_extraida, sr=sr, color='#D8BFD8')
plt.title("Señal de Voz Extraída (La Más Fuerte)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()


frecuencia = np.fft.fftfreq(len(voz_extraida), 1/sr)
transformada = np.fft.fft(voz_extraida)

plt.figure(figsize=(10, 4))
plt.plot(frecuencia[:len(frecuencia)//2], np.abs(transformada[:len(frecuencia)//2]), color='#AEC6CF')
plt.title("Espectro de Frecuencia de la Voz Extraída")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.show()

plt.figure(figsize=(10, 4))
plt.semilogy (frecuencia[:len(frecuencia)//2], np.abs(transformada[:len(frecuencia)//2]), color='#C1E1C1')
plt.title("Espectro de Frecuencia de la Voz Extraída")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.show()

print(f"La voz extraída corresponde a la fuente {indice_voz + 1}.")
print(f"SNR de la voz extraída: {snr_voz:.2f} dB")
print("La señal ha sido guardada como 'voz_extraida.wav'.")