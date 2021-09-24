import pygame, sys, math


def place_figure(png_name, rect_size, screen, where:tuple):
    chars = 'ABCDEFGH'
    c_x, c_y = where[1]-1, chars.index(where[0]) # defining x and y coordinates
    c_figure = pygame.image.load(f"./figures/{png_name}.png") # loading the corresponding image
    c_figure.convert()
    c_figure = pygame.transform.rotozoom(c_figure, 0, rect_size / c_figure.get_height()) # scaling the image to the right size 
    screen.blit(c_figure, (((rect_size/2) - c_figure.get_width() / 2)+ c_x*rect_size, c_y*rect_size))

if __name__ == "__main__":
    pass