# The Karel robot picks a beeper by running horizontally and vertically
# stanfordkarel # pip install stanfordkarel
# karel # pip install karel
# pyparsing # pip install pyparsing

# Turns Karel 90 degrees to the right.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_left():
    pass

def move():
    pass



def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for step in range(6):
    jump()


