import pygame
from Grid import Grid
from Button import Button
from ChatBox import ChatBox
from InputText import InputText
import utils as u
import random

hexcells = []
MOUSE_LEFT = 1
MOUSE_RIGHT = 3

# Inicializando o pygame, setando o tamanho da tela.
pygame.display.init()
window_size = (1200, 600)
screen = pygame.display.set_mode(window_size)

# Criando o grid( A estrela) e desenhando na tela.

screen.fill((220, 220, 220))
grid = Grid()
grid.draw_grid(screen)

# Inicilizando e desenhando o botão de passar a vez.

pass_turn_button = Button("Passar a vez", u.WHITE, u.BLUE)
pass_turn_button.draw_button(screen,150,450,200,50)

# Inicializando e desenhando o botão de desistir.

give_up_button = Button("Desistir", u.WHITE, u.RED)
give_up_button.draw_button(screen, 150, 525, 200, 50)

# Inicializando o ChatBox

chat_box = ChatBox(screen, 500,80, 600,350,u.WHITE)

# Inicilizando o input_text

input_text = InputText(screen, 500, 460, 400, 110, u.WHITE, "")

# Inicializando o botão de enviar mensagem no chat

send_mensage_button = Button("Enviar",u.WHITE, u.GREEN)

send_mensage_button_rect = send_mensage_button.draw_button(screen, 920, 490, 200, 50)

input_para_chatbox = ""

def enviar_mensagem(input):
    input_text.clean_input()
    pygame.display.flip()
    chat_box.add_text(0, input)
    chat_box.update_chat_array_ui()

# Recebendo toques e dinamica do jogo.

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_LEFT:
                if  input_text.get_input_text_rect().collidepoint(event.pos):
                    input_text.handle_event(event)
                if send_mensage_button_rect.collidepoint(event.pos):
                    enviar_mensagem(input_para_chatbox)
                else:
                    #Recebendo ponteiro do mouse
                    position_mouse = pygame.mouse.get_pos()
                    x = position_mouse[0]
                    y = position_mouse[1]

                    hexcell = grid.verify_position_in_matrix(x, y)
                    if hexcell != None:
                        if hexcell.get_color() != u.WHITE and len(hexcells) == 0:
                            hexcells.append(hexcell)
                        if hexcell.get_color() == u.WHITE and len(hexcells) > 0:
                            hexcells.append(hexcell)
                    print(hexcells)
                    if len(hexcells) == 2:
                        grid.change_hexcell_position(hexcells[0],hexcells[1])
                        hexcells = []
                    grid.draw_grid(screen)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_RIGHT:
                position_mouse = pygame.mouse.get_pos()
                x = position_mouse[0]
                y = position_mouse[1]
                hexcell = grid.verify_position_in_matrix(x, y)
                if hexcell != None:
                    if hexcell.get_color() != u.WHITE:
                        neighborhood = grid.get_neighborhood(hexcell, [], [])
                        grid.show_highlight(neighborhood)
                        grid.draw_grid(screen)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == MOUSE_RIGHT:
                grid.remove_highlight(screen)

        if event.type == pygame.KEYDOWN:

            input_text.handle_event(event)
            input_para_chatbox = input_text.draw(screen)
            pygame.display.flip()




