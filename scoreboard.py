"""Scoreboard module: display and persist player score.

`ScoreBoard` extends `turtle.Turtle` to draw the current score and
high score at the top of the screen. The high score is read from and
written to `HighScore.txt`.
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    """Display and manage the current score and persisted high score.

    Methods
    -------
    get_high_score()
        Read the recorded high score from `HighScore.txt` (returns int).
    store_high_score()
        Write the current high score back to `HighScore.txt`.
    update_score_board()
        Refresh the on-screen score text.
    increase_score()
        Increment the current score by one and update display.
    reset()
        Handle end-of-game: update high score if needed and reset current score.
    """
    
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
        """Return the integer high score read from `HighScore.txt`.

        If the file is missing or empty this will raise an exception,
        matching the original program's expectations.
        """
        with open("HighScore.txt") as file:
            high_score = int(file.read())
            return high_score
        
        
    def store_high_score(self):
        """Persist the current `high_score` value to `HighScore.txt`."""
        with open("HighScore.txt", mode="w") as file:
            file.write(str(self.high_score))
    
    
    def update_score_board(self):
        """Clear and redraw the score and high score at the top of the screen."""
        self.clear()
        self.text = f"Score: {self.score} High Score: {self.high_score}"
        
        self.write(arg=self.text, align=ALIGNMENT, font=FONT)
        
        
    
    def increase_score(self):
        """Increment the current score and refresh the display."""
        self.score += 1
        
        
        self.update_score_board()
        
    
    def reset(self):
        """If current score exceeds high score, update and persist it, then reset."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_high_score()
            
            
        self.score = 0
        self.update_score_board()
            
        
        
        