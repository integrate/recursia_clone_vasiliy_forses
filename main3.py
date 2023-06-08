import pygame

screen=pygame.display.set_mode([700,700])
def loza(a,b,c,d):
    pygame.draw.line(screen,[0,255,0],[a,b],[c,d],5)
while True:
    event = pygame.event.get()
    screen.fill([0, 0, 0])
    loza(0,350,700,350)
    pygame.display.flip()