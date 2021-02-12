import turtle as t
import random
t.colormode(255)
t=t.Turtle()
t.pensize(15)
t.speed("fastest")

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_colour=(r,g,b)
    return random_colour

directions=[0, 90, 180, 270, 360]
for _ in range(300):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))

