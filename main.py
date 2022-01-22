import turtle #helps build games in python, pygame is another example
import os #helps us use basoc os calls

wn = turtle.Screen() #creates the game screen
wn.title("Pong by Rahul Jestadi")
wn.bgcolor("black") #to pick color of background
wn.setup(width=800, height=600) #adjusts the size of the screen
wn.tracer(0) #stops window from updating, speeds up the game

#Score
score_a = 0
score_b = 0

#Main Game Loop

#Paddle A
paddle_a = turtle.Turtle() #When a Turtle object is
                            # created or a function derived from some Turtle method is
                            # called a TurtleScreen object is automatically created
paddle_a.speed(0) #sets max possible speed
paddle_a.shape("square") #give paddle a shape
paddle_a.color("white") #paddle color
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #avoids to draw line when moving
paddle_a.goto(-350,0) #places it in the left side (left paddle)

#Paddle B

paddle_b = turtle.Turtle() #When a Turtle object is
                            # created or a function derived from some Turtle method is
                            # called a TurtleScreen object is automatically created
paddle_b.speed(0) #sets max possible speed
paddle_b.shape("square") #give paddle a shape
paddle_b.color("white") #paddle color
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #avoids to draw line when moving
paddle_b.goto(350,0)  #places it in right (right paddle)

#Ball

ball = turtle.Turtle() #When a Turtle object is
                            # created or a function derived from some Turtle method is
                            # called a TurtleScreen object is automatically created
ball.speed(0) #sets max possible speed
ball.shape("circle") #give paddle a shape
ball.color("white") #paddle color
ball.penup() #avoids to draw line when moving
ball.goto(0,0)  #places it in right (right paddle)

ball.dx = 2 #change in x (moves by 2px)
ball.dy = 2 #change in y (moves up 2px)  #so up and diagonal

#Pen
pen = turtle.Turtle()
pen.speed(0) #animation, not movement speed
pen.color("white")
pen.penup() #to just freeze the position
pen.hideturtle() #hide cause we dont want to see, just need the text
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24, "normal"))


#Functions

#for paddle a upwards
def paddle_a_up():
    y = paddle_a.ycor() #returns y coordinate and add it to y
    y += 20 #add 20px to y coordinate
    paddle_a.sety(y) #sets y to the new y

#for paddle a downwards
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#for paddle b upwards
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


#for paddle b downwards
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard Binding

wn.listen() #listens for the keyboard
wn.onkeypress(paddle_a_up, "Up") #when up is pressed, it calls function paddle_a_up
wn.onkeypress(paddle_a_down, "Down") #when down is pressed, it calls function paddle_a_down
wn.onkeypress(paddle_b_up, "w") #when w is pressed, it calls function paddle_a_down
wn.onkeypress(paddle_b_down, "s") #when s is pressed, it calls function paddle_a_down

while True:
    wn.update() #everytime loop runs, screen is updated


    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses the direction of the ball, dy becomes -2
        os.system("afplay bounce.wav&") #sound, add ampersand to keep it clean, or it crashes

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #reverses the direction of the ball, dy becomes -2
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1 #the borders for the sides, right border
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0) #the borders for the sides, left border
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 #hits and reverses
        os.system("afplay bounce.wav&")
    #edges basically touching and is it anywhere top or bottom of the paddle

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")



