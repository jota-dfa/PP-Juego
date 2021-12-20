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
textoBotonSalir = 'Salir'
seleccion_mapa = 3#random.randint(1,3)

def Juego(g, viento_activo, Lista_proyectiles, jugadores):

    if viento_activo == 0:
        print("Viento Desactivado")
        viento = 0

    if viento_activo == 1:
        print("Viento Activado")
        viento = 10
    
    ##### FUNCIONES PRINCIPALES DEL JUEGO ######

    #VENTANA
    Angulo_usuario = ''
    Velocidad_usuario = ''
    Rect_izq_1 = pygame.Rect(150,830, 100,50)#Angulo izq
    Rect_izq_2 = pygame.Rect(1450,830, 100,50)#Velocidad izq
    Rect_izq_3 = pygame.Rect(750,10, 100,50)#Velocidad izq
    
    clock = pygame.time.Clock()######################################
    VENTANA = pygame.display.set_mode((ANCHO, ALTO)) # (Horizontal, Vertical)
    pygame.display.set_caption("Scorched World")

    def Opciones_izq(): # objetos
        pygame.draw.rect(VENTANA, BLANCO,( 0, 700, 10000, 600))
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_1,2) #Ventana angulo
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_2,2) #Ventana
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_3,2) #Ventana boton salir
        
        texto_B_angulo = fuente_base.render(texto_angulo,True,(0,0,0))
        texto_B_velocidad = fuente_base.render(texto_velocidad,True,(0,0,0))
        texto_B_salir = fuente_base.render(textoBotonSalir,True,(0,0,0))
        VENTANA.blit(texto_B_angulo,(Rect_izq_1.x - 140 , Rect_izq_1.y + 10))
        VENTANA.blit(texto_B_velocidad,(Rect_izq_2.x - 185,Rect_izq_2.y + 10))
        VENTANA.blit(texto_B_salir,(Rect_izq_3.x - 0,Rect_izq_3.y + 0))

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
        tr_x, tr_y = Proyectil.Proyectil.pr_trayectoria(v, g, t, angl, posX, posY)
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

    def check_colision(x,y, cont, tx, ty, numTank):
        if(Mapa_2.Mapa.colision_terreno(x, y) == False): #lim . laterales
            return False
        if(Mapa_2.Mapa.colisionBala_terreno(x,y , seleccion_mapa, cont) == False):
            print("DISTANCIA MAXIMA",dMax)
            return False
        """if(Tanques_2.Tanques.col_proyectil_tanque(x,y, tx, ty, numTank) == True): # colision proyectil-tanque 
            return True"""
        

    def desordenarList(list, lim_der):
        return random.sample(list, lim_der) 

    def spawn_tanques(mov_y,seleccion_mapa, numTanks, listaVida): # agregar parametro /numTanks
        
        # Esta función lo que hace es que tiene los puntos de reaparicion para los tanques, luego se aleatorizan los turnos
        # y tambien se aleatorizan los puntos (x,y) de aparicion 

        if(seleccion_mapa==1):
            a = random.randint(1,4)
            b = random.randint(1,4)

            listPos = {(40, 30), (326, 30), (500, 30), (670, 30), (850, 30), (1015, 30), (1238, 30), (1561, 30)}

            #listTanks = {1, 2, 3, 4, 5, 6}
            listTurn = {1, 2, 3, 4, 5, 6}

            listPos = desordenarList(listPos, len(listPos))
            #listTanks = desordenarList(listTanks, numTanks) # (List, Len(listTanks))
            listTurn = desordenarList(listTurn, numTanks)

            for i in range(numTanks):
                if( i == 0 ):
                    Tanques_2.Tanques.p1(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 1 ):
                    Tanques_2.Tanques.p2(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 2 ):
                    Tanques_2.Tanques.p3(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 3 ):
                    Tanques_2.Tanques.p4(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 4 ):
                    Tanques_2.Tanques.p5(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 5 ):
                    Tanques_2.Tanques.p6(VENTANA, listPos[i][0], listPos[i][1])

            return listPos
        
        if(seleccion_mapa==2):
            a = random.randint(1,4)
            b = random.randint(1,4)
            
            listPos = {(23, 30), (147, 30), (323, 30), (483, 30), (730, 30), (1133, 30), (1283, 30), (1449, 30)}
            #listTanks = {1, 2, 3, 4, 5, 6}
            listTurn = {1, 2, 3, 4, 5, 6}

            listPos = desordenarList(listPos, len(listPos))
            #listTanks = desordenarList(listTanks, numTanks) # (List, Len(listTanks))
            listTurn = desordenarList(listTurn, numTanks)

            for i in range(numTanks):
                if( i == 0 ):
                    Tanques_2.Tanques.p1(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 1 ):
                    Tanques_2.Tanques.p2(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 2 ):
                    Tanques_2.Tanques.p3(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 3 ):
                    Tanques_2.Tanques.p4(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 4 ):
                    Tanques_2.Tanques.p5(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 5 ):
                    Tanques_2.Tanques.p6(VENTANA, listPos[i][0], listPos[i][1])

            return listPos
        
        if(seleccion_mapa==3):
            
            a = random.randint(1,5)
            b = random.randint(1,4)

            listPos = {(21, 30), (179, 30), (439, 30), (755, 30), (967, 30), (1085, 30), (1305, 30), (1569, 30)}
            #listTanks = {1, 2, 3, 4, 5, 6}
            listTurn = {1, 2, 3, 4, 5, 6}

            listPos = desordenarList(listPos, len(listPos))
            #listTanks = desordenarList(listTanks, numTanks) # (List, Len(listTanks))
            listTurn = desordenarList(listTurn, numTanks)

            for i in range(numTanks):
                if( i == 0 ):
                    Tanques_2.Tanques.p1(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 1 ):
                    Tanques_2.Tanques.p2(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 2 ):
                    Tanques_2.Tanques.p3(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 3 ):
                    Tanques_2.Tanques.p3(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 4 ):
                    Tanques_2.Tanques.p4(VENTANA, listPos[i][0], listPos[i][1])
                if( i == 5 ):
                    Tanques_2.Tanques.p5(VENTANA, listPos[i][0], listPos[i][1])

            return listPos

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

    def expressIA(nJugadores, nIa):
        newList = []
        for i in range(nJugadores):
            if(i < nIA):
                newList.append((i, -1))
            else:
                newList.append((i, 1))
        return newList
                   

    def turno_1(posxEmisor, posyEmisor, listaProyectiles, turno):
        
        boton_rectangulo = pygame.Rect([0, 0, 40, 40])
        boton_rect = pygame.Rect(740,10, 50,25)
        boton_salir = pygame.Rect(740,10, 50,25)
        #Rect_izq_1 = pygame.Rect(100,460, 50,25)#Angulo izq
        #Rect_izq_2 = pygame.Rect(600,460, 50,25)#Velocidad izq
        xEmisor, yEmisor = posxEmisor+10, posyEmisor-190
      
        opcProyectil = 0#listaProyectiles[0][2]
        angulo_usuario = ''
        velocidad_usuario = ''
        botonSalir = ''
        fin_turno = 0
        active = 0
        active1 = False
        active2 = False
        while fin_turno == 0:

            text_surface1 = fuente_base.render(angulo_usuario, True,(0,0,0))
            text_surface2 = fuente_base.render(velocidad_usuario, True,(0,0,0))
            #text_surface3 = fuente_base.render(botonSalir, True,(0,0,0))
            
            boton = pygame.image.load("imagenes/button_reset_n.png")
            VENTANA.blit(boton, (0, 0))
            
            if listaProyectiles[1][2] == 0 and listaProyectiles[2][2] == 0 and listaProyectiles[3][2] == 0: # elimina tanque por su vida
                if turno == 1:
                    vida[0] = 0
                if turno == 2:
                    vida[1]= 0
                if turno == 3:
                    vida[1]= 0
                if turno == 4:
                    vida[1]= 0
                if turno == 5:
                    vida[1]= 0
                if turno == 6:
                    vida[1]= 0
                return 1,0,0,0,0,listaProyectiles, opcProyectil

            for event in pygame.event.get():


                if event.type == pygame.MOUSEBUTTONDOWN: #VELOCIDAD

                    """ boton salir """
                    if boton_rect.collidepoint(event.pos):
                        print("apreto salir")
                        return -1,0,0,0,0,listaProyectiles, opcProyectil

                    """ boton reinicio """
                    if boton_rectangulo.collidepoint(event.pos):
                        return 1,0,0,0,0,listaProyectiles, opcProyectil
                    
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

                    if event.key == pygame.K_SPACE: # Lanza proyectil al presionar barra espaciadora
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
                        if(turno == 0):
                            elem_inciales(seleccion_mapa)
                            Opciones_izq()
                            Tanques_2.Tanques.aparecen(VENTANA, listaPosiciones, numTanques)
                            #InterfazJuego_2.InterfazJuego.marcadorJugador(VENTANA, 1, xEmisor, yEmisor)
                        else:
                            elem_iniciales2(seleccion_mapa)
                            Opciones_izq()
                            Tanques_2.Tanques.aparecen(VENTANA, listaPosiciones, numTanques)
                            #InterfazJuego_2.InterfazJuego.marcadorJugador(VENTANA, 1, xEmisor, yEmisor)

                        """if turno == 1:
                            Tanques_2.Tanques.p1(VENTANA, posxEmisor, posyEmisor) #permanecia de tanques p1
                            Tanques_2.Tanques.p2(VENTANA, posxDestino, posyDestino)
                        if turno == 2:
                            Tanques_2.Tanques.p2(VENTANA, posxEmisor, posyEmisor) #permanecia de tanques p1
                            Tanques_2.Tanques.p1(VENTANA, posxDestino, posyDestino)"""
                        #InterfazJuego_2.InterfazJuego.marcadorJugador(VENTANA, turno, posxEmisor, posyEmisor)
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
        viento_suma = random.randint(-viento,viento)
        angulo_usuario, velocidad_usuario = validar_angulo(int(angulo_usuario)), validar_velocidad(float(velocidad_usuario)+viento_suma)
        angulo_usuario = Proyectil.Proyectil.grad_a_rad(angulo_usuario)
        posxEmisor, posyEmisor = ((posxEmisor+25), posyEmisor)
        print("Viento Suma: ",viento_suma)
        print("Velocidad Usuario: ",velocidad_usuario)
        print("opcion de proyectil: ", opcProyectil)
        
        return 0, angulo_usuario, velocidad_usuario, posxEmisor, posyEmisor, listaProyectiles, opcProyectil
                 

    active = False
    fin_juego = 0
    municion_105 = Lista_proyectiles[2]
    municion_perfor = Lista_proyectiles[1]
    municion_60 = Lista_proyectiles[0]
    listaPosiciones = []
    listaProyectiles = []
    listaProyectilesB = []
    listaProyectiles = Proyectil.Proyectil.proyectiles(listaProyectiles,municion_105, municion_perfor,municion_60)
    listaProyectilesB = Proyectil.Proyectil.proyectiles(listaProyectilesB,municion_105, municion_perfor,municion_60)
    vida = [100, 100, 100, 100, 100, 100]
    kills = [0, 0, 0, 0, 0, 0, 0]

    numTanques = jugadores
    posEmisor = 0
    aux = 0
    indexListPos = 0
    nIA = 0 #####
    nIA = nIA - 1
    listaIA = expressIA(numTanques, nIA)
    turno = listaIA[indexListPos][1]

    #print(listaProyectiles[0][1])

    while turno != 0: #PRINCIPAL
        
        if aux == 0: #Carga elementos iniciales -> elem_inciales(seleccion_mapa)
            listaPosiciones = spawn_tanques(0,seleccion_mapa,numTanques, vida) #num tanques
            for i in range(numTanques): #num tanques
                listaPosiciones[i], contCaida = Tanques_2.Tanques.caen(aux, seleccion_mapa, listaPosiciones[i][0], listaPosiciones[i][1] )
                elem_inciales(seleccion_mapa)
                Opciones_izq()
                
            Tanques_2.Tanques.aparecen(VENTANA, listaPosiciones, numTanques)
            
            x1_1, y1_2 = listaPosiciones[0][0], listaPosiciones[0][1]
            #Tanques_2.Tanques.p1(VENTANA, x1_1, y1_2) #permanecia de tanques p1
            #Tanques_2.Tanques.p2(VENTANA, x2_1,y2_2)
            vida = Tanques_2.Tanques.vida(VENTANA, vida, 0, 0)

        x1_1, y1_2 = listaPosiciones[indexListPos][0], listaPosiciones[indexListPos][1]

        vida = Tanques_2.Tanques.vida(VENTANA, vida, 0, 0)
        pygame.display.update()

        pygame.display.update()  #Actualizacion ventana       
        InterfazJuego_2.InterfazJuego.altura_distancia()         
        
        if turno == 1: ## Turno == 1, acciones de jugador
            print("\nJUGADOR", indexListPos+1)
            #fin_juego, angulo_usuario, velocidad_usuario, posxEmisor, posyEmisor, posxDestino, posyDestino
            InterfazJuego_2.InterfazJuego.marcadorJugador(VENTANA, 1, x1_1, y1_2)
            fin_juego, angulo, velocidad, posX_tanque, posY_tanque, listaProyectiles, opcProyectil = turno_1(x1_1, y1_2, listaProyectiles, aux)

            t = 0
            alt_max = Altura_maximo(velocidad , angulo)
            turno += 5 #no entrada
            aux += 1 #Contador de turnos
            posEmisor += 1

        #print(indexListPos)

        if turno == -1:
            print("\nJUGADOR", indexListPos+1)
            posX_tanque, posY_tanque = x1_1, y1_2
            velocidad = random.randint(30, 100)
            ang = random.randint(20, 170)
            angulo = Proyectil.Proyectil.grad_a_rad(ang)
            t = 0
            alt_max = Altura_maximo(velocidad , angulo)
            turno += 5 #no entrada
            aux += 1 #Contador de turnos
            print("aux", aux)
            posEmisor += 1
            opcProyectil = random.randint(0,3)


        if(fin_juego == -1):
            return -1

        time.sleep(0.002)
        t = t+0.02*10 #velocidad *5
        x, y = proyectil(t, velocidad, angulo, posX_tanque, posY_tanque-15)
        dMax = Distancia_maximo(posX_tanque , posY_tanque , x , y)
        InterfazJuego_2.InterfazJuego.dibujar_altura(alt_max)
        InterfazJuego_2.InterfazJuego.dibujar_distancia(dMax)
        
        ''' COLSIONES '''

        colision = check_colision(x, y, aux, listaPosiciones[indexListPos][0], listaPosiciones[indexListPos][0], numTanques)              # col_posxT, col_posyT = tanque destino
        colision_suicidio = check_colision(x, y, aux, listaPosiciones[indexListPos][0], listaPosiciones[indexListPos][0], numTanques) # posX_tanque, posY_tanque = tanque emisor
        
        if(colision == False):     ##### False = colisiono terreno -> destruccion terreno, cambia turno

            Mapa_2.Mapa.destruccionMapa(VENTANA, x, y, seleccion_mapa, aux, opcProyectil)
            vida = Mapa_2.Mapa.dañoRadio(x,y, numTanques, vida, indexListPos, opcProyectil, listaPosiciones)
            turno = listaIA[indexListPos][1]
            indexListPos += 1
            elem_iniciales2(seleccion_mapa)
            Opciones_izq()

        vida = Tanques_2.Tanques.vida(VENTANA, vida, 0, 0)
        pygame.display.update()

        #eliminacion de los tanques

        if(fin_juego == 1):
            break

        ''' FIN COLISIONES '''

        for i in range(numTanques):
            listaPosiciones[i], contCaida = Tanques_2.Tanques.caen(aux, seleccion_mapa, listaPosiciones[i][0], listaPosiciones[i][1])
            vida = Tanques_2.Tanques.vida(VENTANA, vida, (contCaida*0.2), i+1)
        #elem_iniciales2(seleccion_mapa)
        Opciones_izq()
        Tanques_2.Tanques.aparecen(VENTANA, listaPosiciones, numTanques)

        if(indexListPos == numTanques):
            indexListPos = 0

        InterfazJuego_2.InterfazJuego.turno_jugador(indexListPos+1)
        InterfazJuego_2.InterfazJuego.altura_distancia()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()            

            if event.type == pygame.QUIT:
                turno = 0
                pygame.quit()
                quit()


        clock.tick(60)
