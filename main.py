import pygame
from Grid import Grid
from Button import Button
from ChatBox import ChatBox
from InputText import InputText
import utils as u
import random


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

input_text = InputText(screen, 500, 460, 400, 110, u.WHITE)

# Inicializando o botão de enviar mensagem no chat

send_mensage_button = Button("Enviar",u.WHITE, u.GREEN)

send_mensage_button.draw_button(screen, 920, 490, 200, 50)

# Recebendo toques e dinamica do jogo.

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:

            position_mouse = pygame.mouse.get_pos()
            print(position_mouse)
            x = position_mouse[0]
            y = position_mouse[1]
            grid.verify_position_in_matrix(x, y, screen)
        if event.type == pygame.KEYDOWN:
            random_number = random.randint(0,1)
            chat_box.add_text(random_number,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            print(len(chat_box.get_all_texts()))
            chat_box.update_chat_array_ui()


