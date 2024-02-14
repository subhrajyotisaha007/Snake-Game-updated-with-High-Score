from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP =90
DOWN =270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.all_squares =[]
        self.create_snake()
        self.head = self.all_squares[0]


    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self,position):
        tim = Turtle()
        tim.color('white')
        tim.shape('square')
        tim.penup()
        tim.goto(position)
        self.all_squares.append(tim)

    def reset(self):
        for seg in self.all_squares:
            seg.goto(1000,1000)
        self.all_squares.clear()
        self.create_snake()
        self.head = self.all_squares[0]

    def extend(self):
        self.add_segment(self.all_squares[-1].position())


    def move(self):
        for sega_num in range((len(self.all_squares)-1),0,-1):
            new_x = self.all_squares[sega_num-1].xcor()
            new_y = self.all_squares[sega_num-1].ycor()
            self.all_squares[sega_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
