import os
import pygame
from sys import exit

pygame.init()


screen_width = 512
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
font = pygame.font.Font("graphics/JockeyOne-Regular.ttf", 25)

background_surf = pygame.surface.Surface((512, 512))
header_text_surf = font.render("Space Invaders: A practice project", False, "White")
header_text_rect = header_text_surf.get_rect(center = (screen_width/2, 10))

player_surf = pygame.image.load("graphics/player.png").convert_alpha()
player_x_pos = 0
player_rect = player_surf.get_rect(midbottom=(player_x_pos, screen_height - 100))

monster_surf = pygame.image.load("graphics/green.png").convert_alpha()
monster_rect = monster_surf.get_rect(midbottom=(screen_width / 2, 100))

bullet_surf = pygame.Surface((10, 10))
bullet_surf.fill("Yellow")
bullet_rect = bullet_surf.get_rect(midbottom=player_rect.midtop)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.x -= 10
                bullet_rect.midbottom = player_rect.midtop
            if event.key == pygame.K_RIGHT:
                player_rect.x+= 10
                bullet_rect.midbottom = player_rect.midtop
                
                
    screen.blit(background_surf, (0, 0))
    screen.blit(header_text_surf, header_text_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(monster_surf, monster_rect)
    screen.blit(bullet_surf, bullet_rect)

    pygame.display.update()
    clock.tick(60)
