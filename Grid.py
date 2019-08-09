import pygame
import utils as u
import numpy as np
from HexCell import HexCell


class Grid():
    def __init__(self):
        self.selectedsHex = []
        self.grid = np.array([
            # Ponta verde #
            [HexCell(250, 90, 10, u.GREEN)],
            [HexCell(240, 110, 10, u.GREEN), HexCell(260, 110, 10, u.GREEN)],
            [HexCell(230, 130, 10, u.GREEN), HexCell(250, 130, 10, u.GREEN), HexCell(270, 130, 10, u.GREEN)],
            [HexCell(220, 150, 10, u.GREEN), HexCell(240, 150, 10, u.GREEN), HexCell(260, 150, 10, u.GREEN),
             HexCell(280, 150, 10, u.GREEN)],
            # =========== #
            [HexCell(130, 170, 10, u.WHITE), HexCell(150, 170, 10, u.WHITE), HexCell(170, 170, 10, u.WHITE),
             HexCell(190, 170, 10, u.WHITE), HexCell(210, 170, 10, u.WHITE), HexCell(230, 170, 10, u.WHITE),
             HexCell(250, 170, 10, u.WHITE), HexCell(270, 170, 10, u.WHITE), HexCell(290, 170, 10, u.GREEN),
             HexCell(310, 170, 10, u.WHITE), HexCell(330, 170, 10, u.WHITE), HexCell(350, 170, 10, u.WHITE),
             HexCell(370, 170, 10, u.WHITE)],

            [HexCell(140, 190, 10, u.WHITE), HexCell(160, 190, 10, u.WHITE), HexCell(180, 190, 10, u.WHITE),
             HexCell(200, 190, 10, u.WHITE), HexCell(220, 190, 10, u.WHITE), HexCell(240, 190, 10, u.WHITE),
             HexCell(260, 190, 10, u.WHITE), HexCell(280, 190, 10, u.GREEN), HexCell(300, 190, 10, u.WHITE),
             HexCell(320, 190, 10, u.WHITE), HexCell(340, 190, 10, u.WHITE), HexCell(360, 190, 10, u.WHITE)],

            [HexCell(150, 210, 10, u.WHITE), HexCell(170, 210, 10, u.WHITE), HexCell(190, 210, 10, u.WHITE),
             HexCell(210, 210, 10, u.WHITE), HexCell(230, 210, 10, u.WHITE), HexCell(250, 210, 10, u.WHITE),
             HexCell(270, 210, 10, u.WHITE), HexCell(290, 210, 10, u.WHITE), HexCell(310, 210, 10, u.WHITE),
             HexCell(330, 210, 10, u.WHITE), HexCell(350, 210, 10, u.WHITE)],

            [HexCell(160, 230, 10, u.WHITE), HexCell(180, 230, 10, u.WHITE), HexCell(200, 230, 10, u.WHITE),
             HexCell(220, 230, 10, u.WHITE), HexCell(240, 230, 10, u.WHITE), HexCell(260, 230, 10, u.WHITE),
             HexCell(280, 230, 10, u.WHITE), HexCell(300, 230, 10, u.WHITE), HexCell(320, 230, 10, u.WHITE),
             HexCell(340, 230, 10, u.WHITE)],

            # = Meio da Estrela = #
            [HexCell(170, 250, 10, u.WHITE), HexCell(190, 250, 10, u.WHITE), HexCell(210, 250, 10, u.WHITE),
             HexCell(230, 250, 10, u.WHITE), HexCell(250, 250, 10, u.WHITE), HexCell(270, 250, 10, u.WHITE),
             HexCell(290, 250, 10, u.WHITE), HexCell(310, 250, 10, u.WHITE), HexCell(330, 250, 10, u.WHITE)],
            # =================== #
            [HexCell(160, 270, 10, u.WHITE),HexCell(180, 270, 10, u.WHITE),HexCell(200, 270, 10, u.WHITE)
            ,HexCell(220, 270, 10, u.WHITE),HexCell(240, 270, 10, u.WHITE),HexCell(260, 270, 10, u.WHITE)
            ,HexCell(280, 270, 10, u.WHITE),HexCell(300, 270, 10, u.WHITE),HexCell(320, 270, 10, u.WHITE)
            ,HexCell(340, 270, 10, u.WHITE)],

            [HexCell(150,290,10,u.WHITE),HexCell(170,290,10,u.WHITE),HexCell(190,290,10,u.WHITE),HexCell(210,290,10,u.WHITE)
            ,HexCell(230,290,10,u.WHITE),HexCell(250,290,10,u.WHITE),HexCell(270,290,10,u.WHITE),HexCell(290,290,10,u.WHITE)
            ,HexCell(310,290,10,u.WHITE),HexCell(330,290,10,u.WHITE),HexCell(350,290,10,u.WHITE)],

            [HexCell(140,310,10,u.WHITE),HexCell(160,310,10,u.WHITE),HexCell(180,310,10,u.WHITE),HexCell(200,310,10,u.WHITE)
            ,HexCell(220,310,10,u.WHITE),HexCell(240,310,10,u.WHITE),HexCell(260,310,10,u.WHITE),HexCell(280,310,10,u.WHITE)
            ,HexCell(300,310,10,u.WHITE),HexCell(320,310,10,u.WHITE),HexCell(340,310,10,u.WHITE),HexCell(360,310,10,u.WHITE)],

            [HexCell(130, 330, 10, u.WHITE),HexCell(150, 330, 10, u.WHITE),HexCell(170, 330, 10, u.WHITE),HexCell(190, 330, 10, u.WHITE)
            ,HexCell(210, 330, 10, u.WHITE),HexCell(230, 330, 10, u.WHITE),HexCell(250, 330, 10, u.WHITE),HexCell(270, 330, 10, u.WHITE),
             HexCell(290, 330, 10, u.WHITE),HexCell(310, 330, 10, u.WHITE),HexCell(330, 330, 10, u.WHITE),HexCell(350, 330, 10, u.WHITE),
             HexCell(370, 330, 10, u.WHITE)],
            # Parte vermelha da estrela
            [HexCell(220, 350, 10, u.RED),HexCell(240, 350, 10, u.RED),HexCell(260, 350, 10, u.RED),HexCell(280, 350, 10, u.RED)],
            [HexCell(230, 370, 10, u.RED),HexCell(250, 370, 10, u.RED),HexCell(270, 370, 10, u.RED)],
            [HexCell(240, 390, 10, u.RED), HexCell(260, 390, 10, u.RED)],
            [HexCell(250,410,10,u.RED)]
        ])

    def draw_grid(self, screen):
        for array in self.grid:
            for hexcell in array:
                hexcell.create_circle(screen)
        pygame.display.flip()

    def verify_inside_circle(self,x,y,a,b,r):
        return (x - a) * (x - a) + (y - b) * (y - b) < r*r

    def verify_position_in_matrix(self,x,y,event):
        for i, array in enumerate(self.grid):
            for j, hexcell in enumerate(array):
                (a,b) = hexcell.get_position()
                if self.verify_inside_circle(x, y, a, b, 10) and hexcell.valid:
                        return hexcell


    def get_neighborhood(self,hexcell):
        (x,y) = hexcell.get_position()
        print(x,y)

        right_hexted = self.get_hexcell_from_position(x+20,y)
        left_hexted = self.get_hexcell_from_position(x-20,y)
        top_left_hexted = self.get_hexcell_from_position(x - 10, y - 20)
        top_right_hexted = self.get_hexcell_from_position(x + 10, y - 20)
        bottom_left_hexted = self.get_hexcell_from_position(x - 10, y + 20)
        bottom_right_hexted = self.get_hexcell_from_position(x + 10, y + 20)

        return right_hexted,left_hexted,top_left_hexted,top_right_hexted,bottom_left_hexted,bottom_right_hexted

    def show_highlight(self,neighborhood):
        for hexted in neighborhood:
            if hexted != None and hexted.get_color() == u.WHITE:
                hexted.highlight()

    def remove_highlight(self, screen ):
        for array in self.grid:
            for hexcell in array:
                if hexcell.get_color() == (255,255,0):
                    hexcell.back_to_white()
                hexcell.create_circle(screen)
        pygame.display.flip()

    def get_hexcell_from_position(self, x , y):
        for i, array in enumerate(self.grid):
            for j, hexcell in enumerate(array):
                (a,b) = hexcell.get_position()
                if (a == x and b == y):
                    return hexcell

    def change_hexcell_position(self,hexcell, other_hexcell):
        pos = hexcell.get_position()
        hexcell.set_position(other_hexcell.get_position())
        other_hexcell.set_position(pos)
        print("aqui")

