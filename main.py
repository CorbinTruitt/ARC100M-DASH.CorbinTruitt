import turtle
from turtle import Turtle, Screen, listen, onkey
from random import randint
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(1)

def run():
    runner1.forward(10)
listen()
onkey(run, "Right")

screen.bgpic("Track.gif")
screen.addshape("SimpsonLogo.gif")
screen.addshape("CentralLogo.gif")
screen.addshape("WartburgLogo.gif")
screen.addshape("LorasLogo.gif")
screen.addshape("DubuqueLogo.gif")
screen.addshape("LutherLogo.gif")
screen.addshape("NWLogo.gif")

ref = Turtle()
ref.penup()
ref.hideturtle()
ref.write("Welcome to the ARC 100m Dash!", move=False, align='center', font=('Arial', 15, 'normal'))
time.sleep(5)
ref.clear()
ref.write("When you see *BANG*, press the right arrow key as fast as you can.", move=False, align='center', font=('Arial', 15, 'normal'))
time.sleep(5)
ref.clear()


# yPositions = [-260, -172, -85, 2, 85, 172, 260]
#logos = ["SimpsonLogo.gif", "CentralLogo.gif", "WartburgLogo.gif", "LorasLogo.gif", "DubuqueLogo.gif", "LutherLogo.gif", "NWLogo.gif"]
turtle.penup()
turtle.goto(x=100, y=350)
turtle.pendown()
turtle.pensize(3)
turtle.goto(x=100, y=-350)


runner1 = Turtle(shape="SimpsonLogo.gif")
runner1.penup()
runner1.shapesize(2)
runner1.goto(x=-350, y=-260)


runner2 = Turtle(shape="CentralLogo.gif")
runner2.penup()
runner2.shapesize(2)
runner2.goto(x=-350, y=-172)

runner3 = Turtle(shape="WartburgLogo.gif")
runner3.penup()
runner3.shapesize(2)
runner3.goto(x=-350, y=-85)

runner4 = Turtle(shape="LorasLogo.gif")
runner4.penup()
runner4.shapesize(2)
runner4.goto(x=-350, y=2)

runner5 = Turtle(shape="DubuqueLogo.gif")
runner5.penup()
runner5.shapesize(2)
runner5.goto(x=-350, y=85)

runner6 = Turtle(shape="LutherLogo.gif")
runner6.penup()
runner6.shapesize(2)
runner6.goto(x=-350, y=172)

runner7 = Turtle(shape="NWLogo.gif")
runner7.penup()
runner7.shapesize(2)
runner7.goto(x=-350, y=260)

ref.write("On your marks,", move=False, align='right', font=('Arial', 15, 'normal'))
time.sleep(1)
ref.clear()
ref.write("Get set,", move=False, align='right', font=('Arial', 15, 'normal'))
time.sleep(1)
ref.clear()
ref.write("BANG", move=False, align='right', font=('Arial', 70, 'normal'))
time.sleep(.5)
ref.clear()

podium1 = []
for x in range(105):
    if runner1.xcor() > 100 and podium1.count("Simpson College") == 0:
        podium1.append("Simpson College")
        # print(podium1)
    if runner2.xcor() > 100 and podium1.count("Central College") == 0:
        podium1.append("Central College")
        # print(podium1)
    if runner3.xcor() > 100 and podium1.count("Wartburg College") == 0:
        podium1.append("Wartburg College")
        # print(podium1)
    if runner4.xcor() > 100 and podium1.count("Loras College") == 0:
        podium1.append("Loras College")
        # print(podium1)
    if runner5.xcor() > 100 and podium1.count("University of Dubuque") == 0:
        podium1.append("University of Dubuque")
        # print(podium1)
    if runner6.xcor() > 100 and podium1.count("Luther College") == 0:
        podium1.append("Luther College")
        # print(podium1)
    if runner7.xcor() > 100 and podium1.count("Nebraska Wesleyan University") == 0:
        podium1.append("Nebraska Wesleyan University")
        # print(podium1)
    spd2 = randint(1, 9)
    spd3 = randint(1, 9)
    spd4 = randint(1, 9)
    spd5 = randint(1, 9)
    spd6 = randint(1, 9)
    spd7 = randint(1, 9)
    #   runner1.forward(randint(1, 10))
    runner2.forward(spd2 * 1)
    runner3.forward(spd3 * 1)
    runner4.forward(spd4 * 1)
    runner5.forward(spd5 * 1)
    runner6.forward(spd6 * 1)
    runner7.forward(spd7 * 1)
