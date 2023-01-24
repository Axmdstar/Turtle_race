import turtle as tur
import random




screen = tur.Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Bet", prompt="Place Your Bet Here:")
colors = ["red", "yellow", "blue", "orange", "violet", "green", "indigo"]
y_pos = [0, 20, -20, 40, -40, 60, -60]
all_turtles = []




for index in range(0, 7):
    tu = tur.Turtle(shape="turtle")
    tu.penup()
    tu.color(colors[index])
    tu.goto(x=-240, y=y_pos[index])
    all_turtles.append(tu)

line_tu = tur.Turtle()
line_tu.hideturtle()
line_tu.penup()
line_tu.goto(x=235, y=79)
line_tu.pencolor("cyan")
line_tu.width(10)
line_tu.pendown()
line_tu.goto(x=235, y=-79)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtles in all_turtles:
        if turtles.xcor() > 220:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You Won! {winning_color} wins")
            else:
                print(f"You Lose! {winning_color} wins")

        rand_dist = random.randint(0, 10)
        turtles.forward(rand_dist)



screen.exitonclick()
