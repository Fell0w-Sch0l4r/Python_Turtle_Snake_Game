from turtle import Turtle

from random import randint

class Food(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        
        self.random_location()
        
        
        
    def random_location(self):
        randomx = randint(-280, 280)
        randomy = randint(-280, 280)
        
        self.setpos(x=randomx, y=randomy)