import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# Definição dos parâmetros
n = 1000  # Número de observações
cutoff = 0.1  # Frequência de corte (ajuste conforme necessário)
order = 5  # Ordem do filtro

# Gerar sinal de exemplo (sinal senoidal)
t = np.linspace(0, 1, n, endpoint=False)
x = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# Aplicar filtro passa baixa
fs = 1.0 / (t[1] - t[0])
b, a = butter(order, cutoff, fs=fs, btype='low', analog=False)
y = lfilter(b, a, x)

# Plotar o sinal original e o sinal filtrado
plt.figure()
plt.plot(t, x, label='Sinal Original')
plt.plot(t, y, label='Sinal Filtrado')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
