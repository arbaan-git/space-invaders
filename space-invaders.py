from pathlib import Path
import pygame
from sys import exit

pygame.init()

# set paths
script_dir = Path(__file__).parent
assets_dir = script_dir/"assets"


screen_width = 512
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
font = pygame.font.Font(assets_dir /"JockeyOne-Regular.ttf", 25)

background_surf = pygame.surface.Surface((512, 512))
header_text_surf = font.render("Space Invaders: A practice project", False, "White")
header_text_rect = header_text_surf.get_rect(center = (screen_width/2, 10))

player_surf = pygame.image.load(assets_dir /"player.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(screen_width/2, screen_height - 100))

monster_surf = pygame.image.load(assets_dir / "green.png").convert_alpha()
monster_rect = monster_surf.get_rect(midbottom=(screen_width / 2, 100))
gravity = 5

bullet_surf = pygame.Surface((10, 10))
bullet_surf.fill("Yellow")
bullet_rect = bullet_surf.get_rect(midbottom=player_rect.midtop)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(background_surf, (0, 0))
    screen.blit(header_text_surf, header_text_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(monster_surf, monster_rect)
    screen.blit(bullet_surf, bullet_rect)

    # player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += 3
        bullet_rect.midbottom = player_rect.midtop
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= 3
        bullet_rect.midbottom = player_rect.midtop
        
    #monster gravity
    monster_rect.y += gravity
    if monster_rect.colliderect(player_rect):
        pygame.quit()
        exit()
        
    if monster_rect.y > screen_height:
        monster_rect.y = 100


    pygame.display.update()
    clock.tick(60)
