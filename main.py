import time
import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from tile import Tile
from winner import Winner

screen = Screen()
screen.bgcolor('black')
screen.title('Breakout')
screen.setup(800, 600)
screen.tracer(0)
canvas = turtle.getcanvas()

paddle = Paddle(0, 50)
ball = Ball()
tiles = []
canvas.bind('<Motion>', paddle.move)

for i in range(10):
    for j in range(5):
        tile = Tile(355 - i * 80, 250 - j * 30)
        tiles.append(tile)

# Solves with mouse interaction
# screen.listen()
# screen.onkey(paddle.move_right, 'd')
# screen.onkey(paddle.move_left, 'a')

game_is_on = True
game_state = 1

while game_is_on:

    if game_state == 1:
        screen.update()

        ball.move()
        ball.collide_with_tile(tiles)

        if ball.ycor() > 280:
            ball.bounce_y()

        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()

        if paddle.ycor() - 15 < ball.ycor() < paddle.ycor() + 15 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
            ball.sety(ball.ycor() + 10)
            ball.bounce_y_paddle(paddle)

        if ball.ycor() < -500:
            ball.reset_position()

        if len(tiles) == 0:
            ball.hideturtle()
            paddle.hideturtle()
            game_state = 0
            screen.tracer(1, 0)
    elif game_state == 0:
        winner = Winner()
        winner.display_winner_label()

screen.exitonclick()

# TASK3 Better paddle controlling
