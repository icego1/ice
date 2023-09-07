import pygame
from random import randrange

RES = 1920
RES2 = 1080
SIZE = 10

#x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
x, y = RES / 2, RES2 / 2
apple = randrange(0, RES, SIZE), randrange(0, RES2, SIZE)
dirs = {'W': True, 'A': True, 'S': True, 'D': True, }
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 20

pygame.init()
sc = pygame.display.set_mode([RES, RES2])
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('gray'))
    [(pygame.draw.rect(sc, pygame.Color('black'), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('yellow'), (*apple, SIZE, SIZE))

    x += dx * SIZE
    y += dy * SIZE
    if x <= 1:
       x = 1
    #if y <= SIZE & y >= RES2:
    #    y = dy
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES2, SIZE)
        length += 10
        fps += 1
    #game over
    if x < 0 or x > RES - SIZE or y < 0 or y > RES2 - SIZE:
        break
    if len(snake) != len(set(snake)):
        break


    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'A': True, 'S': False, 'D': True, }
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0,  1
        dirs = {'W': False, 'A': True, 'S': True, 'D': True, }
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'A': True, 'S': True, 'D': False, }
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1,  0
        dirs = {'W': True, 'A': False, 'S': True, 'D': True, }
    if key[pygame.K_ESCAPE]:
        exit()
