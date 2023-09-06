import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light green")
drawing_board.title("Turtle Python")


turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

for i in range(6):
    shrinkingSquare(120 - 20 * i)







turtle.done()