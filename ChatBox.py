import pygame
import utils as u

class ChatBox:
    chat = []

    def __init__(self,screen, x, y, width, height, color):
        self.screen = screen
        self.width = width
        self.rect = pygame.draw.rect(screen, color, (x,y, width,height))
        pygame.display.flip()
        self.font = pygame.font.SysFont("Corbel", 15)

    def update_chat_array_ui(self):

        for index,value in enumerate(self.chat):
            player,text = value
            if player == "RED":
                # text vem do array e o color tbm.
                text = (f"Jogador Vermelho: {text}")
                render_font = self.font.render(text, True, u.RED)
                pygame.draw.rect(self.screen,u.WHITE,(500,90 + (30*index),self.width,30))
                self.screen.blit(render_font, (510,90 + (30*index)))
                pygame.display.flip()
            else:
                # text vem do array e o color tbm.
                text = (f"Jogador Verde: {text}")
                render_font = self.font.render(text, True, u.GREEN)
                pygame.draw.rect(self.screen,u.WHITE,(500,90 + (30*index),self.width,30))
                self.screen.blit(render_font, (510, 90 + (30*index)))
                pygame.display.flip()
