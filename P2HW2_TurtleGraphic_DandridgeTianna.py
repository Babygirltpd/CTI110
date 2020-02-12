import turtle
turtle.showturtle()

def main():
    turtle.forward (100)
    turtle.write ("EAST")
    turtle.back (100)
    turtle.right (180)
    turtle.forward (100)
    turtle.write("WEST")
    turtle.goto (0,0)
    turtle.right (90)
    turtle.forward (100)
    turtle.write ("NORTH")
    turtle.right (180)
    turtle.forward (200)
    turtle.write ("SOUTH")
    turtle.right (180)
    turtle.penup()
    turtle.goto(25,0)
    turtle.pendown()
    turtle.circle(25)
    


main()

