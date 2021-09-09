import pygame, sys

pygame.init()

# creating window
size = [600, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#koordinaten 

x = 300
y = 300
speed = 3
width = 40
height = 40

go = True

while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= speed
    if pressed[pygame.K_DOWN]:
        y += speed
    if pressed[pygame.K_RIGHT]:
        x += speed
    if pressed[pygame.K_LEFT]:
        x -= speed
    if x-width > size[0]:
        x = size[0]
    elif x < 0:
        x = 0
    if y-height > size[1]:
        y = size[1]
    elif y == 0:
        y = 0
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255),(x, y, width, height))
    pygame.display.update()
    #set fps
    clock.tick(60)