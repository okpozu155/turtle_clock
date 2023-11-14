import turtle
import math
import time


# Function to create clock hands
def create_hand(length, angle):
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    turtle.setheading(angle)
    turtle.forward(length)
    turtle.backward(length)

# Function to create the clock face
def create_clock_face(radius,thickness):
    turtle.up()
    turtle.goto(0, -radius)
    turtle.down()
    turtle.circle(radius)
    turtle.width(thickness)
    turtle.circle(radius)
    for i in range(0,13,3):
        turtle.up()
        turtle.goto(0, 0)
        turtle.setheading(90 - 30 * i)
        turtle.forward(radius - 20)
        turtle.write(str(i), align="center", font=("Arial", 12, "normal"))

# Set up the window
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Wall Clock")
wn.setup(width=600, height=600)
wn.tracer(0)

# Create the clock face
create_clock_face(150, 3)

# Draw the clock hands
while True:
    current_time = time.localtime()
    second = current_time.tm_sec
    minute = current_time.tm_min
    hour = current_time.tm_hour % 12  # Considering a 12-hour clock

    # Clear previous hands before drawing the new ones
    turtle.clear()

    # Draw hour hand
    create_hand(50, -hour * 30 - minute * 0.5)

    # Draw minute hand
    create_hand(80, -minute * 6)

    # Draw second hand
    create_hand(100, -second * 6)

    # Update the screen
    wn.update()
    time.sleep(1)

# Uncomment the following line if you're using the `turtle.done()` function to keep the window open
turtle.done()
