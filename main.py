import pygame,random


screen = pygame.display.set_mode([700, 700])
a = 1


def kryg(rastoyanie, r,color):
    if rastoyanie>r-rastoyanie or rastoyanie<=0:
        pygame.draw.circle(screen, [0,0,255], [350, 350], r)
    else:
        pygame.draw.circle(screen, color, [350, 350], r, 5)
    if r > 0 and rastoyanie > 0:
        color[0]-=4
        color[1]-=5
        color[2]-=5
        kryg(rastoyanie - 1, r - rastoyanie,color)

pygame.key.set_repeat(100)
while True:
    event = pygame.event.get()
    screen.fill([0,0,0])
    kryg(a, 340,[148,165,170])
    for u in event:
        if u.type == pygame.KEYDOWN and u.key == pygame.K_UP:
            a+=1
        elif u.type == pygame.KEYDOWN and u.key == pygame.K_DOWN:
            a-=1
    pygame.display.flip()
