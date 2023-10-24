import turtle

wn=turtle.Screen()
wn.title("Pong by Nirmala")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a=0
score_b=0
# Person A
paddle_a=turtle.Turtle()
#animation speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Person B
paddle_b=turtle.Turtle()
#animation speed
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball=turtle.Turtle()
#animation speed
ball.speed(0)
ball.shape("circle")
ball.color('white')
ball.penup()
ball.goto(0,0)
##moves 2 pixels every time
ball.dx=0.05
ball.dy=-0.05

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}        Player B: {}".format(score_a,score_b),align="center", font={"Courier",24, "normal"})

#Function to handle padles
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard binding
#listens keyboard input
wn.listen()
wn.onkeypress(paddle_a_up,"4")
wn.onkeypress(paddle_a_down,"1")
wn.onkeypress(paddle_b_up,"5")
wn.onkeypress(paddle_b_down,"2")
while True:
    wn.update()
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border check
    #top border
    if(ball.ycor()>290):
        ball.sety(290)
        ball.dy*=-1
    #bottom border
    if(ball.ycor()<-290):
        ball.sety(-290)
        ball.dy*=-1
    #left border
    if(ball.xcor()>390):
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}        Player B: {}".format(score_a,score_b),align="center", font={"Courier",24, "normal"})

    if(ball.xcor()<-390):
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}        Player B: {}".format(score_a,score_b),align="center", font={"Courier",24, "normal"})

    ##collisons
    if(ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-40)):
        ball.setx(340)
        ball.dx*=-1
    if(ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-40)):
        ball.setx(-340)
        ball.dx*=-1
    if(paddle_a.ycor()>250):
        paddle_a.sety(250)
    if(paddle_a.ycor()<-250):
        paddle_a.sety(-250)
    if(paddle_b.ycor()>250):
        paddle_b.sety(250)
    if(paddle_b.ycor()<-250):
        paddle_b.sety(-250)
    




