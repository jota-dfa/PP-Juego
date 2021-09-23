import pygame, sys
from pygame.locals import *
import math
import time
import random

pygame.font.init()
#GLOBALES - CONSTANTES
ALTO = 500
ANCHO = 800

CELESTE = (135, 206, 235)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
CAFE = (145, 105, 81)
ROJO = (255, 0, 0)
AZUL = (30, 45, 110)
GRIS =  pygame.Color(131,139,139)
fuente_base = pygame.font.Font(None,12)
texto_angulo = 'Angulo'
texto_velocidad = 'Velocidad'
 
class Mapa():

    def __init__(self) -> None:
        pass
        
    def terreno(VENTANA):
        terreno2 = pygame.draw.rect(VENTANA, CAFE, (0, 400, 800, 100)) #(posX, posY, Largo, Alto) BASE
        pointsT2 = [(0, 400), (40, 370), (95, 400), (144, 380), (250, 340), (390, 390),(410, 410)]
        #terreno2 = pygame.draw.polygon(VENTANA, CAFE, pointsT2, 70)
        #pointsT3 = [(500, 410), (530, 380), (540, 350), (560, 380), (590, 300), (615, 340),(645, 370),(680, 310), (700, 350), (800, 410) ]
        #terreno3 = pygame.draw.polygon(VENTANA, CAFE, pointsT3, 70)
        #rellenoT2 = pygame.draw.circle(VENTANA, CAFE, (530, 400), 51, 0) #Ciculo
        #rellenoT2_2 = pygame.draw.circle(VENTANA, CAFE, (650, 400), 70, 0) #Ciculo

class Tanques():

    def __init__(self, a,b,y):
        self.a = a
        self.b = b
        self.y = y

    def p1(VENTANA, a, y): # b = random
        p1_posNcolor = pygame.draw.rect(VENTANA, ROJO, [a, y , 50, 20]) #JUGADOR 1

    def p2(VENTANA, b, y): # a = random
        p2_posNcolor = pygame.draw.rect(VENTANA, BLANCO, [b, y , 50, 20]) #JUGADOR 2      

class Proyectil():
    
    def __init__(self, v,g,t,posTanque):
        self.v = v # velocidad inicial
        self.g = g #9.8
        self.t = t # inicial 0
        self.posTanque = posTanque

    '''Trayectoria de tiro Parabolico'''

    # v = velocidad // g = c. gravedad // t = tiempo // angl = angulo(rad) #
    # (x,y) = valores en ventana // (x, y_real) = valores reales de la ec.trayectoria #
    
    def pr_trayectoria(v, g, t, angl, posTanque): 
        x = posTanque+v*(math.cos(angl))*t # posTanque+v*(math.cos(angl))*t , posTanque =  posicion tanque 
        y_real = v*(math.sin(angl))*t-(g*t**2)/2
        y = 380 - y_real
        #print(x, y_real) #valores reales de ec. parabolica --> y_real
        return x, y
    
    '''Dibuja Proyectil'''
    def dibu_proyectil(x, y, VENTANA):
        proyectil = [pygame.draw.circle(VENTANA, NEGRO, (x, y), 2, 0)] #Ciculo

    '''Angulo --> Radian'''
    def grad_a_rad(angulo):
        rad = 0.0
        rad = angulo*(3.1415/180) #0.01745
        print("rad: ",rad)
        return rad

    '''Colisiones proyectil'''
    def colision_terreno(x, y):
        if(x<=0 or x>=800):
            return False
        if(y>=400):
            return False

class InterfazJuego():
    def __init__(self) -> None:
        pass

    '''def valIniciales():
        v = float(input("Velocidad: "))
        angulo = float(input("Angulo (90>a>0): "))
        angulo = float(Proyectil.grad_a_rad(angulo))
        return v, angulo '''

