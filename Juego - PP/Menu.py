import pygame, sys
import main
import main_2


Reloj = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Scorched World')
ventana= 0
g = 9.8
ALTO = 500
ANCHO = 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
 
FUENTE = pygame.font.SysFont(None, 35)
 
def Dibujar_texto(texto, fuente, color, superficie, x, y):
    textobj = fuente.render(texto, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    superficie.blit(textobj, textrect)

 
def Opciones():
    click = False
    correr = True
    while correr:
        VENTANA.fill((0,0,0))
        Boton_gravedad = pygame.Rect(0, 0, 50, 50) 
        Boton_pantalla = pygame.Rect(300, 150, 200, 50)
        Boton_municiones = pygame.Rect(300, 250, 200, 50)
        Boton_jug = pygame.Rect(300, 350, 200, 50)
        mx, my = pygame.mouse.get_pos()
        Dibujar_texto('Opciones', FUENTE, (255, 255, 255), VENTANA, 20, 20)
        Dibujar_texto('Pantalla', FUENTE, (255, 255, 255), VENTANA, 310, 160) 
        Dibujar_texto('Municiones', FUENTE, (255,255,255),VENTANA, 310, 260)
        Dibujar_texto('Jugadores', FUENTE, (255, 255, 255), VENTANA, 310, 360) 

        if Boton_pantalla.collidepoint((mx, my)):
            if click:
                ventana = pantalla()

        if Boton_municiones.collidepoint((mx, my)):
            if click:
                municiones()

        if Boton_jug.collidepoint((mx, my)):
            if click:
                jugadores()
                
        if Boton_gravedad.collidepoint((mx,my)):
            if click:
                g = gravedad()


        pygame.draw.rect(VENTANA, (255, 255,255), Boton_pantalla,1)
        pygame.draw.rect(VENTANA, (255, 255,255), Boton_municiones,1)
        pygame.draw.rect(VENTANA, (255, 255,255), Boton_jug,1)
        pygame.draw.rect(VENTANA, (255, 255,255), Boton_gravedad,1)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Menu_principal(ventana,0,0,0,0,g)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 
        
    
        pygame.display.update()
        Reloj.tick(60)
    return ventana ,g

def gravedad():
    g = 90
    print("90")
    return g

def pantalla():    
    correr = True
    click = False
    while correr:
        VENTANA.fill((0,0,0))
        tam_1 = pygame.Rect(450, 150, 200, 50)
        tam_2 = pygame.Rect(150, 150, 200, 50)
        mx, my = pygame.mouse.get_pos()
        Dibujar_texto('800x500', FUENTE, (255, 255, 255), VENTANA, 470, 160)
        Dibujar_texto('1600x900', FUENTE, (255, 255, 255), VENTANA, 170, 160) 

        pygame.draw.rect(VENTANA, (255, 255,255), tam_1,1)
        pygame.draw.rect(VENTANA, (255, 255,255), tam_2,1)
        if tam_1.collidepoint((mx, my)):
            if click:
                print("800x500")
                return 0 

        if tam_2.collidepoint((mx, my)):
            if click:
                print("1600x900")
                return 1

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   Opciones()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 
        pygame.display.update()
        Reloj.tick(60)

def municiones():  
    correr = True
    click = False
    while correr:
        VENTANA.fill((0,0,0))
        bala_1 = pygame.Rect(10, 150, 200, 50)
        bala_2 = pygame.Rect(300, 150, 200, 50)
        bala_3 = pygame.Rect(590, 150, 200, 50)
        mx, my = pygame.mouse.get_pos()


        Dibujar_texto('60mm', FUENTE, (255, 255, 255), VENTANA, 15, 100)
        Dibujar_texto('Proyectil perforante', FUENTE, (255, 255, 255), VENTANA, 305, 100) 
        Dibujar_texto('105mm', FUENTE, (255, 255, 255), VENTANA, 595, 100) 

        pygame.draw.rect(VENTANA, (255, 255,255), bala_1,1)
        pygame.draw.rect(VENTANA, (255, 255,255), bala_2,1)
        pygame.draw.rect(VENTANA, (255, 255,255), bala_3,1)


        if bala_1.collidepoint((mx, my)):
            if click:
                print("60mm")

        if bala_2.collidepoint((mx, my)):
            if click:
                print("Proyectil perforante")

        if bala_3.collidepoint((mx, my)):
            if click:
                print("105mm")

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   Opciones()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 
        pygame.display.update()
        Reloj.tick(60)

def jugadores():
    correr = True
    click = False
    while correr:
        VENTANA.fill((0,0,0))
        Dibujar_texto('PROXIMAMENTE', FUENTE, (255, 255, 255), VENTANA, 20, 20)
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   Opciones()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 
        pygame.display.update()
        Reloj.tick(60)

def Menu_principal(ventana , municion_1, municion_2, municion_3, jugadores, gravedad):
    g = gravedad
    print("GRavedad : ",gravedad)
    click = False
    while True:
        VENTANA.fill((0,0,0))
        Dibujar_texto('Jugar', FUENTE, (255, 255, 255), VENTANA, 360, 160) 
        Dibujar_texto('Opciones', FUENTE, (255,255,255),VENTANA, 345, 260)
        mx, my = pygame.mouse.get_pos()
 
        Boton_1 = pygame.Rect(300, 150, 200, 50)
        Boton_2 = pygame.Rect(300, 250, 200, 50)
        if Boton_1.collidepoint((mx, my)):
            if click:
                if ventana == 0:
                    main.Juego(g)

                if ventana == 1:
                    main_2.Juego(g)    

        if Boton_2.collidepoint((mx, my)):
            if click:
                Opciones()
                Menu_principal(ventana,0,0,0,0,g)
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


Menu_principal(ventana,0,0,0,0,g)
