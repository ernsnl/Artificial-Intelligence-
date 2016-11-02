# For displaying block movement

import turtle # For Displaying movement
import time
def draw_sliding_block(sliding_block):
    # Creating the background for the sliding block problem
    turtle.reset()
    turtle.title("Sliding Block Solution Simulator")
    turtle.setworldcoordinates(0,300,300,0)
    turtle.penup()
    turtle.goto(0,0)
    turtle.speed(0)


    turtle.hideturtle() # Hides the turtle so that there is no distraction

    turtle.begin_fill()
    turtle.fillcolor("#80591E")
    for x in range(0,3):
        turtle.forward(260)
        turtle.left(90)
    turtle.end_fill()

    # End of background creation

    colors = "#ff0000, #f27979, #ffd9bf, #ffee00, #5b8c23, #a3d9c7, #00c2f2, #3d6df2, #5f00b3, #590053, #bf6086, #e50000, #7f4840, #4c3213, #736f39, #2b3326, #00e6b8, #003666, #bfd0ff, #9e86b3, #f200a2, #4c1322, #d90000, #ff8c40, #734d00, #dae6ac, #144d00, #397367, #3385cc, #202080, #9559b3, #ffbfea, #594349, #660000, #995426, #bfa330, #a1f200, #40ff73, #003033, #607180, #170d33, #d600e6, #d90057"
    unique_color = colors.split(", ")
    color_counter = 0

    for block in sliding_block:
        split_str = block.split(" ")
        turtle.penup()
        turtle.begin_fill()
        turtle.fillcolor(unique_color[color_counter])
        turtle.goto((int(split_str[1]) -1) * 40 +10 , (int(split_str[0])) * 40 +10)
        if(split_str[3] == "h"):
            for _ in range(2):
                turtle.forward(40)
                turtle.left(90)
                turtle.forward(int(split_str[2]) * 40)
                turtle.left(90)
        if(split_str[3] == "v"):
            for _ in range(2):
                turtle.forward(int(split_str[2]) * 40)
                turtle.left(90)
                turtle.forward(40)
                turtle.left(90)
        turtle.end_fill()
        color_counter += 1
    time.sleep(5)
