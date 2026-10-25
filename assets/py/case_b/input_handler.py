import pygame

def handle_input(keys, player):
    if keys[pygame.K_UP]:
        player.y -= player.speed
    if keys[pygame.K_DOWN]:
        player.y += player.speed
    if keys[pygame.K_LEFT]:
        player.x -= player.speed
    if keys[pygame.K_RIGHT]:
        player.x += player.speed
    # TODO: tambahkan W, A, S, D di sini
