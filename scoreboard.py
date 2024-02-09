from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 17, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 270)
        self.update_scr()

    def update_scr(self):
        self.write(f"Score: {self.points}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def add_points(self):
        self.points += 1
        self.clear()
        self.update_scr()
