#
#Kponyo JDK - Pong Game
#

import turtle as t
import os

# Score varibales

player_1_score = 0
player_2_score = 0

win = t.Screen()    #window
win.title("Kponyo JDK | Ping-Pong Game")
win.bgcolor('black')  
win.setup(width=800,height=600)
win.tracer(0) #speed game up

# left paddle
paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('blue')
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

# right paddle 
paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.color('orange')
paddle_right.penup()
paddle_right.goto(350,0)

# Pong ball
ball = t.Turtle()
ball.speed(10)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0,0)
ball_dx = 0.3   # Pixels setup for ball movement.
ball_dy = 0.3

#Score update pen
pen = t.Turtle()
pen.speed(0)
pen.color('gray')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0                    Player 2: 0 ",align="center",font=('Monaco',24,"normal"))


# Move left Paddle up
def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 15
    paddle_left.sety(y)

# Move left paddle down
def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 15
    paddle_left.sety(y)

# Move right paddle up
def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 15
    paddle_right.sety(y)

# Move right paddle down
def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 15
    paddle_right.sety(y)

# Keyboard binding
win.listen()
win.onkeypress(paddle_left_up,"w")
win.onkeypress(paddle_left_down,"s")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")




# Main Game Loop
while True:
    win.update() # required to run any game

    # Moving ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Border setup
    if ball.ycor() > 290:   # Right top
        ball.sety(290)
        ball_dy = ball_dy * -1
        
    
    if ball.ycor() < -290:  # Left top
        ball.sety(-290)
        ball_dy = ball_dy * -1
        

    if ball.xcor() > 390:   # right width
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_1_score = player_1_score + 1
        pen.clear()
        pen.write("PLAYER A: {}                    PLAYER B: {} ".format(player_1_score,player_2_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wall.wav&")



    if(ball.xcor()) < -390: # Left width
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_2_score = player_2_score + 1
        pen.clear()
        pen.write("PLAYER A: {}                    PLAYER B: {} ".format(player_1_score,player_2_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wall.wav&")


    # Handling the collisions with paddles.
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")
        
        
#***********************
#*******Kponyo JDK******
#***********************
