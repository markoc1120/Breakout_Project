import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from tile import Tile

screen = Screen()
screen.bgcolor('black')
screen.title('Breakout')
screen.setup(800, 600)
screen.tracer(0)

paddle = Paddle(0, 50)
ball = Ball()
tiles = []

for i in range(10):
    for j in range(5):
        tile = Tile(355 - i * 80, 250 - j * 30)
        tiles.append(tile)

screen.listen()
screen.onkey(paddle.move_right, 'd')
screen.onkey(paddle.move_left, 'a')

game_is_on = True

while game_is_on:
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

    # TASK1 Last tile, ball, paddle ain't disappearing
    if len(tiles) == 0:
        ball.hideturtle()
        paddle.hideturtle()
        game_is_on = False

screen.exitonclick()

# TASK2 Making winner state
# TASK3 Better paddle controlling
