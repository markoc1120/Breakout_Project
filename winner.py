from turtle import Turtle


class Winner(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')

    def display_winner_label(self):
        self.write('Win', align='center', font=("Comic Sans MS", 80, "normal"))
        self.goto((0, -40))
        self.write('☞☜', align='center', font=("Comic Sans MS", 40, "normal"))
