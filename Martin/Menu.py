import pygame, sys
import main

Reloj = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Scorched World')
VENTANA = pygame.display.set_mode((500, 500),0,32)
 
FUENTE = pygame.font.SysFont(None, 35)
 
def Dibujar_texto(texto, fuente, color, superficie, x, y):
    textobj = fuente.render(texto, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    superficie.blit(textobj, textrect)


def Menu_principal():
    click = False
    while True:
 
        VENTANA.fill((0,0,0))
        Dibujar_texto('Jugar', FUENTE, (255, 255, 255), VENTANA, 115, 110)
        Dibujar_texto('Opciones', FUENTE, (255,255,255),VENTANA, 90, 210)
        mx, my = pygame.mouse.get_pos()
 
        Boton_1 = pygame.Rect(50, 100, 200, 50)
        Boton_2 = pygame.Rect(50, 200, 200, 50)
        if Boton_1.collidepoint((mx, my)):
            if click:
                main.Juego()

        if Boton_2.collidepoint((mx, my)):
            if click:
                Opciones()
        pygame.draw.rect(VENTANA, (255, 255,255), Boton_1,1)
        pygame.draw.rect(VENTANA, (255, 255, 255), Boton_2,1)
 
        click = False
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
                if evento.button == 1:
                    click = True
 
        pygame.display.update()
        Reloj.tick(60)
 
def Opciones():
    correr = True
    while correr:
        VENTANA.fill((0,0,0))
 
        Dibujar_texto('Opciones', FUENTE, (255, 255, 255), VENTANA, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    correr = False
        
        pygame.display.update()
        Reloj.tick(60)
 
Menu_principal()
