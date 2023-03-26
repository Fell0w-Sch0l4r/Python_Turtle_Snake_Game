from turtle import Screen
from time import sleep
from food import Food
from scoreboard import ScoreBoard
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()  
food = Food()
score_board = ScoreBoard()

screen.listen()

screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)



while True:
    screen.update()
    sleep(0.1)
    snake.move()
    
    
    #Detect colision with the wall
    if snake.in_edge():
        score_board.reset()
        snake.reset()
        
    
    
    #Detect contact with the food
    if snake.head.distance(food) < 20:
        score_board.increase_score()
        
        food.random_location()
        
        snake.extend()

    #detect colision with the tail
    if snake.touch_tail():
        score_board.reset()
        snake.reset()
        
        
        
    
    
    


screen.exitonclick()