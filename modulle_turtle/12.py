import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("KKC")

def draw_petal(t, radius, angle):
    t.circle(radius, angle)
    t.left(180)
    t.circle(radius, angle)
    t.left(180)

def draw_flower(t, x, y, petals, radius, angle, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()

    for _ in range(petals):
        draw_petal(t, radius, angle)
        t.left(360 / petals)
    t.end_fill()

def draw_text(t, text, x, y, font_size, color):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.write(text, align="center", font=("Arial", font_size, "bold"))

pen = turtle.Turtle()
pen.speed(5)

# Цветы
draw_flower(pen, -100, 100, petals=6, radius=50, angle=60, color="red")
draw_flower(pen, 100, 100, petals=8, radius=50, angle=45, color="pink")
draw_flower(pen, 0, -50, petals=10, radius=30, angle=36, color="purple")

# Текст
draw_text(pen, 'KKC', 0, -150, font_size=24, color="green")

pen.hideturtle()
screen.mainloop()
