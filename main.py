import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#27258f") #color hex code
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance2 = turtle.Turtle()
turtle_instance2.left(90)
turtle_instance2.forward(100)

turtle_instance.fillcolor("red")
turtle.done()
