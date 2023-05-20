import numpy as np

# Definindo as coordenadas dos vértices do triângulo
A = np.array([0, 0, 0, 1])
B = np.array([2, 0, 0, 1])
C = np.array([1, 3, 0, 1])

# Criando a matriz homogênea dos pontos do triângulo
triangle = np.array([A, B, C])

# Definindo a matriz de escala
S = np.array([[3, 0, 0, 0], [0, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])

# Multiplicando a matriz de escala pela matriz homogênea do triângulo
scaled_triangle = np.dot(S, triangle.T).T

# Imprimindo as coordenadas dos vértices do triângulo escalado
print(scaled_triangle)
