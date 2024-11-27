This project creates a real-time Wall Clock using Python's turtle graphics module. The clock features a circular face, hour markers, and moving hour, minute, and second hands that update every second to reflect the current time.
Features

    Real-Time Clock: Updates every second to show the current time.
    Clock Face: Displays hour markers (12-hour format).
    Clock Hands: Separate hands for hours, minutes, and seconds, each moving accurately.
    Customizable Design: Easily adjust clock radius, hand lengths, and other visual parameters.

How It Works

    Clock Face: A circle is drawn with hour markers labeled every 3 hours.
    Clock Hands: Three hands (hour, minute, second) are dynamically drawn based on the current time.
    Real-Time Update: The hands are cleared and redrawn every second using time.localtime() to fetch the system time.

Prerequisites

    Python 3.7 or higher
    turtle module (comes pre-installed with Python)

Installation

    Clone the repository:

    git clone https://github.com//wall-clock-turtle.git

    cd wall-clock-turtle

    Run the Python script:

    python wall_clock.py

Code Overview
Functions

    create_hand(length, angle): Draws a clock hand of a specified length at a given angle.
    create_clock_face(radius, thickness): Draws the circular clock face and hour markers.

Main Loop

    Fetches the current time using time.localtime().
    Clears previously drawn hands.
    Recalculates hand positions based on the current time.
    Redraws the hands and updates the screen.

Customization

You can customize the clock by modifying the following parameters:

    Clock Radius: Adjust the radius parameter in create_clock_face.
    Hand Lengths: Change the values passed to create_hand for hour, minute, and second hands.
    Font Style: Update the font in the turtle.write function to change the appearance of hour markers.
    Clock Dimensions: Use wn.setup(width, height) to resize the clock display.

Example Output

The program creates a graphical clock that updates as shown below:

    Clock Face: A circle with markers for hours.
    Clock Hands: Three hands continuously updating for seconds, minutes, and hours.

Potential Enhancements

    Add a digital clock display alongside the analog clock.
    Include features like alarms or stopwatch functionality.
    Improve visual design with colors and themes.
