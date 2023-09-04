import another_module

from turtle import Turtle, Screen

# Whenever we want to print a variable from  another module we can call it by .(dot) sign.
print(another_module.another_variable)

# Turtle here is a class.
timmy = Turtle()
# timmy is an object.

timmy.shape("turtle")
timmy.color("red")

print(timmy)

timmy.color('red')
timmy.fillcolor('yellow')
timmy.begin_fill()

while True:
    timmy.forward(200)
    timmy.left(170)
    if abs(timmy.pos()) < 1:
        break
# Given below is an example of an object, It's attribute here car is an object whereas speed is it's attribute
# This is how often the structure is given of a OOP.
# car.speed

my_screen = Screen()

print(my_screen.canvheight)

# below is an example of an object (car) with a function(move())
# car.move()

my_screen.exitonclick()
