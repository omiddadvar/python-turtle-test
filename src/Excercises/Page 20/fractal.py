import turtle

# def get_user_choices():
#     """ Build a dictionary of user choices for f """


def draw(level , length):
    turtle.shape("turtle")
    if level > 0 :
        # turtle.penup()
        turtle.forward(length)
        # turtle.pendown()
        
        turtle.left(40)
        draw( level-1 , length / 1.61)

        turtle.right(80)
        draw( level-1 , length / 1.61)
        # for i in range(4) :
        #     turtle.left(90)
        #     draw( level -1 , length * 1.5)
        print("is going back level : " + str(level))
        turtle.left(40)
        turtle.back(length)
    else :
        turtle.stamp()

drawinf_serface = turtle.Screen()

turtle.width(3)
turtle.speed(0)
turtle.goto(0 , -180)
turtle.left(90)

draw(6,200)

drawinf_serface.exitonclick()