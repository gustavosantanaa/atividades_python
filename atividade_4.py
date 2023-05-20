import matplotlib.pyplot as plt

# Definindo as coordenadas dos pontos A, B e C
xA, yA = 1, 2
xB, yB = 5, 6
xC, yC = 7, 3

# Desenhando os pontos A, B e C
plt.scatter(xA, yA, color='red')
plt.scatter(xB, yB, color='green')
plt.scatter(xC, yC, color='blue')

# Desenhando as retas AB, BC e CA
plt.plot([xA, xB], [yA, yB], color='black', linewidth=2)
plt.plot([xB, xC], [yB, yC], color='purple', linewidth=3)
plt.plot([xC, xA], [yC, yA], color='gray', linewidth=4)

# Mostrando o gráfico resultante
plt.show()
