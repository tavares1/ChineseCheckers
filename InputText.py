import pygame

class InputText:
    def __init__(self,screen, x, y, width, height, color):
        pygame.draw.rect(screen, color, (x,y, width,height))
        pygame.display.flip()