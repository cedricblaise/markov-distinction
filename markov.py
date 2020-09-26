import random
import numpy
import sys
from turtle import *

# color states
color_states = ["Red", "Blue", "Green", "Orange", "Yellow"]

# color transition pairs
color_transitions = [["RR", "RB", "RG", "RO", "RY"], ["BR", "BB", "BG", "BO", "BY"], \
    ["GR", "GB", "GG", "GO", "GY"], ["OR", "OB", "OG", "OO", "OY"], ["YR", "YB", "YG", "YO", "YY"]]

# color transition matrix 
color_matrix = [[.1, .3, .2, .3, .1], [.2, .1, .2, .3, .2], [.3, .3, .1, .2, .1], \
    [.2, .2, .2, .1, .3], [.3, .2, .3, .1, .1]]

# shape states
shape_states = ["Square", "Triangle", "Hexagon", "Circle", "Star"]

# shape transition pairs
shape_transitions = [["SS", "ST", "SH", "SC", "SR"], ["TS", "TT", "TH", "TC", "TR"], \
    ["HS", "HT", "HH", "HC", "HR"], ["CS", "CH", "CR", "CC", "CR"], ["RS", "RT", "RH", "SC", "RR"]]

# shape transition matrix 
shape_matrix = [[.1, .1, .4, .3, .1], [.1, .1, .2, .4, .2], [.2, .2, .1, .3, .2], \
    [.3, .1, .3, .1, .2], [.1, .3, .2, .3, .1]]

def main(num_shapes = 15):
    
    # verify probabilities are correct 
    if sum(color_matrix[0]) + sum(color_matrix[1]) + sum(color_matrix[2]) + sum(color_matrix[3]) \
        + sum(color_matrix[4]) != 5:
        print("something went wrong with the color matrix") 
    else:
        print("color matrix is good")

    if sum(shape_matrix[0]) + sum(shape_matrix[1]) + sum(shape_matrix[2]) + sum(shape_matrix[3]) \
        + sum(shape_matrix[4]) != 5:
        print("something went wrong with the shape matrix")
    else:
        print("shape matrix is good")

    color_list = build_color_list(num_shapes)

    shape_list = build_shape_list(num_shapes)

    setup(404, 404)
    screensize(400, 400)
    bgcolor("black")
    speed("normal")
    # penup()
    draw(shape_list, color_list)
    done()
    print("Done!")
    
# determine the order of colors that the shapes will be filled in
def build_color_list(num_shapes):
    current_color = color_states[random.randint(0, len(color_states) - 1)] # randomly select starting color
    color_list = [current_color]

    for i in range(num_shapes):
        if current_color == "Red":
            # pick the transition given the states and probabilities 
            change = numpy.random.choice(color_transitions[0], replace = True, p = color_matrix[0])
            if change == "RR":
                color_list.append("Red")
            elif change == "RB":
                color_list.append("Blue")
                current_color = "Blue"
            elif change == "RG": 
                color_list.append("Green")
                current_color = "Green"
            elif change == "RO":
                color_list.append("Orange")
                current_color = "Orange"
            else: 
                color_list.append("Yellow")
                current_color = "Yellow"

        elif current_color == "Blue":
            change = numpy.random.choice(color_transitions[1], replace = True, p = color_matrix[1])
            if change == "BR":
                color_list.append("Red")
                current_color = "Red"
            elif change == "BB":
                color_list.append("Blue")
            elif change == "BG": 
                color_list.append("Green")
                current_color = "Green"
            elif change == "BO":
                color_list.append("Orange")
                current_color = "Orange"
            else: 
                color_list.append("Yellow")
                current_color = "Yellow"

        elif current_color == "Green":
            change = numpy.random.choice(color_transitions[2], replace = True, p = color_matrix[2])
            if change == "GR":
                color_list.append("Red")
                current_color = "Red"
            elif change == "GB":
                color_list.append("Blue")
                current_color = "Blue"
            elif change == "GG": 
                color_list.append("Green")
            elif change == "GO":
                color_list.append("Orange")
                current_color = "Orange"
            else: 
                color_list.append("Yellow")
                current_color = "Yellow"

        elif current_color == "Orange":
            change = numpy.random.choice(color_transitions[3], replace = True, p = color_matrix[3])
            if change == "OR":
                color_list.append("Red")
                current_color = "Red"
            elif change == "OB":
                color_list.append("Blue")
                current_color = "Blue"
            elif change == "OG": 
                color_list.append("Green")
                current_color = "Green"
            elif change == "OO":
                color_list.append("Orange")
            else: 
                color_list.append("Yellow")
                current_color = "Yellow"

        elif current_color == "Yellow":
            change = numpy.random.choice(color_transitions[4], replace = True, p = color_matrix[4])
            if change == "YR":
                color_list.append("Red")
                current_color = "Red"
            elif change == "YB":
                color_list.append("Blue")
                current_color = "Blue"
            elif change == "YG": 
                color_list.append("Green")
                current_color = "Green"
            elif change == "YO":
                color_list.append("Orange")
                current_color = "Yellow"
            else: 
                color_list.append("Yellow")

    return color_list

