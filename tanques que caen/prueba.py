import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

CAFE = (145, 105, 81)

screen = pygame.display.set_mode((800,500))

tanquesin = pygame.image.load("imagenes/tanquesin_1.png")
tanquesin_rect = tanquesin.get_rect(topleft = [50,200])

tanquesin_2 = pygame.image.load("imagenes/tanquesin_2.png")
tanquesin_rect2 = tanquesin_2.get_rect(topleft = [700,200])

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    screen.fill((0,133,138))
    terreno2 = pygame.draw.rect(screen, CAFE, (0, 400, 800, 100)) #(posX, posY, Largo, Alto) BASE
    
    screen.blit(tanquesin, tanquesin_rect)
    screen.blit(tanquesin_2, tanquesin_rect2)
    
    if(tanquesin_rect2.bottom <= 399): #Colision
        tanquesin_rect2.bottom += 3

    if(tanquesin_rect.bottom <= 399): #Colision
        tanquesin_rect.bottom += 5
    
    pygame.display.update()
    clock.tick(60)