from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, speed):
        super().__init__()
        self.speed = speed
        self.shape('square')
        self.shapesize(0.1, 5)
        self.penup()
        self.color('white')
        self.goto(x, -250)

    # Solved with mouse interaction
    # def move_right(self):
    #     self.setx(self.xcor() + self.speed)
    #
    # def move_left(self):
    #     self.setx(self.xcor() - self.speed)

    def move(self, event):
        i = event.x - 400
        self.setx(i)

