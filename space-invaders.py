import os
import pygame
from sys import exit

os.chdir("D:/coding/pygame/space-invaders")
pygame.init()


screen_width = 512
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
font = pygame.font.Font("graphics/JockeyOne-Regular.ttf", 25)

background_surface = pygame.image.load("graphics/background.png").convert_alpha()
header_text_surface = font.render("Space Invaders: A practice project", False, "White")

player_surface = pygame.image.load("graphics/player.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (screen_width/2, screen_height - 100))
player_x_position = 0

monster_surface = pygame.image.load('graphics/green.png').convert_alpha()
monster_rect = monster_surface.get_rect(midbottom = (screen_width/2, 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0, 0))
    screen.blit(header_text_surface, (10, 10))
    screen.blit(player_surface, player_rect)
    screen.blit(monster_surface, monster_rect)

    pygame.display.update()
    clock.tick(60)
