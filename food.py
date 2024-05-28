import random
from settings import WIDHT, HEIGHT


class Food():
    def __init__(self):
        self.x = random.randrange(10, WIDHT - 10, 1)
        self.y = random.randrange(10, HEIGHT - 10, 1)

