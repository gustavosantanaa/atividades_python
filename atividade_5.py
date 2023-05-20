import numpy as np
import matplotlib.pyplot as plt

# Definindo as coordenadas dos pontos A, B e C
xA, yA = 1, 2
xB, yB = 5, 6
xC, yC = 7, 3

# Criando as matrizes homogêneas para os pontos A, B e C
M_A = np.array([[xA], [yA], [1], [1]])
M_B = np.array([[xB], [yB], [1], [1]])
M_C = np.array([[xC], [yC], [1], [1]])

# Concatenando as matrizes M_A, M_B e M_C em uma única matriz M_total
M_total = np.concatenate((M_A, M_B, M_C), axis=1)

# Definindo a matriz de translação T
T = np.array([[1, 0, 0, 3], [0, 1, 0, 5], [0, 0, 1, 0], [0, 0, 0, 1]])

# Aplicando a transformação de translação multiplicando a matriz T pela matriz M_total
M_translated = np.dot(T, M_total)

# Extraindo as coordenadas dos pontos A', B' e C' da matriz resultante
xA_translated, yA_translated, _, _ = M_translated[:, 0]
xB_translated, yB_translated, _, _ = M_translated[:, 1]
xC_translated, yC_translated, _, _ = M_translated[:, 2]

# Desenhando os pontos A, B e C
plt.scatter(xA, yA, color='red')
plt.scatter(xB, yB, color='green')
plt.scatter(xC, yC, color='blue')

# Desenhando os pontos A', B' e C' (resultantes da translação)
plt.scatter(xA_translated, yA_translated, color='magenta')
plt.scatter(xB_translated, yB_translated, color='lime')
plt.scatter(xC_translated, yC_translated, color='cyan')

# Desenhando as retas AB, BC e CA
plt.plot([xA, xB], [yA, yB], color='black', linewidth=2)
plt.plot([xB, xC], [yB, yC], color='purple', linewidth=3)
plt.plot([xC, xA], [yC, yA], color='orange', linewidth=4)

# Definindo os limites do gráfico
plt.xlim(0, 15)
plt.ylim(0, 15)

# Mostrando o gráfico resultante da translação
plt.show()
