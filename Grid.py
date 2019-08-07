import pygame
import time
import utils as u
import numpy as np
from HexCell import HexCell


class Grid():
    def __init__(self):
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
             HexCell(250, 170, 10, u.WHITE), HexCell(270, 170, 10, u.WHITE), HexCell(290, 170, 10, u.WHITE),
             HexCell(310, 170, 10, u.WHITE), HexCell(330, 170, 10, u.WHITE), HexCell(350, 170, 10, u.WHITE),
             HexCell(370, 170, 10, u.WHITE)],

            [HexCell(140, 190, 10, u.WHITE), HexCell(160, 190, 10, u.WHITE), HexCell(180, 190, 10, u.WHITE),
             HexCell(200, 190, 10, u.WHITE), HexCell(220, 190, 10, u.WHITE), HexCell(240, 190, 10, u.WHITE),
             HexCell(260, 190, 10, u.WHITE), HexCell(280, 190, 10, u.WHITE), HexCell(300, 190, 10, u.WHITE),
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

    def verify_position_in_matrix(self,x,y,screen):
        for array in self.grid:
            for hexcell in array:
                (a,b) = hexcell.get_position()
                if self.verify_inside_circle(x, y, a, b, 10) and hexcell.valid:
                    hexcell.change_color()
                    self.draw_grid(screen)

#     # drawing grid
#     # Bola do meio
#     pygame.draw.circle(screen, u.WHITE, (250, 250), 10)
#
#     # Bola do topo
#     pygame.draw.circle(screen, u.GREEN, (250,90), 10)
#     # A ponta verde da estrela.
#     for i in range(240, 280, 20):
#         pygame.draw.circle(screen, u.GREEN, (i,110),10)
#
#     for i in range(230, 290, 20):
#         pygame.draw.circle(screen, u.GREEN, (i, 130), 10)
#
#     for i in range(220, 300, 20):
#         pygame.draw.circle(screen, u.GREEN, (i, 150), 10)
#     # Meio até a parte verde
#     for i in range(130, 390, 20):
#         pygame.draw.circle(screen, u.WHITE, (i, 170), 10)
#
#     for i in range(140, 380, 20):
#         pygame.draw.circle(screen, u.WHITE, (i, 190), 10)
#
#     for i in range(150, 370, 20):
#         pygame.draw.circle(screen, u.WHITE, (i, 210), 10)
#
#     for i in range(160, 360, 20):
#         pygame.draw.circle(screen, u.WHITE, (i, 230), 10)
#
#     # Meio do tabuleiro
#     for i in range(170, 350, 20):
#         pygame.draw.circle(screen, u.WHITE, (i, 250), 10)
#     # Meio até a parte vermelha da estrela.
#     for i in range(160, 360, 20):
#         pygame.draw.circle(screen, u.WHITE, (i, 270), 10)
#
#     for i in range(150, 370, 20):
#         pygame.draw.circle(screen, u.WHITE, (i, 290), 10)
#
#     for i in range(140, 380, 20):
#         pygame.draw.circle(screen, u.WHITE, (i, 310), 10)
#
#     for i in range(130, 390, 20):
#         pygame.draw.circle(screen, u.WHITE, (i, 330), 10)
# #   Ponta vermelha da estrela
#     for i in range(220, 300, 20):
#         pygame.draw.circle(screen, u.RED, (i, 350), 10)
#
#     for i in range(230, 290, 20):
#         pygame.draw.circle(screen, u.RED, (i, 370), 10)
#
#     for i in range(240, 280, 20):
#         pygame.draw.circle(screen, u.RED, (i, 390), 10)
#
# # Ponta da estrela vermelha
#     pygame.draw.circle(screen, u.RED, (250, 410), 10)
