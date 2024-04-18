import turtle
 
def instructions() :
    """informs the user about this program, get user's shape choice,
    send users shape to the draw_shape function """
    print("Welcome to my app !!! \nI draw shapes")
    print("What shape would you like to see ?")
    prompt = ("Circle(C) , Square(S) , Triangle(T) \n>")

    #get shape
    shape = input(prompt).upper()
    while shape not in ["C" , "S" , "T"] :
        shape = input(prompt).upper()

    #draw user's selected shape
    draw_shape(shape)


# shape drawer factory:
def draw_shape(shapeShortName) :
    """selects which shape-drawer to choose according to shapeShortName,
    send users shape to the proper drawer function """
    #setup the window
    drawing_surface = turtle.Screen()

    #create a turtle object
    myTurtle = turtle.Turtle()

    #Set the shape and pen color
    myTurtle = turtle.shape("turtle")
    myTurtle = turtle.color("red")

    #select shape-drawer with respect to user's choice of shape-short-name 
    if shapeShortName == "C" :
        draw_circle()
    elif shapeShortName == "T" :
        draw_triangle()
    elif shapeShortName == "S" :
        draw_square()

    #exits properly
    drawing_surface.exitonclick()


# drawer functions :
def draw_circle() :
    """--Draws square shape--"""
    turtle.circle(80)

def draw_triangle() :
    """--Draws square shape--"""
    #set the side-length size and rotaion degree for drawer
    size = 80
    rotation_degree = 120

    # drawing first side
    turtle.forward(size) # Forward turtle by size units
    turtle.left(rotation_degree) # Turn turtle by 120 degree

    # drawing secodn side
    turtle.forward(size) # Forward turtle by size units
    turtle.left(rotation_degree) # Turn turtle by 120 degree

    # drawing third side
    turtle.forward(size) # Forward turtle by size units
    turtle.left(rotation_degree) # Turn turtle by 120 degree

def draw_square() :
    """--Draws square shape--"""
    #set the side-length size and rotaion degree for drawer
    size = 80
    rotation_degree = 90

    # drawing first side
    turtle.forward(size) # Forward turtle by size units
    turtle.left(rotation_degree) # Turn turtle by 90 degree
    
    # drawing second side
    turtle.forward(size) # Forward turtle by size units
    turtle.left(rotation_degree) # Turn turtle by 90 degree
    
    # drawing third side
    turtle.forward(size) # Forward turtle by size units
    turtle.left(rotation_degree) # Turn turtle by 90 degree
    
    # drawing fourth side
    turtle.forward(size) # Forward turtle by size units
    turtle.left(rotation_degree) # Turn turtle by 90 degree


# User intractions part :
instructions()