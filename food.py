"""Food module: provides a `Food` turtle used as the snake's target.

`Food` inherits from `turtle.Turtle` and places itself at a random
location inside the playfield when created or when `random_location()` is called.
"""

from turtle import Turtle

from random import randint


class Food(Turtle):
    """A small circular turtle representing food for the snake.

    Methods
    -------
    random_location()
        Move the food to a new random position inside the playfield.
    """
    
    def __init__(self) -> None:
        super().__init__()
        
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        
        self.random_location()
        
        
        
    def random_location(self):
        """Place the food at a random (x, y) within +/-280 pixels."""
        randomx = randint(-280, 280)
        randomy = randint(-280, 280)
        
        self.setpos(x=randomx, y=randomy)