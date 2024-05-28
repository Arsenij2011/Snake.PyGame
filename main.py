import pygame as x
from menu import menu
from settings import *
from snake import Snake
from food import Food
import random 
from reset import reset


x.init()
screen = x.display.set_mode((WIDHT, HEIGHT))
x.display.set_caption('ЗМЕЙКА')
clock = x.time.Clock()
s = Snake(x,screen)
ex_f = Food()

menu.main_menu().mainloop(screen)

bg.play(loops = 1)
bg.set_volume(0.3)

def draw():
    screen.fill(WHITE)
    f = food_img.get_rect(x = ex_f.x,y = ex_f.y)
    screen.blit(food_img,f)
    if f.x + SIZE > s.x > f.x - SIZE and f.y + SIZE > s.y > f.y - SIZE:
        ex_f.y = random.randrange(10, HEIGHT - 10, 5)
        ex_f.x = random.randrange(10, WIDHT - 10, 5)
        s.length += 1
        eat.play()

    s.bord()
    s.move(vector)
    s.snake()
    font_style = x.font.SysFont('Arial', size = 25)
    massage = font_style.render(f'Очки: {s.length - 1}', True, RED)
    screen.blit(massage, [10, 10])


    for i in s.snake_body[:-1]:
        if i == [s.x, s.y]:
            bg.stop()
            gameover.play()
            s.length = reset(screen)
            bg.play()

    x.display.update()

while True:
    draw()
    
    for event in x.event.get():
        if event.type == x.QUIT:
            quit()
        if event.type == x.KEYDOWN:
            if event.key == x.K_UP:
                if vector != 's' or s.length == 1:
                    vector = 'w'
            elif event.key == x.K_DOWN :
                if vector != 'w'or s.length == 1:
                    vector = 's' 
            elif event.key == x.K_RIGHT :
                if vector != 'd'or s.length == 1:
                    vector = 'a' 
            elif event.key == x.K_LEFT :
                if vector != 'a'or s.length == 1:
                    vector = 'd' 
            elif event.key == x.K_m:
                menu.main_menu().mainloop(screen)
    clock.tick(FPS)

