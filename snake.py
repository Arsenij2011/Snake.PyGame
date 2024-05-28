from settings import *
class Snake:
    def __init__(self,pygame,screen):
        self.x = WIDHT // 2
        self.y = HEIGHT // 2
        self.length = 1
        self.snake_body = []
        self.pygame = pygame
        self.screen = screen
        self.turn = 0

    def move(self,vector):
        if vector == 'w':
            self.y -= 5
            self.turn = 3

        elif vector == 's':
            self.y +=5
            self.turn = 0

        elif vector == 'd':
            self.x -= 5
            self.turn = 1

        elif vector == 'a':
            self.x +=5       
            self.turn = 2

    def bord(self):
        if self.x < 0:
            self.x = WIDHT

        elif self.x > WIDHT:
            self.x = 0

        elif self.y < 0:
            self.y = HEIGHT

        elif self.y > HEIGHT:
            self.y = 0

    def snake(self):
        snake_head = [self.x, self.y]
        self.snake_body.append(snake_head)
        
        for x in self.snake_body:
            if self.snake_body.index(x) == 0 and self.length > 2:
                tail_snake_rect = tail_snake_img[self.turn].get_rect(x = x[0], y = x[1])
                self.screen.blit(tail_snake_img[self.turn], tail_snake_rect)
            elif x == self.snake_body[-1] or self.length == 1:
                head_snake_rect = head_snake_img[self.turn].get_rect(x = x[0], y = x[1])
                self.screen.blit(head_snake_img[self.turn], head_snake_rect)  
            else:
                body_snake_rect = body_snake_img.get_rect(x = x[0], y = x[1])
                self.screen.blit(body_snake_img, body_snake_rect)                
        
        if len(self.snake_body) > self.length:
            del self.snake_body[0]
        