# determine the order (and number) of shapes drawn
def build_shape_list(num_shapes):
    current_shape = shape_states[random.randint(0, len(shape_states) - 1)]
    shape_list = [current_shape]

    for i in range(num_shapes):
        if current_shape == "Square":
            change = numpy.random.choice(shape_transitions[0], replace = True, p = shape_matrix[0])
            if change == "SS":
                shape_list.append("Square")
            elif change == "ST":
                shape_list.append("Triangle")
                current_shape = "Triangle"
            elif change == "SH": 
                shape_list.append("Hexagon")
                current_shape = "Hexagon"
            elif change == "SC":
                shape_list.append("Circle")
                current_shape = "Circle"
            else: 
                shape_list.append("Star")
                current_shape = "Star"

        elif current_shape == "Triangle":
            change = numpy.random.choice(shape_transitions[1], replace = True, p = shape_matrix[1])
            if change == "TS":
                shape_list.append("Square")
                current_shape = "Square"
            elif change == "TT":
                shape_list.append("Triangle")
            elif change == "TH": 
                shape_list.append("Hexagon")
                current_shape = "Hexagon"
            elif change == "TC":
                shape_list.append("Circle")
                current_shape = "Circle"
            else: 
                shape_list.append("Star")
                current_shape = "Star"

        elif current_shape == "Hexagon":
            change = numpy.random.choice(shape_transitions[2], replace = True, p = shape_matrix[2])
            if change == "HS":
                shape_list.append("Square")
                current_shape = "Square"
            elif change == "HT":
                shape_list.append("Triangle")
                current_shape = "Triangle"
            elif change == "HH": 
                shape_list.append("Hexagon")
            elif change == "HC":
                shape_list.append("Circle")
                current_shape = "Circle"
            else: 
                shape_list.append("Star")
                current_shape = "Star"

        elif current_shape == "Circle":
            change = numpy.random.choice(shape_transitions[3], replace = True, p = shape_matrix[3])
            if change == "CS":
                shape_list.append("Square")
                current_shape = "Square"
            elif change == "CT":
                shape_list.append("Triangle")
                current_shape = "Triangle"
            elif change == "CH": 
                shape_list.append("Hexagon")
                current_shape = "Hexagon"
            elif change == "CC":
                shape_list.append("Circle")
            else: 
                shape_list.append("Star")
                current_shape = "Star"

        elif current_shape == "Star":
            change = numpy.random.choice(shape_transitions[4], replace = True, p = shape_matrix[4])
            if change == "RS":
                shape_list.append("Square")
                current_shape = "Square"
            elif change == "RT":
                shape_list.append("Triangle")
                current_shape = "Triangle"
            elif change == "RH": 
                shape_list.append("Hexagon")
                current_shape = "Hexagon"
            elif change == "RC":
                shape_list.append("Circle")
                current_shape = "Circle"
            else: 
                shape_list.append("Star")

    return shape_list

# given the shapes and colors, create the art piece
def draw(shape_list, color_list):
    # determine the shape and color to be used at each point
    for i in range(len(shape_list)):
        shape = shape_list[i]
        c = color_list[i]
        if shape == "Square": draw_square(c)
        elif shape == "Triangle": draw_triangle(c)
        elif shape == "Hexagon": draw_hexagon(c)
        elif shape == "Circle": draw_circle(c)
        elif shape == "Star": draw_star(c)
        # randomly select the location of the next shape
        color("white")
        goto(random.randint(-200, 200), random.randint(-200, 200))

def draw_square(c):
    color(c)
    begin_fill()
    s = random.randint(0, 100)  # randomly pick the side length
    for i in range(4): 
        forward(s) 
        right(90) 
    end_fill()

def draw_triangle(c):
    color(c)
    begin_fill()
    s = random.randint(0, 100)
    for i in range(3): 
        forward(s) 
        left(120)
    end_fill()

def draw_hexagon(c):
    color(c)
    begin_fill()
    s = random.randint(0, 100)
    for i in range(6): 
        forward(s) 
        left(60)
    end_fill()

def draw_circle(c):
    color(c)
    begin_fill()
    r = random.randint(0, 100)
    circle(r)
    end_fill()

def draw_star(c):
    color(c)
    begin_fill()
    s = random.randint(0, 100)
    for i in range(5): 
        forward(s) 
        right(144) 
        forward(s) 
        right(-72) 
    end_fill()

if __name__ == "__main__":
    main(int(sys.argv[1])) if len(sys.argv) > 1 else main()