import matplotlib.pyplot as plt

# Define as coordenadas do ponto A
x = 5
y = 5

# Define as propriedades do ponto A
point_size = 8
point_char = 'o'
point_color = 'red'

# Cria uma figura
fig, ax = plt.subplots()

# Plota o ponto A
ax.plot(x, y, marker=point_char, markersize=point_size, color=point_color)

# Define o tamanho dos eixos
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])

# Exibe o gráfico
plt.show()
