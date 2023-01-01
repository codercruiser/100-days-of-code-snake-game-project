from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake_skin()
        self.head = self.snake_body[0]

    def snake_skin(self):
        for turtle_index in range(0, 3):
            new_body = Turtle(shape='square')
            new_body.color('white')
            new_body.penup()
            new_body.goto(x=(turtle_index * -20), y=0)
            self.snake_body.append(new_body)



    def extend(self,):
        for turtle_index in range(0, 1):
            new_body = Turtle(shape='square')
            new_body.color('white')
            new_body.penup()
            new_body.goto(self.snake_body[-1].position())
            self.snake_body.append(new_body)


    def move(self):
        for body in range(len(self.snake_body) - 1, 0, -1, ):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x, new_y)
        return self.snake_body[0].forward(MOVE_DISTANCE)



    def Up(self):
        if self.head.heading() != DOWN:
            return self.head.setheading(90)
    def Down(self):
        if self.head.heading() != UP:
            return self.head.setheading(270)
    def Left(self):
        if self.head.heading() != RIGHT:
            return self.head.setheading(180)
    def Right(self):
        if self.head.heading() != LEFT:
            return self.head.setheading(0)


