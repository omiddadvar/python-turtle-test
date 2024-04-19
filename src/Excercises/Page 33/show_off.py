import turtle
import random

def initialize() :
   
    userClickLogs = []

    turtle.speed(0)
    turtle.shape("turtle")
    turtle.left(90)

def get_user_info():
    title = "User information"
    prompt = "What is your name (at least three characters)?"
    
    name = ""
    while len(name) < 3 : 
        name = turtle.textinput(title, prompt) 
        if(name is None) : 
            return None
    
    return name


def get_welcome_message_configs() :
    configs = {
        "font" : {
            "name" : "ariel",
            "size" : 20,
            "weight" : "bold"
        },
        "move" : True
    }
    return configs

def get_instruction_message_configs() :
    configs = {
        "font" : {
            "name" : "ariel",
            "size" : 15,
            "weight" : "normal"
        },
        "move" : True
    }
    return configs

def get_screen_configs() :
    screenWidth = screen.window_width() 
    screenHeight = screen.window_height() 
    return {
        "width" : screenWidth,
        "height" : screenHeight
    }

def print_welcome_message(name, screenConfigs,configs):
    turtle.penup()
    turtle.goto(-1 * screenConfigs["width"] /2 + 30  , screenConfigs["height"] /2 - 50)
    turtle.pendown()

    message = "Welcome to my app '" + name + "'"
    turtle.write(message , configs["move"] , font=(configs["font"]["name"] , configs["font"]["size"] , configs["font"]["weight"]))

def print_instruction_message(screenConfigs,configs):
    turtle.penup()
    turtle.goto(-1 * screenConfigs["width"] /2 + 30  , screenConfigs["height"] /2 - 80)
    turtle.pendown()

    instructions = "Click anywhere on this screen to see the star !!!"
    turtle.write(instructions , configs["move"] , font=(configs["font"]["name"] , configs["font"]["size"] , configs["font"]["weight"]))


def get_random_color() :
    permitted_colors = ["orange" , "green" , "blue" , "red"]
    return random.choice(permitted_colors)


def onclick_action(x , y):
    global working
    if working is True: 
        return
    
    turtle.penup()
    turtle.goto(x, y) 
    turtle.pendown()

    draw_star_fractal(3 , 20 , get_random_color())
    working = False


def set_onclick_listener() :
    # turtle.onclick(onclick_action) 
    screen.onclick(onclick_action) 
    screen.mainloop()


def draw_star_fractal(level , length , color):
    global working
    working = True

    turtle.fillcolor(color)
    if level > 0 :
        for i in range(5) :
             #go forward to draw a circle
            turtle.penup()
            turtle.forward(length)
            turtle.pendown()

            #draw a circle
            turtle.begin_fill()
            turtle.circle(5)
            turtle.end_fill()

            #go back to the first position
            turtle.penup()
            turtle.back(length)
            turtle.pendown()

            turtle.left(72)
        draw_star_fractal(level - 1 , length + 20 , color)
    else :
        return

#------------------------------------------
#---------------Main program---------------
#------------------------------------------


screen = turtle.Screen()
working = False

initialize()

username = get_user_info()

if username is not None :
    welcomeMessageConfig = get_welcome_message_configs()
    welcomeScreenConfigs = get_screen_configs()
    instructionMessageConfig = get_instruction_message_configs()
    print_welcome_message(username, welcomeScreenConfigs ,welcomeMessageConfig)
    print_instruction_message(welcomeScreenConfigs ,instructionMessageConfig)

    set_onclick_listener()

#screen.exitonclick()