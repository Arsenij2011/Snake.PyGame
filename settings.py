import pygame
pygame.init()
eat = pygame.mixer.Sound("sounds/eat.mp3")
bg = pygame.mixer.Sound("sounds/bg.mp3")
gameover = pygame.mixer.Sound("sounds/gameover.mp3")

HEIGHT = 600
WIDHT = 800
FPS = 40

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
vector = None
SIZE = 20
food_img = pygame.transform.scale(pygame.image.load('img/food.png'),(SIZE, SIZE))
body_snake_img = pygame.transform.scale(pygame.image.load('img/body.png'),(SIZE, SIZE))
head_snake_img = [
    pygame.transform.scale(pygame.image.load('img/HeadB.png'),(SIZE, SIZE)),
    pygame.transform.scale(pygame.image.load('img/HeadL.png'),(SIZE, SIZE)),
    pygame.transform.scale(pygame.image.load('img/HeadR.png'),(SIZE, SIZE)),
    pygame.transform.scale(pygame.image.load('img/HeadT.png'),(SIZE, SIZE))
]

tail_snake_img = [
    pygame.transform.scale(pygame.image.load('img/TailD.png'),(SIZE, SIZE)),
    pygame.transform.scale(pygame.image.load('img/TailL.png'),(SIZE, SIZE)),
    pygame.transform.scale(pygame.image.load('img/TailR.png'),(SIZE, SIZE)),
    pygame.transform.scale(pygame.image.load('img/TailU.png'),(SIZE, SIZE))
]
