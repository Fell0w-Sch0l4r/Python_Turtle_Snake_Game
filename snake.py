from turtle import Turtle

STARTING_POSITIONS: tuple = ((0, 0), (-20, 0), (-40, 0))
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0 


class Snake:

    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        tail_size = len(self.segments) - 1
        for seg_num in range(tail_size, 0, -1):
            xcor = self.segments[seg_num - 1].xcor()
            ycor = self.segments[seg_num - 1].ycor()
        
            self.segments[seg_num].goto(x=xcor, y=ycor)
        
        self.head.fd(20)

    def in_edge(self) -> bool:
        xcor = self.head.xcor()
        ycor = self.head.ycor()
        
        if xcor > 280 or xcor < -280 or ycor > 280 or ycor < -280:
            return True
        
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setpos(position)
        self.segments.append(new_segment)
           
    def extend(self):
        self.add_segment(self.segments[-1].pos())
        
    def touch_tail(self) -> bool:
        tail = self.segments[1:]
        for segment in tail:
            if segment.distance(self.head) < 5:
                return True
            
            
    def reset(self):
        for segment in self.segments:
            segment.setpos(1000, 1000)
            
        self.segments.clear()
        
        self.create_snake()
        
        self.head = self.segments[0]

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)