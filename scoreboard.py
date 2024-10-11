from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("C:/Users/Basel/Desktop/files/data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.setposition(0, 260)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score = {self.score}     High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            new_score = self.high_score
            with open("C:/Users/Basel/Desktop/files/data.txt", mode="w") as file:
                file.write(str(new_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def prize_score(self):
        self.score += 10
