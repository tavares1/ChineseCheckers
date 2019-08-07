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

    def create_circle(self, screen):
        return pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 10)

    def change_color(self):
        self.color = (0, 0, 255)
        return self.color
