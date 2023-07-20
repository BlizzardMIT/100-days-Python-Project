# The Karel robot picks a beeper by running horizontally and vertically
# https://compedu.stanford.edu/karel-reader/docs/python/en/chapter4.html

from karel.stanfordkarel import *

def main():
    move()
    fill_pothole()
    move()

def fill_pothole():
    turn_right()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()

# Turns Karel 90 degrees to the right.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Turns Karel around 180  degrees.
def turn_around():
    turn_left()
    turn_left()


