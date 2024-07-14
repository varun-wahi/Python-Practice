import turtle
turtle.setup(width=600, height=500)
turtle.reset()
turtle.bgcolor("black")
w=turtle.Turtle()
#w.hideturtle()

def square(x,color):
  w.left(99)
  w.forward(x)
  w.right(90)
  w.forward(x)
  w.right(90)
  w.forward(x)
  w.right(90)
  w.forward(x)
  w.pencolor(color)

#setup
w.pensize(0.8)
w.speed("fastest")
list=["red","blue","green","light blue","yellow","black"]
w.penup()
w.pendown()

#main
for i in range(1):
  for x in range(0,200,2):
    for color in list:
      square(x,color)

#end statements
w.done()
