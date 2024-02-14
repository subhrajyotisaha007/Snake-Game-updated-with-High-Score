from turtle import Turtle
ALIGHNMENT = 'center'
FONT = ('Courier',24,'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as highscore:
            self.highscore = int(highscore.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.updated_score()
    def updated_score(self):
        self.clear()
        self.write(f'score: {self.score} HighSchore: {self.highscore}', align=ALIGHNMENT, font= FONT)
    def point(self):
        self.score += 1
        self.updated_score()

    def resetscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', 'w') as new_high_score:
                new_high_score.write(f'{self.highscore}')
        #self.score = 0
        #self.updated_score()


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.updated_score()
        self.goto(0, 30)
        self.write('GAME OVER',align=ALIGHNMENT,font=FONT)

