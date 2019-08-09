import pygame
import utils as u

pygame.init()
COLOR_INACTIVE = pygame.Color("gray")
COLOR_ACTIVE = pygame.Color("white")
FONT = pygame.font.SysFont("Corbel", 15)
FONT2 = pygame.font.SysFont("Corbel", 15)

class InputText:

    def __init__(self,screen, x, y, width, height, color, text):
        self.screen = screen
        self.user_input = []
        self.active = False
        self.rect = pygame.draw.rect(screen, COLOR_INACTIVE, (x,y, width,height))
        self.text = text
        self.surface_text = FONT.render(text, True, u.BLACK)
        self.quantity_of_number = FONT2.render('0/60', True, u.BLACK)
        self.screen.blit(self.quantity_of_number, (850, 540))
        self.color = color
        pygame.display.flip()

    def get_input_text_rect(self):
        return self.rect

    def get_use_input(self,player,text):
        self.user_input((player,text))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            self.draw(self.screen)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = " "
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 60:
                        self.text += event.unicode
                self.surface_text = FONT.render(self.text, True, u.BLACK)
                self.quantity_of_number = FONT2.render(f"{len(self.text)}/60", True, u.BLACK)

    def draw(self, screen):
        pygame.draw.rect(screen,self.color,self.rect)
        pygame.draw.rect(screen, self.color, (500, 460, 400, 30))
        self.screen.blit(self.surface_text, (500, 460))
        if len(self.text) < 60:
            pygame.draw.rect(screen, self.color, (850, 540, 50, 30))
        else:
            pygame.draw.rect(screen, u.RED, (850, 540, 50, 30))
        self.screen.blit(self.quantity_of_number, (850, 540))
        pygame.display.flip()
        return self.text

    def clean_input(self):
        self.text = ""
        self.surface_text = FONT.render(self.text, True, u.BLACK)
        self.quantity_of_number = FONT2.render(f"{len(self.text)}/60", True, u.BLACK)
        self.color = COLOR_INACTIVE
        self.draw(self.screen)
        print(self.text)
        pygame.display.flip()