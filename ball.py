from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.sety(-200)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y_paddle(self, paddle):
        self.x_move = (self.xcor() - paddle.xcor()) * 0.3
        self.y_move *= -1

    def collide_with_tile(self, tiles):
        for tile in tiles:
            if tile.distance(self) < 50:
                tile.goto(1000, 1000)
                tiles.remove(tile)
                self.bounce_y()

    def reset_position(self):
        self.x_move = 10
        self.y_move = 10
        self.goto(random.randint(-350, 350), -200)
        self.bounce_x()
