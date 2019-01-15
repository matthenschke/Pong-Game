"""
Pong Game using the turtle library
Author: Matthew Henschke
"""
import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Matthew Henschke")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0,0)

#scores
scoreA = 0
scoreB = 0

# Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.shapesize(stretch_wid = 5, stretch_len= 1)
paddle_A.color("white")
paddle_A.penup()
paddle_A.goto(-350,0)

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.shapesize(stretch_wid = 5, stretch_len= 1)
paddle_B.color("white")
paddle_B.penup()
paddle_B.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(2)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

# ball movement
ball.dx = .5
ball.dy = .5

# pen to write out score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# paddle moving functions
def padA_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def padA_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def padB_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)
def padB_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)




# Keyboard binding
wn.listen()

# move paddles up 
wn.onkeypress(padA_up, "w")
wn.onkeypress(padB_up, "Up")


# move paddles down
wn.onkeypress(padA_down, "s")
wn.onkeypress(padB_down, "Down")

if __name__ == "__main__":
    # Main game loop 
    while True:

        wn.update()

        # display score
        pen.clear()    
        pen.write("Player A: {}\tPlayerB : {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))

        # move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            scoreA += 1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            scoreB +=1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # paddle and ball collisions

        # paddle b
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            
        
        # paddle a
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        
        
    

