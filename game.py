import pygame, sys, math, time
from methods import *
from classes import *
pygame.init()

# creating window
rect_size = 100
chars_space_size = math.ceil(int(rect_size * 0.5))
size = [rect_size*8 + chars_space_size, rect_size*8 +  chars_space_size]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

side_color = (80,70,10)
font_size = 50
myfont = pygame.font.SysFont("Calibri", font_size)

screen.fill((41,35,0))

chars = 'ABCDEFGH'
board_data = {(char, number+1): {'manned': False, 'figure': ''} for char in chars for number in range(8)}
# board_data[('A', 2)] --> {'manned': True, 'figure': 'horse1_black'}

for i in range(8): #i -> y Koordinate
    for j in range(4):
        pygame.draw.rect(
            screen, #draw on the screen
            (255,255,255), #color
            ((j*2+(i%2))*rect_size , #where to draw it horizontally
            i*rect_size, # where to draw it vertically
            rect_size, # which size
            rect_size
        ))
    pygame.draw.rect(screen, side_color, (i*rect_size, 8*rect_size, rect_size,chars_space_size))
    pygame.draw.rect(screen, side_color, (8*rect_size, i*rect_size,chars_space_size, rect_size))
    number = myfont.render(str(i+1), 1, 'white')
    char = myfont.render(chars[i], 1, 'white')
    screen.blit(number,(i*rect_size + (rect_size-font_size-10), 8*rect_size))
    screen.blit(char,(8*rect_size + 10, i*rect_size + (chars_space_size-20)))

pygame.draw.rect(screen, side_color, (8*rect_size, 8*rect_size,chars_space_size, chars_space_size))

first_row_figures = {'tower':[0,7], 'horse':[1,6], 'runner':[2,5], 'lady':[4], 'king':[3]}
# loop for both players

players = {}
for player in range(1,3):
    #placing first row items
    for field in range(8):
        x = [(key if field in value else '') for key, value in first_row_figures.items()] # zb ['','','','tower', '']
        x.sort() # ['','',''..., 'tower']
        figure = x[-1]
        color = ('_black' if player == 1 else '_white')
        name = figure + ("_2" if (figure+'_1' + color) in list(players.keys()) else '_1') + color
        image_name = figure + ('_black' if player == 1 else '')
        place = ('A' if player == 1 else 'H', field+1)
        players[name] = Figure(name, image_name,place, screen, rect_size)

    #mathematical impovements needed ?!
    for field in range(8,16): # placing farmers in second row
        #placing of the farmers
        place = list(board_data.keys())[field] if player == 1 else list(board_data.keys())[-(field+1)]
        name = 'farmer_' + str(8-field%8) + ('_black' if player == 1 else '_white')
        image_name = 'farmer' + ('_black' if player == 1 else '')
        players[name] = Figure(name,image_name, place, screen, rect_size)



for name, object_ in players.items():
    print(name)
    object_.place_figure()
go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_UP]:
    #     players['farmer_1_white'].move_figure((players['farmer_1_white'].chars[players['farmer_1_white'].chars.index(players['farmer_1_white'].position[0])-1], 1))
    pygame.display.update()
    clock.tick(30)