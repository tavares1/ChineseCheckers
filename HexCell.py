import pygame


class HexCell:
    def __init__(self, x, y, radius, color, valid = True):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.valid = valid


    def get_position(self):
        return self.x, self.y

    def get_color(self):
        return self.color

    def get_validate(self):
        return self.valid

    def change_validation(self):
        self.valid = True if self.valid == True else False

    def create_circle(self, screen):
        return pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 10)

    def change_color(self):
        self.color = (0, 0, 255)
        return self.color

    def highlight(self):
        self.color = (255,255,0)
        return self.color

    def back_to_white(self):
        self.color = (255,255,255)
        return self.color

    def set_position(self, pos):
        self.x, self.y = pos

