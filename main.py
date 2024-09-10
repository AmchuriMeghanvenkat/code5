from turtle import Turtle,Screen
import random
is_race_on=False
all_turtles=["timmy","nani","meghan","venkat","harsha"]
timmy=Turtle("turtle")
nani=Turtle("turtle")
meghan=Turtle("turtle")
venkat=Turtle("turtle")
harsha=Turtle("turtle")


def color():
    timmy.color('black')
    nani.color('red')
    meghan.color('green')
    venkat.color('pink')
    harsha.color('orange')
def pen_up():
    timmy.penup()
    nani.penup()
    meghan.penup()
    venkat.penup()
    harsha.penup()
def start(x,y,):
    timmy.goto(-230, -100)
    nani.goto(-230, -50)
    meghan.goto(-230, 0)
    venkat.goto(-230, 50)
    harsha.goto(-230, 100)

screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput("Make your bet",
                 "which turtle will win the race?Enter a color:")

start(pen_up(),color())
if user_bet:
    is_race_on=True
while is_race_on:
        rand_distance=random.randint(0,20)
        timmy.forward(rand_distance)
        rand_distance = random.randint(0, 20)
        nani.forward(rand_distance)
        rand_distance = random.randint(0, 20)
        meghan.forward(rand_distance)
        rand_distance = random.randint(0, 20)
        venkat.forward(rand_distance)
        rand_distance = random.randint(0, 20)
        harsha.forward(rand_distance)
        if timmy.xcor()>210 or meghan.xcor()>210 or venkat.xcor()>210 or nani.xcor()>210 or harsha.xcor()>210:

            is_race_on = False

start(pen_up(),color(),speed())

screen.exitonclick()