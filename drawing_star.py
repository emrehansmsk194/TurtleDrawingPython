import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("Star Drawing Example")

turtle_instance = turtle.Turtle()
num_of_sides = 5
angle = 360.0 / num_of_sides * 2
len_of_sides = 300
for i in range(num_of_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(len_of_sides)

turtle.done()