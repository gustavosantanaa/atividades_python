import matplotlib.pyplot as plt

# Define as coordenadas do ponto A
xA, yA = 3,2
xB, yB = 6,8


# Define as propriedades do ponto A e B
point_size = 8
point_charA, point_charB = 'o' , '+'
point_colorA, point_colorB = 'green' , 'blue'


# Cria uma figura
fig, ax = plt.subplots()

# Plota o ponto A e B
ax.plot(xA, yA, marker=point_charA,  color=point_colorA)
ax.plot(xB, yB, marker=point_charB,  color=point_colorB)


# Define o tamanho dos eixos
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])


# Exibe o gráfico
plt.show()
