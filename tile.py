from turtle import Turtle


class Tile(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 3.5)
        self.penup()
        self.color('white')
        self.goto(x, y)