time.sleep(2)
print("First Place: " + podium1[0])
print("Second Place: " + podium1[1])
print("Third Place: " + podium1[2])
#        if runner1.pos() == (300, -260):
#            runner1.write("First Place", move=False, align='left', font=('Arial', 8, 'normal'))
runner1.hideturtle()
runner2.hideturtle()
runner3.hideturtle()
runner4.hideturtle()
runner5.hideturtle()
runner6.hideturtle()
runner7.hideturtle()



runner1.goto(x=-350, y=-260)
runner2.goto(x=-350, y=-172)
runner3.goto(x=-350, y=-85)
runner4.goto(x=-350, y=2)
runner5.goto(x=-350, y=85)
runner6.goto(x=-350, y=172)
runner7.goto(x=-350, y=260)

ref = Turtle()
ref.hideturtle()
ref.goto(x=60,y=0)
ref.goto(x=-150, y=0)
ref.write("Welcome to the Finals!!!", move=False, align='left', font=('Arial', 15, 'normal'))
time.sleep(5)
ref.clear()
ref.penup()
ref.goto(x=-200, y=0)
ref.write("The competition will be harder, so get ready.", move=False, align='left', font=('Arial', 15, 'normal'))
time.sleep(5)
ref.clear()

runner1.showturtle()
runner2.showturtle()
runner3.showturtle()
runner4.showturtle()
runner5.showturtle()
runner6.showturtle()
runner7.showturtle()

ref.write("On your marks,", move=False, align='left', font=('Arial', 15, 'normal'))
time.sleep(1)
ref.clear()
ref.write("Get set,", move=False, align='left', font=('Arial', 15, 'normal'))
time.sleep(1)
ref.clear()
ref.write("BANG", move=False, align='left', font=('Arial', 70, 'normal'))
time.sleep(.5)
ref.clear()

podium2 = []
for x in range(50):
    if runner1.xcor() > 100 and podium2.count("Simpson College") == 0:
        podium2.append("Simpson College")
        # print(podium2)
    if runner2.xcor() > 100 and podium2.count("Central College") == 0:
        podium2.append("Central College")
        # print(podium2)
    if runner3.xcor() > 100 and podium2.count("Wartburg College") == 0:
        podium2.append("Wartburg College")
        # print(podium2)
    if runner4.xcor() > 100 and podium2.count("Loras College") == 0:
        podium2.append("Loras College")
        # print(podium2)
    if runner5.xcor() > 100 and podium2.count("University of Dubuque") == 0:
        podium2.append("University of Dubuque")
        # print(podium2)
    if runner6.xcor() > 100 and podium2.count("Luther College") == 0:
        podium2.append("Luther College")
        # print(podium2)
    if runner7.xcor() > 100 and podium2.count("Nebraska Wesleyan University") == 0:
        podium2.append("Nebraska Wesleyan University")
        # print(podium2)

    spd2 = randint(1, 9)
    spd3 = randint(1, 9)
    spd4 = randint(1, 9)
    spd5 = randint(1, 9)
    spd6 = randint(1, 9)
    spd7 = randint(1, 9)
    #   runner1.forward(randint(1, 10))
    runner2.forward(spd2 * randint(1, 3))
    runner3.forward(spd3 * randint(1, 3))
    runner4.forward(spd4 * randint(1, 3))
    runner5.forward(spd5 * randint(1, 3))
    runner6.forward(spd6 * randint(1, 3))
    runner7.forward(spd7 * randint(1, 3))
time.sleep(1)
print("Conference Champion: " + podium2[0])
print("Conference Runner-up: " + podium2[1])
print("Conference Second Runner-up: " + podium2[2])


# if runner1.xcor() > 100:
#     podium1.append("Simpson College")
#     runner1.write("Hello", move=False, align='left', font=('Arial', 8, 'normal'))
# if runner2.xcor() > 100:
#     podium1.append("Central college")
# if runner3.xcor() > 100:
#     podium1.append("Wartburg college")

runner1.hideturtle()
runner2.hideturtle()
runner3.hideturtle()
runner4.hideturtle()
runner5.hideturtle()
runner6.hideturtle()
runner7.hideturtle()


turtle.clear()
ref.write("Thanks for playing!!!", move=False, align='left', font=('Arial', 50, 'normal'))

screen.exitonclick()





