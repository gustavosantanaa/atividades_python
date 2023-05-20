import turtle

# Definir os pontos A e B
xA, yA = -100, 0
xB, yB = 100, 0

# Definir a janela de exibição
turtle.setup(width=600, height=400)

# Criar a tartaruga e definir sua posição inicial em A
t = turtle.Turtle()
t.penup()
t.goto(xA, yA)
t.pendown()

# Definir a equação paramétrica da reta
def parametric_line(t, xA, yA, xB, yB):
    dx = xB - xA
    dy = yB - yA
    m = dy / dx
    b = yA - m * xA
    return lambda t: (xA + t * dx, m * (xA + t * dx) + b)

line = parametric_line(t, xA, yA, xB, yB)

# Desenhar o segmento de reta AB
t.speed('fast')
t.pensize(2)
for t_value in [0.1 * i for i in range(11)]:
    x, y = line(t_value)
    t.goto(x, y)

turtle.done()
