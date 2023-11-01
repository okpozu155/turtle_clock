import turtle
import time

# Function to create clock hands
def create_hand(length, angle):
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    turtle.setheading(angle)
    turtle.forward(length)
    turtle.backward(length)


while True:
    curent_time = time.time()