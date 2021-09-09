import pygame, sys, math

pygame.init()

# creating window
rect_size = 100
chars_space_size = math.ceil(int(rect_size * 0.5))
print(chars_space_size)
size = [rect_size*8 + chars_space_size, rect_size*8 +  chars_space_size]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

screen.fill((0,0,0))

chars = 'ABCDEFGH'
board_data = {(char, number+1): {'manned': False, 'figure': ''} for char in chars for number in range(8)}
# board_data[('A', 2)] --> {'manned': True, 'figure': 'horse1_black'}

for i in range(8):
    for j in range(4):
        pygame.draw.rect(
            screen, #draw on the screen
            (255,255,255), #color
            ((j*2+(i%2))*rect_size , #where to draw it horizontally
            i*rect_size, # where to draw it vertically
            rect_size, # which size
            rect_size
        ))
    pygame.draw.rect(
        screen, #draw on the screen
        (100,100,100), #color
        (8*rect_size, # where to draw it horizontally
        i*rect_size, # where to draw it horizontally, # where to draw it vertically
        chars_space_size, # which size
        rect_size)
    )
    pygame.draw.rect(
        screen, #draw on the screen
        (100,100,100), #color
        (i*rect_size, # where to draw it horizontally
        8*rect_size, # where to draw it horizontally, # where to draw it vertically
        # which size
        rect_size,
        chars_space_size)
    )
pygame.draw.rect(
    
)
go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    #set fps
    clock.tick(60)