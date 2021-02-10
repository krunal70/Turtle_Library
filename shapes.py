from turtle import *
import random
t=Turtle()
colours=["#4169E1","#00CED1","#ADFF2F","#8B4513","#7B68EE","#FFD700","#800000"]
def shapes(num_of_sides):
    angle=360/num_of_sides
    for _ in range(num_of_sides):
        t.forward(100)
        t.right(angle)

for sides in range(3,11):
    t.color(random.choice(colours))
    shapes(sides)