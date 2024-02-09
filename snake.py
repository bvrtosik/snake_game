from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for snum in range(len(self.segments) - 1, 0, -1):
            position_snake = self.segments[snum - 1].position()
            self.segments[snum].goto(position_snake)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_segment(self, position):
        snake_seg = Turtle("square")
        snake_seg.color("white")
        snake_seg.penup()
        snake_seg.goto(position)
        self.segments.append(snake_seg)

    def extend(self):
        # add new segment to the snake.
        self.add_segment(self.segments[-1].position())