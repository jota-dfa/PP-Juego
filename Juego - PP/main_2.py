import pygame, sys
from pygame.locals import *
import math
import time
import random
from PIL import Image

import Mapa
import Tanques_2
import Proyectil
import InterfazJuego_2
import Mapa_2


pygame.font.init()
#GLOBALES - CONSTANTES
ALTO = 900
ANCHO = 1600

CELESTE = (135, 206, 235)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
CAFE = (145, 105, 81)
ROJO = (255, 0, 0)
AZUL = (30, 45, 110)
GRIS =  (131,139,139)
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

fuente_base = pygame.font.Font(None,50)
texto_angulo = 'Angulo'
texto_velocidad = 'Velocidad'
seleccion_mapa = random.randint(1,3)

def Juego():
    
    ##### FUNCIONES PRINCIPALES DEL JUEGO ######

    #VENTANA
    Angulo_usuario = ''
    Velocidad_usuario = ''
    Rect_izq_1 = pygame.Rect(150,830, 100,50)#Angulo izq
    Rect_izq_2 = pygame.Rect(1450,830, 100,50)#Velocidad izq
    
    clock = pygame.time.Clock()######################################
    VENTANA = pygame.display.set_mode((ANCHO, ALTO)) # (Horizontal, Vertical)
    pygame.display.set_caption("Scorched World")

    def Opciones_izq(): # objetos
        pygame.draw.rect(VENTANA, BLANCO,( 0, 700, 10000, 600))
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_1,2) #Ventana angulo
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_2,2) #Ventana
        
        texto_B_angulo = fuente_base.render(texto_angulo,True,(0,0,0))
        texto_B_velocidad = fuente_base.render(texto_velocidad,True,(0,0,0))
        VENTANA.blit(texto_B_angulo,(Rect_izq_1.x - 140 , Rect_izq_1.y + 10))
        VENTANA.blit(texto_B_velocidad,(Rect_izq_2.x - 185,Rect_izq_2.y + 10))

    def Opciones_validar_ang():
        pygame.draw.rect(VENTANA, BLANCO,( 0, 450, 400 , 500))
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_1,2) #Ventana angulo

        texto_B_angulo = fuente_base.render(texto_angulo,True,(0,0,0))
        VENTANA.blit(texto_B_angulo,(Rect_izq_1.x - 90 , Rect_izq_1.y + 4))
        
    def Opciones_validar_vel():
        pygame.draw.rect(VENTANA, BLANCO,( 250, 450, 5000 , 800))
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_2,2) #Ventana velocidad
        
        texto_B_velocidad = fuente_base.render(texto_velocidad,True,(0,0,0))
        VENTANA.blit(texto_B_velocidad,(Rect_izq_2.x - 115,Rect_izq_2.y + 4))

    ''' Elementos Inciales '''
    
    def elem_inciales(seleccion_mapa):
        #TERRENO
        Mapa_2.Mapa.terreno(VENTANA, seleccion_mapa)

    def elem_iniciales2(seleccion_mapa):
        Mapa_2.Mapa.terreno2(VENTANA, seleccion_mapa)

    elem_inciales(seleccion_mapa)
    Opciones_izq()

    ''' Fin elementos iniciales '''

    #PROYECTILES
    def proyectil(t, v, angl, posX, posY): # a,b posTanques
        tr_x, tr_y = Proyectil.Proyectil.pr_trayectoria(v, 9.8, t, angl, posX, posY)
        #colision_terreno = True
        #colision_terreno = Mapa_2.Mapa.colision_terreno(tr_x, tr_y)
        Proyectil.Proyectil.dibu_proyectil(tr_x, tr_y, VENTANA)
        return tr_x, tr_y

    def Distancia_maximo(x1, y1 ,x , y ):
        #x1 e y1 = coordenada inicial tanque
        #x2 e y2 = punto de colision de la bala
        d_max = math.sqrt((math.pow(x-x1,2) + math.pow(y-y1,2) )) 
        return d_max

    def Altura_maximo(velocidad , angulo):
        alt_max = (math.pow(velocidad,2) * math.pow(math.sin(angulo),2))/19.6 
        return alt_max

    def check_colision(x,y, a,b, cont):
        if(Mapa_2.Mapa.colision_terreno(x, y) == False): #lim . laterales
            return False
        if(Mapa_2.Mapa.colisionBala_terreno(x,y , seleccion_mapa, cont) == False):
            print("DISTANCIA MAXIMA",dMax)
            return False
        if(Tanques_2.Tanques.col_proyectil_tanque(x,y, a,b) == True):
            return True


    def spawn_tanques(mov_y,seleccion_mapa): #animacion , escalar con un arreglo de randoms
        
        if(seleccion_mapa==1):
            a = random.randint(1,4)
            b = random.randint(1,4)
            
            coordenada1_1, coordenada1_2 = 55, 217
            coordenada2_1, coordenada2_2 = 849, 263

            return coordenada1_1, coordenada1_2, coordenada2_1,coordenada2_2
        
        if(seleccion_mapa==2):
            a = random.randint(1,4)
            b = random.randint(1,4)
            
            coordenada1_1, coordenada1_2 = 336, 415
            coordenada2_1, coordenada2_2 = 1204, 315
            
            return coordenada1_1, coordenada1_2, coordenada2_1,coordenada2_2
        
        if(seleccion_mapa==3):
            
            a = random.randint(1,5)
            b = random.randint(1,4)

            coordenada1_1, coordenada1_2 = 146, 414
            coordenada2_1, coordenada2_2 = 1060, 314

            return coordenada1_1, coordenada1_2, coordenada2_1,coordenada2_2

    def validar_angulo(x):
        if x < 0 or x > 180:
            Opciones_validar_ang()
            while x < 0 or x > 180:
                print("ERROR, Angulo incorrecto")
                
            return x    

        else:
            angulo_usuario = x
            return angulo_usuario   

    def validar_velocidad(y):
        if y < 0 or y > 250:
            Opciones_validar_vel()
            while y < 0 or y > 250:
                print("ERROR, Velocidad incorrecta")

                
            return y    

        else:
            velocidad_usuario = y
            return velocidad_usuario         

    def turno_1(posxEmisor, posyEmisor, posxDestino, posyDestino, listaProyectiles, turno):
        
        boton_rectangulo = pygame.Rect([0, 0, 40, 40])
        boton_rect =  boton_rect = pygame.Rect(740,10, 50,25)
        #Rect_izq_1 = pygame.Rect(100,460, 50,25)#Angulo izq
        #Rect_izq_2 = pygame.Rect(600,460, 50,25)#Velocidad izq
        xEmisor, yEmisor = posxEmisor+10, posyEmisor-190
      
        opcProyectil = 0#listaProyectiles[0][2]
        angulo_usuario = ''
        velocidad_usuario = ''
        fin_turno = 0
        active = 0
        active1 = False
        active2 = False
        while fin_turno == 0:

            text_surface1 = fuente_base.render(angulo_usuario, True,(0,0,0))
            text_surface2 = fuente_base.render(velocidad_usuario, True,(0,0,0))
            
            boton = pygame.image.load("imagenes/button_reset_n.png")
            VENTANA.blit(boton, (0, 0))
            
            if listaProyectiles[1][2] == 0 and listaProyectiles[2][2] == 0 and listaProyectiles[3][2] == 0:
                if turno == 1:
                    vida[0] = 0
                if turno == 2:
                    vida[1]= 0
                return 1,0,0,0,0,0,0,listaProyectiles, opcProyectil

            for event in pygame.event.get():


                if event.type == pygame.MOUSEBUTTONDOWN: #VELOCIDAD

                    """ boton salir """
                    if boton_rect.collidepoint(event.pos):
                        return 1,0,0,0,0,0,0,listaProyectiles, opcProyectil

                    """ boton reinicio """
                    if boton_rectangulo.collidepoint(event.pos):
                        return 1,0,0,0,0,0,0,listaProyectiles, opcProyectil
                    
                    """ rectangulo angulo """
                    if Rect_izq_1.collidepoint(event.pos):
                        active1 = True
                        active2 = False
                    else:
                        active1 = False
                
                    """ rectangulo velocidad """
                    if Rect_izq_2.collidepoint(event.pos):
                        active2 = True
                        active1 = False
                    else:
                        active2 = False

                if event.type == pygame.KEYDOWN:
                    
                    previo = event.unicode

                    if event.key == pygame.K_SPACE: ###############
                        listaProyectiles = Proyectil.Proyectil.restaProyectiles(listaProyectiles, opcProyectil)
                        fin_turno = 1

                    """ input texto velocidad y angulo"""
                    if previo != 'i':    
                        if active1 == True:
                            if event.key == pygame.K_BACKSPACE:
                                angulo_usuario = angulo_usuario[:-1]
                            else:
                                angulo_usuario += event.unicode

                        if active2 == True:
                            if event.key == pygame.K_BACKSPACE:
                                velocidad_usuario = velocidad_usuario[:-1]
                            else:
                                velocidad_usuario += event.unicode

                    if previo == 'i':
                        listaProyectiles, opcProyectil = InterfazJuego_2.InterfazJuego.menuProyectiles(VENTANA, xEmisor, yEmisor, listaProyectiles)
                        elem_iniciales2(seleccion_mapa)
                        Opciones_izq()
                        if turno == 1:
                            Tanques_2.Tanques.p1(VENTANA, posxEmisor, posyEmisor,seleccion_mapa) #permanecia de tanques p1
                            Tanques_2.Tanques.p2(VENTANA, posxDestino, posyDestino,seleccion_mapa)
                        if turno == 2:
                            Tanques_2.Tanques.p2(VENTANA, posxEmisor, posyEmisor,seleccion_mapa) #permanecia de tanques p1
                            Tanques_2.Tanques.p1(VENTANA, posxDestino, posyDestino,seleccion_mapa)
                        InterfazJuego_2.InterfazJuego.marcadorJugador(VENTANA, turno, posxEmisor, posyEmisor)
                        Tanques_2.Tanques.vida(VENTANA, vida, 0, 0)
                        InterfazJuego_2.InterfazJuego.turno_jugador(turno)
                        InterfazJuego_2.InterfazJuego.altura_distancia()

                    if previo == ' ':
                        if (angulo_usuario == '' or velocidad_usuario == ''):
                            fin_turno = 0

                VENTANA.blit(text_surface1,(Rect_izq_1.x + 3, Rect_izq_1.y + 3))
                Rect_izq_1.w = max(100, text_surface1.get_width() + 10)

                VENTANA.blit(text_surface2,(Rect_izq_2.x + 3, Rect_izq_2.y + 3))
                Rect_izq_2.w = max(100, text_surface2.get_width() + 10)

                pygame.display.update()

        """ validaciones """        
        angulo_usuario, velocidad_usuario = validar_angulo(int(angulo_usuario)), validar_velocidad(float(velocidad_usuario))
        angulo_usuario = Proyectil.Proyectil.grad_a_rad(angulo_usuario)
        posxEmisor, posyEmisor = ((posxEmisor+25), posyEmisor)

        return 0, angulo_usuario, velocidad_usuario, posxEmisor, posyEmisor, posxDestino, posyDestino, listaProyectiles, opcProyectil
                 

    turno = 1
    cont = 0
    active = False
    fin_juego = 0

    listaProyectiles = []
    listaProyectilesB = []
    listaProyectiles = Proyectil.Proyectil.proyectiles(listaProyectiles)
    listaProyectilesB = Proyectil.Proyectil.proyectiles(listaProyectilesB)
    vida = [100, 100]

   

    while turno != 0: #PRINCIPAL
        
        if cont == 0:
            x1_1, y1_2, x2_1, y2_2 = spawn_tanques(0,seleccion_mapa)
            Tanques_2.Tanques.p1(VENTANA, x1_1, y1_2,seleccion_mapa) #permanecia de tanques p1
            Tanques_2.Tanques.p2(VENTANA, x2_1,y2_2,seleccion_mapa)
            vida = Tanques_2.Tanques.vida(VENTANA, vida, 0, 0)



        vida = Tanques_2.Tanques.vida(VENTANA, vida, 0, 0)
        pygame.display.update()

        
        pygame.display.update()  #Actualizacion ventana       
        InterfazJuego_2.InterfazJuego.altura_distancia()         

        if turno == 1:
            print("\nJUGADOR 1")
            #fin_juego, angulo_usuario, velocidad_usuario, posxEmisor, posyEmisor, posxDestino, posyDestino
            InterfazJuego_2.InterfazJuego.marcadorJugador(VENTANA, 1, x1_1, y1_2)
            fin_juego, angulo, velocidad, posX_tanque, posY_tanque, col_posxT, col_posyT, listaProyectiles, opcProyectil = turno_1(x1_1, y1_2, x2_1, y2_2, listaProyectiles, 1)
            
            t = 0
            alt_max = Altura_maximo(velocidad , angulo)
            turno += 5 #no entrada
            cont += 1 #Contador de turnos
            
        time.sleep(0.002)
        t = t+0.02*10 #velocidad *5
        x, y = proyectil(t, velocidad, angulo, posX_tanque, posY_tanque-3)
        dMax = Distancia_maximo(posX_tanque , posY_tanque , x , y)
        InterfazJuego_2.InterfazJuego.dibujar_altura(alt_max)
        InterfazJuego_2.InterfazJuego.dibujar_distancia(dMax)
        
        
        ''' COLSIONES '''

        colision = check_colision(x, y, col_posxT, col_posyT, cont)              # col_posxT, col_posyT = tanque destino
        colision_suicidio = check_colision(x, y, posX_tanque, posY_tanque, cont) # posX_tanque, posY_tanque = tanque emisor
        
        if(colision == False):     #####
                        
            if(cont % 2 != 0):
                Mapa_2.Mapa.destruccionMapa(VENTANA, x, y, seleccion_mapa, cont)
                turno = 2
            else:
                #turno 2
                Mapa_2.Mapa.destruccionMapa(VENTANA, x, y, seleccion_mapa, cont)
                turno = 1
            elem_iniciales2(seleccion_mapa)
            Opciones_izq()

        if(colision == True):       
            elem_iniciales2(seleccion_mapa)
            Opciones_izq()
            if(cont % 2 != 0):
                turno = 2
            else:
                turno = 1
            vida = Tanques_2.Tanques.vida(VENTANA, vida, listaProyectiles[opcProyectil][1], turno)
            pygame.display.update()
            #print("a ganado el jugador ", turno)
            #fin_juego = InterfazJuego.pantalla_ganador(VENTANA, turno)

        vida = Tanques_2.Tanques.vida(VENTANA, vida, 0, 0)
        pygame.display.update()

        if(colision_suicidio == True):      
            elem_iniciales2(seleccion_mapa)
            Opciones_izq()
            pygame.display.update()
            if(cont % 2 != 0):
                turno = 2
                id = 1
            else:
                turno = 1
                id = 2
            vida = Tanques_2.Tanques.vida(VENTANA, vida, listaProyectiles[opcProyectil][1], id)
            pygame.display.update()
            #print("a ganado el jugador ", turno)
            #fin_juego = InterfazJuego.pantalla_ganador(VENTANA, turno)
        
        if(vida[0] <= 0):
            fin_juego = InterfazJuego_2.InterfazJuego.pantalla_ganador(VENTANA, 2)
        if(vida[1] <= 0):
            fin_juego = InterfazJuego_2.InterfazJuego.pantalla_ganador(VENTANA, 1)

        if(fin_juego == 1):
            break

        ''' FIN COLISIONES '''

        Tanques_2.Tanques.p1(VENTANA, x1_1, y1_2,seleccion_mapa) #permanecia de tanques p1
        Tanques_2.Tanques.p2(VENTANA, x2_1, y2_2,seleccion_mapa)

        InterfazJuego_2.InterfazJuego.turno_jugador(turno)
        InterfazJuego_2.InterfazJuego.altura_distancia()

        if turno == 2:
            print("\nJUGADOR 2")
            InterfazJuego_2.InterfazJuego.marcadorJugador(VENTANA, 2, x2_1, y2_2)
            fin_juego, angulo, velocidad, posX_tanque, posY_tanque, col_posxT, col_posyT, listaProyectilesB, opcProyectil = turno_1(x2_1, y2_2, x1_1, y1_2, listaProyectilesB, 2)
            t = 0
            alt_max = Altura_maximo(velocidad , angulo)
            turno += 5 #no entrada
            cont += 1 #Contador de turnos

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()            

            if event.type == pygame.QUIT:
                turno = 0
                pygame.quit()
                quit()


        clock.tick(60)
