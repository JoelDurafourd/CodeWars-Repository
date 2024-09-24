from turtle import Turtle, Screen
import random

is_race_on = False
turtles = []
colors = ["green", "violet", "blue", "black", "orange", "purple"]
y_start_position = -100

screen = Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Entenr a color: ")
screen.setup(width=500, height=400)

for color in colors:
  turtle = Turtle(shape="turtle")
  turtle.color(color)
  turtles.append(turtle)
  turtle.penup()
  turtle.goto(x = -240, y = y_start_position)
  y_start_position += 30

if user_bet:
  is_race_on = True

while is_race_on:

  for turtle in turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner.")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner.")

    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)


screen.exitonclick()
