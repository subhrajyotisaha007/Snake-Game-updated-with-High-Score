from turtle import Screen
from snake import Snake
from food import Food
import time
from score import Score
from bigfood import BigFood


screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor('black')
screen.title('Hello Snakes')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
bigfood = BigFood()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #big food
    if score.score >=5 and score.score%5 == 0:
        bigfood.show_bigfood()
        screen.ontimer(bigfood.off,2000)
        screen.ontimer(bigfood.refresh,8000)
        screen.update()
        if snake.head.distance(bigfood) < 20:
            bigfood.refresh()
            snake.extend()
            snake.extend()
            score.point()
            score.point()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.point()
    #Detec collision
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.resetscore()
        #snake.reset()
        game_on = False
        score.game_over()

    for i in snake.all_squares[1:]:
        if snake.head.distance(i) < 10:
            score.resetscore()
            #snake.reset()
            score.game_over()
            game_on = False



screen.exitonclick()
