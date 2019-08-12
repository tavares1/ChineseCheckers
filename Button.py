import pygame
import utils as u

class Button():
    def __init__(self, text, color, text_color):
        pygame.init()
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.SysFont("Candara",25)

    def draw_button(self, screen, x, y, width, height):
        rect = pygame.draw.rect(screen, self.color , (x,y,width,height))
        render_font = self.font.render(self.text, True, self.text_color)
        text_size_w, text_size_h = render_font.get_size()
        font_position_x = (x + width/2) - (text_size_w/2)
        font_position_y = (y + height/2) - (text_size_h/2)
        screen.blit(render_font, (font_position_x, font_position_y))
        pygame.display.flip()
        return rect
