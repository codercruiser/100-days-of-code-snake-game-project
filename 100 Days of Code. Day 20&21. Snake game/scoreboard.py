import turtle
from turtle import Turtle
FONT = ('courier', 24, 'normal')
ALIGNMENT = 'center'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.wn = turtle.Screen()
        top_height = self.wn.window_height() / 2
        y = top_height - top_height / 10
        self.hideturtle()
        self.setposition(0, y)
        self.color('white')
        self.write(f'score: {self.score}', move=True, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f'score: {self.score}', move=True, align='center', font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(f'GAME OVER', move=True, align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.wn = turtle.Screen()
        top_height = self.wn.window_height() / 2
        y = top_height - top_height / 10
        self.setposition(0, y)
        self.update_scoreboard()



