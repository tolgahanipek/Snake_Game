import turtle
import time
import random
speed=0.1
score=1
window=turtle.Screen()
window.title("Snake_Game")
window.bgcolor('lightblue')
window.setup(width=700,height=700)
window.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("brown")
head.penup()
head.goto(0,100)
head.direction="stop"

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,0)
food.direction="stop"
food.shapesize(0.8,0.8)

text=turtle.Turtle()
text.speed(0)
text.shape("square")
text.color("white")
text.penup()
text.goto(0,300)
text.hideturtle()
text.write("SCORE: {}".format(score),align="center",font=("Courier",24,"normal"))

queues=[]



def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x -20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def goUp():
    if head.direction!="down":
        head.direction="up"

def goDown():
    if head.direction!="up":
        head.direction="down"

def goLeft():
    if head.direction!="right":
        head.direction="left"

def goRight():
    if head.direction!="left":
        head.direction="right"

window.listen()
window.onkey(goUp,'Up')
window.onkey(goDown,'Down')
window.onkey(goRight,'Right')
window.onkey(goLeft,'Left')


while True:
    window.update()
    for queuey in queues:
        if head.xcor()==queuey.xcor() and head.ycor()==queuey.ycor():
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for queuey in queues:
                queuey.goto(1000, 1000)
            queues = []
            score = 0
            text.write("SCORE: {}".format(score), align="center", font=("Courier", 24, "normal"))
            speed = 0.15
            break

    if head.xcor()>350 or head.xcor()<-350 or head.ycor()>350 or head.ycor()<-350:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"


        for queuey in queues:
         queuey.goto(1000,1000)

        queues = []
        score = 0
        text.write("SCORE: {}".format(score), align="center", font=("Courier", 24, "normal"))
        speed=0.15



    if head.distance(food)<20:
        x=random.randint(-350,350)
        y=random.randint(-350,350)
        food.goto(x,y)
        score+=10
        text.clear()
        text.write("SCORE: {}".format(score), align="center", font=("Courier", 24, "normal"))

        speed=speed-0.001

        newQueue=turtle.Turtle()
        newQueue.speed(0)
        newQueue.shape('square')
        newQueue.color('red')
        newQueue.penup()
        queues.append(newQueue)

    for i in range(len(queues)-1,0,-1):
            x=queues[i-1].xcor()
            y=queues[i-1].ycor()
            queues[i].goto(x,y)

    if len(queues)>0:
        x=head.xcor()
        y=head.ycor()
        queues[0].goto(x,y)

    move()
    time.sleep(speed)





