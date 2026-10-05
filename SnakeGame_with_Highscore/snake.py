from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-30, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_block(position)

    def add_block(self, position):
        snake_block = Turtle(shape="square")
        snake_block.color("white")
        snake_block.penup()
        snake_block.goto(position)
        self.blocks.append(snake_block)

    def extend_block(self):
        self.add_block(self.blocks[-1].position())

    def move(self):
        for block_num in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[block_num - 1].xcor()
            new_y = self.blocks[block_num - 1].ycor()
            self.blocks[block_num].goto(new_x, new_y)
        self.blocks[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def restart_game(self):
        for block in self.blocks:
            block.goto(1000,1000)
        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]
