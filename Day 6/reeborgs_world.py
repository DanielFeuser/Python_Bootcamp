#Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def right_wall():
    if not wall_on_right():
        turn_right()
    move()

while not at_goal():
    if not wall_on_right():
        right_wall()
    elif wall_in_front():
        turn_left()
    else:
        move()