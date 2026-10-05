from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score}  HighScore:{self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.update()

    def new_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update()
