import turtle

def draw_square(brad):


    for i in range(1,5):
        brad.forward(100)
        brad.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(100)
    for i in range(1,361):
        draw_square(brad)
        brad.right(1)
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #draw_circle(angie)
    window.exitonclick()



def draw_circle(angie):
    angie.circle(100)

draw_art()


