from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.score = 0
        self.high_score = self.get_high_score()
        
        self.hideturtle()
        self.penup()
        self.color("white")
        self.sety(270)
        
        self.update_score_board()
        
        
    def get_high_score(self):
        with open("HighScore.txt") as file:
            high_score = int(file.read())
            return high_score
        
        
    def store_high_score(self):
        with open("HighScore.txt", mode="w") as file:
            file.write(str(self.high_score))
    
    
    def update_score_board(self):
        self.clear()
        self.text = f"Score: {self.score} High Score: {self.high_score}"
        
        self.write(arg=self.text, align=ALIGNMENT, font=FONT)
        
        
    
    def increase_score(self):
        self.score += 1
        
        
        self.update_score_board()
        
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_high_score()
            
            
        self.score = 0
        self.update_score_board()
            
        
        
        