def Juego():
    
    ##### FUNCIONES PRINCIPALES DEL JUEGO ######

    #VENTANA
    Angulo_usuario = ''
    Velocidad_usuario = ''
    Angulo_usuario2 = ''
    Velocidad_usuario2 = '' 
    Rect_der_1 = pygame.Rect(700,460, 20,10)#Angulo der
    Rect_der_2 = pygame.Rect(700,480, 20,10)#Velocidad der
    Rect_izq_1 = pygame.Rect(60,460, 20,10)#Angulo izq
    Rect_izq_2 = pygame.Rect(60,480, 20,10)#Velocidad izq
    
    clock = pygame.time.Clock()######################################
    VENTANA = pygame.display.set_mode((ANCHO, ALTO)) # (Horizontal, Vertical)
    pygame.display.set_caption("Scorched World")

    def Opciones_izq():
        pygame.draw.rect(VENTANA, (255,255,255),( 0, 450, 1000, 600))
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_1,2)
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_2,2)
        texto_B_angulo = fuente_base.render(texto_angulo,True,(0,0,0))
        texto_B_velocidad = fuente_base.render(texto_velocidad,True,(0,0,0))
        VENTANA.blit(texto_B_angulo,(Rect_izq_1.x - 40 , Rect_izq_1.y))
        VENTANA.blit(texto_B_velocidad,(Rect_izq_2.x - 40,Rect_izq_2.y))

    def Opciones_der():
        pygame.draw.rect(VENTANA, GRIS, Rect_der_1,2)
        pygame.draw.rect(VENTANA, GRIS, Rect_der_2,2)
        texto_B_angulo = fuente_base.render(texto_angulo,True,(0,0,0))
        texto_B_velocidad = fuente_base.render(texto_velocidad,True,(0,0,0))
        VENTANA.blit(texto_B_angulo,(Rect_der_1.x + 30, Rect_der_1.y) )
        VENTANA.blit(texto_B_velocidad,(Rect_der_2.x + 30, Rect_der_2.y))     
    
    ''' Elementos Inciales '''
    
    def elem_inciales():
        #FONDO
        fondo = pygame.image.load("imagenes/fondo_2.png")
        VENTANA.blit(fondo, (0, 0))

        #TERRENO
        Mapa.terreno(VENTANA)
        #TANQUES
        #Tanques.p1(VENTANA)
        #Tanques.p2(VENTANA)

    elem_inciales()
    Opciones_izq()
    Opciones_der()
    ''' Fin elementos iniciales '''

    #PROYECTILES
    def proyectil(t, v, angl, pos): # a,b posTanques
        tr_x, tr_y = Proyectil.pr_trayectoria(v, 9.8, t, angl, pos)
        #colision_terreno = True
        colision_terreno = Proyectil.colision_terreno(tr_x, tr_y)
        Proyectil.dibu_proyectil(tr_x, tr_y, VENTANA)
        return tr_x, tr_y

    def check_colision(x, y):
        if(Proyectil.colision_terreno(x, y) == False):
            return False

    def spawn_tanques(mov_y): #animacion , escalar con un arreglo de randoms
        a = random.randint(0,200)
        b = random.randint(400,600)
        #mov_y = 0
        while (mov_y < 380): # 380 = colision temporal, cambiar 380 a variable
            #J1
            Tanques.p1(VENTANA, a, mov_y)
            #J2
            Tanques.p2(VENTANA, b, mov_y)
            mov_y = mov_y + 0.3
            pygame.display.update()
        
        elem_inciales()
        Opciones_izq()
        Opciones_der() 
        #Posicion definitiva tanques
        Tanques.p1(VENTANA, a, 380)
        Tanques.p2(VENTANA, b, 380)
        return a, b

    turno = 1
    cont = 0
    active = False
    Angulo_usuario = 0.0
    Angulo_usuario2 = 0.0
    Velocidad_usuario = 0.0
    Velocidad_usuario2 = 0.0
    while turno != 0: #PRINCIPAL
        
        if cont == 0:
            posT1, posT2 = spawn_tanques(0)
        else:
            Tanques.p1(VENTANA, posT1, 380) #permanecia de tanques p1
            Tanques.p2(VENTANA, posT2, 380) #         //           p2

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()  #Actualizacion ventana

        if event.type == pygame.MOUSEBUTTONDOWN:
            if Rect_izq_1.collidepoint(event.pos):
                active = True
                if event.type == pygame.KEYDOWN:
                    if active == True:  
                        if event.key == pygame.K_BACKSPACE:
                            Angulo_usuario = Angulo_usuario[:-1]
                else:
                    Angulo_usuario += event.unicode
            else:
                active = False

            if Rect_izq_2.collidepoint(event.pos):
                active = True
                if event.type == pygame.KEYDOWN:
                    if active == True:  
                        if event.key == pygame.K_BACKSPACE:
                           Velocidad_usuario = Velocidad_usuario[:-1]
                else:
                    Velocidad_usuario += event.unicode                
            else:
                active = False

            if Rect_der_1.collidepoint(event.pos):
                active = True
                if event.type == pygame.KEYDOWN:
                    if active == True:  
                        if event.key == pygame.K_BACKSPACE:
                            Angulo_usuario2 = Angulo_usuario2[:-1]
                else:
                    Angulo_usuario2 += event.unicode                
            else:
                active = False

            if Rect_der_2.collidepoint(event.pos):
                active = True
                if event.type == pygame.KEYDOWN:
                    if active == True:  
                        if event.key == pygame.K_BACKSPACE:
                            Velocidad_usuario2 = Velocidad_usuario2[:-1]
                else:
                    Velocidad_usuario2 += event.unicode                
            else:
                active = False
   
   
        if turno == 1:
            #print("\nJUGADOR 1")
            velocidad = Velocidad_usuario
            angulo = float(Angulo_usuario) 
            angulo = Proyectil.grad_a_rad(angulo)
            turno += 5 #no entrada
            cont += 1 #Contador de turnos
            t = 0
            pos_tanque = posT1+25 # 2 pos tanques 1 def de proyectil
        
        #t = pygame.time.get_ticks()/1000 #en segundos
        #t = t #5 veces mas rapido
        time.sleep(0.002)
        t = t+0.02*10 #velocidad *5
        x, y = proyectil(t, velocidad, angulo, pos_tanque)

        colision = check_colision(x, y)
        if(colision == False):
            turno = 0
            elem_inciales()
            if(cont % 2 != 0):
                turno += 2
            else:
                turno += 1
            time.sleep(0.5) #delay por turnos
            
        if turno == 2:
            #print("\nJUGADOR 2")
            velocidad = Velocidad_usuario2
            angulo = float(Angulo_usuario2)
            angulo = Proyectil.grad_a_rad(angulo)
            turno += 5 #condicion de no entrada
            cont += 1
            t = 0
            pos_tanque = posT2+25

        clock.tick(60)
        
Juego()