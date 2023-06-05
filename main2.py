import pygame, random

screen = pygame.display.set_mode([700, 700])
x = 350
y = 350
c = [88, 51, 202]


def romb(x, y, shag, shag2, shagshag,c):
    pygame.draw.line(screen, c, [x, y], [x - shag, y - shag2], 5)
    x -= shag
    y -= shag2
    pygame.draw.line(screen, c, [x, y], [x + shag, y - shag2], 5)
    x += shag
    y -= shag2
    pygame.draw.line(screen, c, [x, y], [x + shag, y + shag2], 5)
    x += shag
    y += shag2
    shag -= shagshag
    shag2 -= shagshag
    pygame.draw.line(screen, c, [x, y], [x - shag - shagshag, y + shag2], 5)
    x -= shag + shagshag
    y += shag2

    if c[0]>=10:
        c[0]-=10
    if c[1]>=10:
        c[1]-=10
    if c[2]>=10:
        c[2]-=10

    pygame.draw.circle(screen, [88, 51, 202], [0, 0], 4)
    pygame.image.save(screen, '1.jpg')
    if shag > 0 and shag2 > 0:
        romb(x, y, shag, shag2, shagshag,c)


pygame.key.set_repeat(30)
while True:
    event = pygame.event.get()
    screen.fill([0, 0, 0])
    for b in event:
        if b.type == pygame.KEYDOWN and b.key == pygame.K_UP:
            y += 1

        elif b.type == pygame.KEYDOWN and b.key == pygame.K_DOWN:
            y -= 1
        if b.type == pygame.KEYDOWN and b.key == pygame.K_LEFT:
            x += 1

        elif b.type == pygame.KEYDOWN and b.key == pygame.K_RIGHT:
            x -= 1
        if b.type == pygame.KEYDOWN and b.key == pygame.K_SPACE:
            c=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

    romb(350, 350 + y, x, y, 20,c)
    pygame.display.flip()
