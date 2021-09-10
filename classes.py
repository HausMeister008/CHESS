import pygame, sys, math


class Figure:
    def __init__(self, name:str,image_name:str, position:tuple, screen, rect_size):
        self.name = name
        self.image_name = image_name
        self.position = position
        self.screen = screen
        self.rect_size = rect_size
        self.chars = 'ABCDEFGH'
        self.image = pygame.image.load(f"./figures/{self.image_name}.png") # loading the corresponding image
        self.image.convert()
        self.image = pygame.transform.rotozoom(self.image, 0, self.rect_size / self.image.get_height()) # scaling the image to the right size 
        self.c_x, self.c_y = self.position[1]-1, self.chars.index(self.position[0]) # defining x and y coordinates

    def place_figure(self):
        self.screen.blit(self.image, (((self.rect_size/2) - self.image.get_width() / 2)+ self.c_x*self.rect_size, self.c_y*self.rect_size))

    def move_figure(self, position):
        old_position = self.position
        self.position = position
        self.c_x, self.c_y = self.position[1]-1, self.chars.index(self.position[0]) # defining x and y coordinates
        self.place_figure()
        #deleting old image here


        
class Farmer(Figure):
    def __init__(self):
        pass