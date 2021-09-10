import pygame, sys
from pygame.locals import *
import math
import time

#GLOBALES - CONSTANTES
ALTO = 500
ANCHO = 800

CELESTE = (135, 206, 235)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
CAFE = (145, 105, 81)
ROJO = (255, 0, 0)
AZUL = (30, 45, 110)

class Mapa():

    def __init__(self) -> None:
        pass
        
    def terreno(VENTANA):
        terreno2 = pygame.draw.rect(VENTANA, CAFE, (0, 400, 800, 100)) #(posX, posY, Largo, Alto) BASE
        #pointsT2 = [(0, 400), (40, 370), (95, 400), (144, 380), (250, 340), (390, 390),(410, 410)]
        #terreno2 = pygame.draw.polygon(VENTANA, CAFE, pointsT2, 70)
        #pointsT3 = [(500, 410), (530, 380), (540, 350), (560, 380), (590, 300), (615, 340),(645, 370),(680, 310), (700, 350), (800, 410) ]
        #terreno3 = pygame.draw.polygon(VENTANA, CAFE, pointsT3, 70)
        #rellenoT2 = pygame.draw.circle(VENTANA, CAFE, (530, 400), 51, 0) #Ciculo
        #rellenoT2_2 = pygame.draw.circle(VENTANA, CAFE, (650, 400), 70, 0) #Ciculo

class Tanques():

    def p1(VENTANA):
        p2_posNcolor = pygame.draw.circle(VENTANA, ROJO, (96, 353.5), 12, 0) #JUGADOR 1

    def p2(VENTANA):
        p2_posNcolor = pygame.draw.circle(VENTANA, AZUL, (680, 298), 12, 0) #JUGADOR 2      

class Proyectil():
    
    def __init__(self, v,g,t):
        self.v = v # angulo --> rad
        self.g = g #9.8
        self.t = t # inicial 0

    def der_trayectoria(v, g, t, angl): #trayectoria de izquierda a derecha
        x = v*(math.cos(angl))*t
        y_no = v*(math.sin(angl))*t-(g*t**2)/2
        y = 400 - y_no
        #print("angulo: ", angl)
        #print(x, y_no) #valores reales de ec. parabolica --> y_no
        return x, y

    def dibu_proyectil(x, y, VENTANA):
        proyectil = [pygame.draw.circle(VENTANA, NEGRO, (x, y), 2, 0)] #Ciculo

    def grad_a_rad(angulo):
        rad = 0.0
        rad = angulo*(3.1415/180) #0.01745
        #print("rad: ",rad)
        return rad

    #Colisiones proyectil
    def colision_terreno():
        m = 1


class InterfazJuego():

    def __init__(self) -> None:
        pass

    def valIniciales():
        v = float(input("Velocidad: "))
        angulo = float(input("Angulo (90>a>0): "))
        angulo = float(Proyectil.grad_a_rad(angulo))
        return v, angulo 

def Juego():
    
    #VENTANA
    pygame.init()
    VENTANA = pygame.display.set_mode((ANCHO, ALTO)) # (Horizontal, Vertical)
    pygame.display.set_caption("Scorched World")
    
    ''' Elementos Inciales '''

    #FONDO
    fondo = pygame.image.load("imagenes/fondo_2.png")
    VENTANA.blit(fondo, (0, 0))

    #TERRENO
    Mapa.terreno(VENTANA)

    ''' Fin elementos iniciales'''

    #TANQUES
    Tanques.p1(VENTANA)
    Tanques.p2(VENTANA)
    
    #INTERFAZ DE JUEGO
    #v, angl = InterfazJuego.valIniciales
    #print(v, angl)

    #PROYECTILES
    def proyectil(t, v, angl):
        
        tr_x, tr_y = Proyectil.der_trayectoria(v, 9.8, t, angl)
        Proyectil.dibu_proyectil(tr_x, tr_y, VENTANA)
        return tr_x, tr_y

    def check_colisiones(x, y):
        m=1
    
    turno = 1
    while turno != 0:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()  #Actualizacion ventana
        
        if turno == 1:
            velocidad = float(input("Velocidad: "))
            angulo = float(input("Angulo: "))
            angulo = Proyectil.grad_a_rad(angulo)
            turno += 1
            t = 0
        
        #t = pygame.time.get_ticks()/1000 #en segundos
        #t = t #5 veces mas rapido
        time.sleep(0.002)
        t = t+0.002*5 #velocidad *5
        proyectil(t, velocidad, angulo)
        
Juego()