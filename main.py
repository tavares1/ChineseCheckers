import pygame
from Grid import Grid

pygame.display.init()
window_size = (1200, 600)
screen = pygame.display.set_mode(window_size)
screen.fill((0, 0, 0))
grid = Grid()
grid.draw_grid(screen)
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            position_mouse = pygame.mouse.get_pos()
            x = position_mouse[0]
            y = position_mouse[1]
            grid.verify_position_in_matrix(x, y, screen)
