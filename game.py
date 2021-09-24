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


chars = 'ABCDEFGH'
board_data = {(char, number+1): {'manned': False, 'figure': ''} for char in chars for number in range(8)}
# board_data[('A', 2)] --> {'manned': True, 'figure': 'horse1_black'}
def draw_board():
    screen.fill((41,35,0))
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
draw_board()
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
        position = ('A' if player == 1 else 'H', field+1)
        players[name] = Figure(name, image_name,position, screen, rect_size)

    for field in range(8,16): # placing farmers in second row
        #placing of the farmers
        position = list(board_data.keys())[field] if player == 1 else list(board_data.keys())[-(field+1)]
        name = 'farmer_' + str(8-field%8) + ('_black' if player == 1 else '_white')
        image_name = 'farmer' + ('_black' if player == 1 else '')
        players[name] = Farmer(name,image_name, position, screen, rect_size)


# players = {'famer_1_white': oject} -> object hat attribute (zb postion)
def draw_figures():
    for name, object_ in players.items():
        object_.place_figure()
draw_figures()
def draw():
    draw_board()
    draw_figures()
go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 2 -> middle click; 3 -> right click; 4 -> scroll up; 5 -> scroll down
            x_pos, y_pos = (int(math.trunc(x/rect_size)) for x in pygame.mouse.get_pos()) # rounding down to get the field we are on
            #print(x_pos+1, chars[y_pos])
            name = ''
            for player in players.values():
                if player.position == (chars[y_pos], x_pos+1):
                    name = player.name
                    p = players[name]
                    p.move_figure((p.c_x, p.c_y + (-1 if 'white' in name else + 1)))
                    draw()
                    break
            print(name)
        if event.type == pygame.QUIT:
            sys.exit()
    pressed = pygame.key.get_pressed()
    pygame.display.update()
    clock.tick(20)