from pathlib import Path
import pygame
from sys import exit

pygame.init()

# set paths
script_dir = Path(__file__).parent
assets_dir = script_dir / "assets"

# screen + logic setup
screen_width = 512
screen_height = 512
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
font = pygame.font.Font(assets_dir / "JockeyOne-Regular.ttf", 25)
game_active = True
player_speed = 5
gravity = 2

# background + text init
background_surf = pygame.surface.Surface((512, 512))
header_text_surf = font.render("Space Invaders: A practice project", False, "White")
header_text_rect = header_text_surf.get_rect(midtop=(screen_width / 2, 10))
gameover_text_surf = font.render("gameover, press space to restart", False, "White")
gameover_text_rect = gameover_text_surf.get_rect(center=(screen_width / 2, 50))

# player init
player_surf = pygame.image.load(assets_dir / "player.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(screen_width / 2, screen_height - 100))

# monster init
monster_surf = pygame.image.load(assets_dir / "green.png").convert_alpha()
monster_x_position = 30
monster_rects = []
for x_position in [30, screen_width / 2, screen_width - 30]:
    monster_rect = monster_surf.get_rect(midbottom=(x_position, 100))
    monster_rects.append(monster_rect)

# bullet init
bullet_surf = pygame.surface.Surface((10, 10))
bullet_surf.fill("Yellow")
bullet_rects = []
countdown = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        screen.blit(background_surf, (0, 0))
        screen.blit(header_text_surf, header_text_rect)
        screen.blit(player_surf, player_rect)

        keys = pygame.key.get_pressed()

        # player
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_rect.x += player_speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_rect.x -= player_speed

        # monster
        for monster_rect in monster_rects:
            screen.blit(monster_surf, monster_rect)
            monster_rect.y += gravity

            if monster_rect.colliderect(player_rect) or monster_rect.bottom >= 512:
                game_active = False

        # bullet
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            bullet = bullet_surf.get_rect(midbottom=player_rect.midtop)
            bullet_rects.append(bullet)
        for bullet_rect in bullet_rects:
            if countdown <= 0:
                screen.blit(bullet_surf, bullet_rect)
                countdown = 10
            bullet_rect.y -= 10
            countdown -= 1

    else:
        screen.blit(gameover_text_surf, gameover_text_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            for monster_rect in monster_rects:
                monster_rect.y = 100
            game_active = True

    pygame.display.update()
    clock.tick(60)
