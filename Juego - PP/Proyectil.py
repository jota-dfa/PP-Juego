import pygame
import math

NEGRO = (0, 0, 0)

class Proyectil():
    
    def __init__(self, v,g,t,posXTanque, posYTanque):
        self.v = v # velocidad inicial
        self.g = g #9.8
        self.t = t # inicial 0
        self.posXTanque = posXTanque
        self.posYTanque = posYTanque

    '''Trayectoria de tiro Parabolico'''

    # v = velocidad // g = c. gravedad // t = tiempo // angl = angulo(rad) #
    # (x,y) = valores en ventana // (x, y_real) = valores reales de la ec.trayectoria #
    
    def pr_trayectoria(v, g, t, angl, posXTanque, posYTanque): 
        x = posXTanque+v*(math.cos(angl))*t # posTanque+v*(math.cos(angl))*t , posTanque =  posicion tanque 
        y_real = v*(math.sin(angl))*t-(g*t**2)/2
        y = posYTanque - y_real
        #print(x, y_real) #valores reales de ec. parabolica --> y_real
        return x, y
    
    '''Dibuja Proyectil'''
    def dibu_proyectil(x, y, VENTANA):
        proyectil = [pygame.draw.circle(VENTANA, NEGRO, (x, y), 2, 0)] #Ciculo

    '''Angulo --> Radian'''
    def grad_a_rad(angulo):
        rad = 0.0
        rad = angulo*(3.1415/180) #0.01745
        #print("rad: ",rad)
        return rad

    '''Colisiones proyectil'''
    def colision_terreno(x,y):        
        if(x<=0 or x>=800):
            return False
        '''if(y>=400): ####colision terreno planoooooooooooooooooooo
            return False'''

    def proyectiles(lista):

        #proyectil por defecto (5 dmg, infinito)
        lista.append(['por defecto', 10, 0])

        #proyectil 105mm (50 dmg, 3 unidades)
        lista.append(['105mm ', 50, 3])
        
        #proyectil perforante (40 dmg, 10 undidades)
        lista.append(['Perfor', 40, 9])
        
        #proyectil 60mmm (30 dmg, 3 unidades)
        lista.append(['60mm ', 30, 3])

        return lista

    def restaProyectiles(listaProyectiles, opc):

        if opc == 0:
            listaProyectiles[opc][2] = listaProyectiles[opc][2]-1
        if opc == 1:
            listaProyectiles[opc][2] = listaProyectiles[opc][2]-1
        if opc == 2:
            listaProyectiles[opc][2] = listaProyectiles[opc][2]-1
        if opc == 3:
            listaProyectiles[opc][2] = listaProyectiles[opc][2]-1
        
        return listaProyectiles