import pygame, sys, math

chars = 'ABCDEFGH'
def convert_positions( position:tuple):
    a_y, a_x = position
    n_x = a_x -1
    n_y = chars.index(a_y)  
    return (n_x, n_y)

def convert_coordinates( position:tuple):
    # converting the coordinates (0-7, 0-7) to readable postions (A-H, 1-8)
    x, y = position
    x += 1
    y = chars[y]
    return (y,x)

class Figure:
    def __init__(self, name:str,image_name:str, position:tuple, screen, rect_size): #position -> Buchstabe/Zahl
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

    def move_figure(self, f_position): #future position, erst x, dann y
        old_position = self.position
        self.c_x, self.c_y = f_position[0], f_position[1] # defining x and y coordinates
        self.position = (self.chars[f_position[1]],f_position[0]+1) #erst y, dann x (x in richtigen Zahlen deswegen +1)
        #self.place_figure()
        #deleting old image here
        


        
class Farmer(Figure):
    def __init__(self, name: str, image_name: str, position: tuple, screen, rect_size):
        super().__init__(name, image_name, position, screen, rect_size)
    def calc_possible_postitions(self, board_data):
        b_d = {convert_positions(c):values for c, values in board_data.items()}
        print(b_d)
        look_here_y = self.c_y + (1 if 'black' in self.name else -1)
        if look_here_y > 0 and look_here_y < 8:
            look_here_x = [(self.c_x + x if self.c_x + x < 8 and self.c_x + x >= 0 else '' ) for x in range(-1,2)]
            while '' in look_here_x:
                look_here_x.remove('')
            
            for x in look_here_x:
                if b_d[(x, look_here_y)]['manned']:
                    if 'white' in self.name and 'black' in b_d[(x, look_here_y)]['figure'] or 'black' in self.name and 'white' in b_d[(x, look_here_y)]['figure']:
                        pass
                    else:
                        pass

        else:
            return (self.c_x, self.c_y)
        