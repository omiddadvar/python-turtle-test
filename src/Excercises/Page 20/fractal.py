import turtle

def get_user_choices():
    """ Build a dictionary of user choices for f """
    
    #initilize dictionary
    userChoicesConfigs = {
        "shape" : "turtle",
        "level" : 3,
        "branches" : 3,
        "length" : 50,
    }
    #get number of levels for the fractal
    level = 0
    while level not in range(1,10) :
        level = input("To what level you want the fractal (1 to 10)?")
        level = int(level)
        if level in range(1,10) :
            userChoicesConfigs["level"] = level
    
    #get number of branches for the fractal
    branch = 0
    while branch not in range(1,30) :
        branch = input("How many branches do you want for the fractal (1 to 30)?")
        branch = int(branch)
        if branch in range(1,30) :
            userChoicesConfigs["branch"] = branch
    
    #get initial length of fractal from center
    length = 0
    while length not in range(50,200) :
        length = input("what initial length do you want for the fractal from center (50 to 200)?")
        length = int(length)
        if length in range(1,30) :
            userChoicesConfigs["length"] = length
    
    #return the user-choice-confgis for the fractal
    return userChoicesConfigs


def draw_fractal(drawingConfigs):
    """a recursive function to draw circular-fractal
    drawingConfigs  = a dictionary with level, length, shape and (number of) branches"""
    
    turtle.shape(drawingConfigs["shape"])

    if drawingConfigs["level"] > 0 :
        #creating circular pattern according to number of branches
        for i in range(drawingConfigs["branches"]) :
            #go forward to stamp a turtle
            turtle.penup()
            turtle.forward(drawingConfigs["length"])
            turtle.pendown()

            #stamp a turtle
            turtle.stamp()

            #go back to the first position
            turtle.penup()
            turtle.back(drawingConfigs["length"])
            turtle.pendown()

            #trun 306/branches degree to stamp another turtle
            turtle.left(360 / drawingConfigs["branches"])
    else :
        #exit from function when reached max level of drawing
        return
    #preparing new configs for recursive call
    drawingConfigs["level"] = drawingConfigs["level"] - 1
    drawingConfigs["length"] = drawingConfigs["length"] + 30

    #recursive call to darw the pattern in another level
    draw_fractal(drawingConfigs)


#------ Main program starts here --------

#instructions 
print("Hello this program will draw you a circular-fractal shape")

#initial configs for program 
drawinf_serface = turtle.Screen()
turtle.color("blue")
turtle.speed(0)
turtle.left(90)

#get user input to draw fractal
userChoices = get_user_choices()

#call fractal-drawer function
draw_fractal(userChoices)

#safe exit
drawinf_serface.exitonclick()