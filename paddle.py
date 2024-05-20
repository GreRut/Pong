from turtle import Turtle

MOVE_DISTANCE = 30


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.that_s_a_paddling(position)

    def that_s_a_paddling(self, position):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def down(self):
        self.goto(self.xcor(), self.ycor()-MOVE_DISTANCE)
