from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.score = 0
        
        self.hideturtle()
        self.penup()
        self.color("white")
        self.sety(270)
        
        self.update_score_board()
        
        
    def update_score_board(self):
        
        self.text = f"Score: {self.score}"
        
        self.write(arg=self.text, align=ALIGNMENT, font=FONT)
        
        
    
    def increase_score(self):
        self.score += 1
        self.clear()
        
        self.update_score_board()
        
        
    def game_over(self):
        self.setpos(x=0, y=0)
        self.color("red")
        
        self.text = "GAME OVER"
        
        self.write(arg=self.text, align=ALIGNMENT, font=FONT)
        
        
        