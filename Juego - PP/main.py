import pygame, sys
from pygame.locals import *
import math
import time
import random

import Mapa
import Tanques
import Proyectil
import InterfazJuego

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
GRIS =  (131,139,139)
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

fuente_base = pygame.font.Font(None,30)
texto_angulo = 'Angulo'
texto_velocidad = 'Velocidad'
seleccion_mapa = 1 #random.randint(1,3)

def Juego():
    
    ##### FUNCIONES PRINCIPALES DEL JUEGO ######

    #VENTANA
    Angulo_usuario = ''
    Velocidad_usuario = ''
    Rect_izq_1 = pygame.Rect(100,460, 50,25)#Angulo izq
    Rect_izq_2 = pygame.Rect(600,460, 50,25)#Velocidad izq
    
    clock = pygame.time.Clock()######################################
    VENTANA = pygame.display.set_mode((ANCHO, ALTO)) # (Horizontal, Vertical)
    pygame.display.set_caption("Scorched World")

    def Opciones_izq(): # objetos
        pygame.draw.rect(VENTANA, (255,255,255),( 0, 450, 1000, 600))
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_1,2) #Ventana angulo
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_2,2) #Ventana
        
        texto_B_angulo = fuente_base.render(texto_angulo,True,(0,0,0))
        texto_B_velocidad = fuente_base.render(texto_velocidad,True,(0,0,0))
        VENTANA.blit(texto_B_angulo,(Rect_izq_1.x - 90 , Rect_izq_1.y + 4))
        VENTANA.blit(texto_B_velocidad,(Rect_izq_2.x - 115,Rect_izq_2.y + 4))

    def Opciones_validar_ang():
        pygame.draw.rect(VENTANA, (255,255,255),( 0, 450, 400 , 500))
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_1,2) #Ventana angulo

        texto_B_angulo = fuente_base.render(texto_angulo,True,(0,0,0))
        VENTANA.blit(texto_B_angulo,(Rect_izq_1.x - 90 , Rect_izq_1.y + 4))
        
    def Opciones_validar_vel():
        pygame.draw.rect(VENTANA, (255,255,255),( 250, 450, 5000 , 800))
        pygame.draw.rect(VENTANA, GRIS, Rect_izq_2,2) #Ventana velocidad
        
        texto_B_velocidad = fuente_base.render(texto_velocidad,True,(0,0,0))
        VENTANA.blit(texto_B_velocidad,(Rect_izq_2.x - 115,Rect_izq_2.y + 4))

    ''' Elementos Inciales '''
    
    def elem_inciales(seleccion_mapa):
        #FONDO
        
        if(seleccion_mapa==1):
            fondo = pygame.image.load("imagenes/fondo_2.png")
            VENTANA.blit(fondo, (0, 0))
        if(seleccion_mapa==2):
            fondo = pygame.image.load("imagenes/fondo_3.png")
            VENTANA.blit(fondo, (0, 0))

        if(seleccion_mapa==3):
            fondo = pygame.image.load("imagenes/fondo_4.png")
            VENTANA.blit(fondo, (0, 0))
        #TERRENO
        Mapa.Mapa.terreno(VENTANA,seleccion_mapa)
        #TANQUES
        #Tanques.p1(VENTANA)
        #Tanques.p2(VENTANA)

    elem_inciales(seleccion_mapa)
    Opciones_izq()

    ''' Fin elementos iniciales '''

    #PROYECTILES
    def proyectil(t, v, angl, posX, posY): # a,b posTanques
        tr_x, tr_y = Proyectil.Proyectil.pr_trayectoria(v, 9.8, t, angl, posX, posY)
        #colision_terreno = True
        colision_terreno = Proyectil.Proyectil.colision_terreno(tr_x, tr_y)
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

    def check_colision(x,y, a,b):
        if(Proyectil.Proyectil.colision_terreno(x, y) == False):
            return False
        if(Mapa.Mapa.colisionBala_terreno(x,y , seleccion_mapa) == False):
            print("DISTANCIA MAXIMA",dMax)
            return False
        if(Tanques.Tanques.col_proyectil_tanque(x,y, a,b) == True):
            return True


    def spawn_tanques(mov_y,seleccion_mapa): #animacion , escalar con un arreglo de randoms
        if(seleccion_mapa==1):
            a = 1
            b =random.randint(1,2)
            
            xl1_1=random.randint(0,100)
            yl1_1=((-0.5*xl1_1)-155)*-1     #Recta 1 - tanque 1
            yl2_1=220                       #Recta 2 - tanque 1
            xl3_1=random.randint(210,300)
            yl3_1=((0.9*xl3_1)-400)*-1+40   #Recta 3 - tanque 1
            
            if(a==1):
                coordenada1_1 = xl1_1
                coordenada1_2 = yl1_1+80
            if(a==2):
                coordenada1_1 = xl1_1
                coordenada1_2 = yl2_1
            if(a==3):
                coordenada1_1 = xl3_1
                coordenada1_2 = yl3_1

            xl1_2=random.randint(550,700)
            yl1_2=((0.16*xl1_2)-265)*-1  #Recta 1 - tanque 2, recta compartida t1 y t2
            xl2_2 =random.randint(300,550)
            yl2_2 =((-0.32*xl2_2)-34)*-1+50  #Recta 2 - tanque 2
            
            if(b==1):
                coordenada2_1 = xl1_2
                coordenada2_2 = yl1_2+80
            if(b==2):
                coordenada2_1 = xl2_2
                coordenada2_2 = yl2_2 
            
            return coordenada1_1, coordenada1_2, coordenada2_1,coordenada2_2
        if(seleccion_mapa==2):
            a = random.randint(1,6)
            b = random.randint(1,6)
            
            xl1_1 = random.randint(0,74)
            yl1_1 = (1.3*xl1_1-250)*-1
            
            xl2_1 =random.randint(74,150)
            yl2_1=((-1.3*xl2_1)-54)*-1

            xl3_1 = random.randint(150,250)
            yl3_1 = 250

            xl4_1 = random.randint(250,300)
            yl4_1 = xl4_1

            xl5_1 = random.randint(300,350)
            yl5_1 = (xl5_1 - 600)*-1

            xl6_1 = random.randint(350,390)
            yl6_1 = 250

            if(a==1):
                coordenada1_1 = xl1_1
                coordenada1_2 = yl1_1
            if(a==2):
                coordenada1_1 = xl1_1
                coordenada1_2 = yl2_1
            if(a==3):
                coordenada1_1 = xl3_1
                coordenada1_2 = yl3_1
            if(a==4):
                coordenada1_1 = xl4_1
                coordenada1_2 = yl4_1
            if(a==5):
                coordenada1_1 = xl5_1
                coordenada1_2 = yl5_1
            if(a==6):
                coordenada1_1 = xl6_1
                coordenada1_2 = yl6_1

            #################
            

            xl1_2 = random.randint(400,450)
            yl1_2 = 250

            xl2_2 = random.randint(450,500)
            yl2_2 = (-xl2_2 + 200)*-1   

            xl3_2 = random.randint(500,550)
            yl3_2 = (xl3_2 -800)*-1
            
            xl4_2 = random.randint(550,650)
            yl4_2 = 250
            
            xl5_2 = random.randint(650,725)
            yl5_2 = ((1.3*xl5_2)-1090)*-1
        
            xl6_2 = random.randint(725,800)
            yl6_2 = ((-1.3*xl6_2)+800)*-1

            if(b==1):
                coordenada2_1 = xl1_2
                coordenada2_2 = yl1_2
            if(b==2):
                coordenada2_1 = xl2_2
                coordenada2_2 = yl2_2 
            if(b==3):
                coordenada2_1 = xl3_2
                coordenada2_2 = yl3_2
            if(b==4):
                coordenada2_1 = xl4_2
                coordenada2_2 = yl4_2 
            if(b==5):
                coordenada2_1 = xl5_2
                coordenada2_2 = yl5_2
            if(b==6):
                coordenada2_1 = xl6_2
                coordenada2_2 = yl6_2 
            return coordenada1_1, coordenada1_2, coordenada2_1,coordenada2_2
        if(seleccion_mapa==3):
            a = random.randint(1,8)
            b = 1

            xl1_1 = random.randint(0,34)
            yl1_1 = ((0.3*xl1_1)-176)*-1

            xl2_1 = random.randint(38,49)
            yl2_1 = ((-5.4*xl2_1)+47)*-1

            xl3_1 = random.randint(49,100)
            yl3_1 = ((-0.5*xl3_1)-195)*-1

            xl4_1 = random.randint(100,149)
            yl4_1 = ((-1.9*xl4_1)-59)*-1

            xl5_1 = random.randint(149,190)
            yl5_1 = ((2.6*xl5_1)-745)*-1

            xl6_1 = random.randint(190,253)
            yl6_1 = ((0.6*xl6_1)-349)*-1

            xl7_1 = random.randint(253,283)
            yl7_1 = ((1.5*xl7_1)-581)*-1

            xl8_1 = random.randint(283,339)
            yl8_1 = ((-1.5*xl8_1)+289)*-1

            if(a==1):
                coordenada1_1 = xl1_1
                coordenada1_2 = yl1_1-10
            if(a==2):
                coordenada1_1 = xl1_1
                coordenada1_2 = yl2_1
            if(a==3):
                coordenada1_1 = xl3_1
                coordenada1_2 = yl3_1
            if(a==4):
                coordenada1_1 = xl4_1
                coordenada1_2 = yl4_1
            if(a==5):
                coordenada1_1 = xl5_1
                coordenada1_2 = yl5_1
            if(a==6):
                coordenada1_1 = xl6_1
                coordenada1_2 = yl6_1
            if(a==7):
                coordenada1_1 = xl1_1
                coordenada1_2 = yl1_1
            if(a==8):
                coordenada1_1 = xl1_1
                coordenada1_2 = yl2_1

            ##xl9_1 = random.randint(339,408)
            ##yl9_1 = ((-0.06*xl9_1)-209)*-1

            ##xl10_1 = random.randint(408,469)
            ##yl10_1 = ((-1.3*xl10_1)+326)*-1

            ##xl11_1 = random.randint(469,520)
            ##yl11_1 = ((2.1*xl11_1)-1305)*-1


            xl1_2 = random.randint(520,566)
            yl1_2 = ((0.9*xl1_2)-698)*-1

            xl2_2 = random.randint(566,650)
            yl2_2 = ((-0.2*xl2_2)-48)*-1

            xl3_2 = random.randint(650,700)
            yl3_2 = ((0.7*xl3_2)-670)*-1

            xl4_2 = random.randint(700,756)
            yl4_2 = ((-0.3*xl4_2)+66)*-1

            xl5_2 = random.randint(756,800)
            yl5_2 = ((0.6*xl5_2)+643)*-1
            
            if(b==1):
                coordenada2_1 = xl1_2
                coordenada2_2 = yl1_2
            if(b==2):
                coordenada2_1 = xl2_2
                coordenada2_2 = yl2_2 
            if(b==3):
                coordenada2_1 = xl3_2
                coordenada2_2 = yl3_2
            if(b==4):
                coordenada2_1 = xl4_2
                coordenada2_2 = yl4_2 
            if(b==5):
                coordenada2_1 = xl5_2
                coordenada2_2 = yl5_2
            print(coordenada2_1,coordenada2_2,b)
            return coordenada1_1, coordenada1_2, coordenada2_1,coordenada2_2
        

    def validar_angulo(x):
        if x < 0 or x > 180:
            Opciones_validar_ang()
            while x < 0 or x > 180:
                print("ERROR, Angulo incorrecto")
                x = float(evento_angulo())
                
            return x    

        else:
            angulo_usuario = x
            return angulo_usuario   

    def validar_velocidad(y):
        if y < 0 or y > 250:
            Opciones_validar_vel()
            while y < 0 or y > 250:
                print("ERROR, Velocidad incorrecta")
                y = int(evento_velocidad())
                
            return y    

        else:
            velocidad_usuario = y
            return velocidad_usuario         

    def evento_angulo():
        salir = 0
        angulo_usuario = ''
        active = False
        while salir == 0:
            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN: #ANGULO
                    if Rect_izq_1.collidepoint(event.pos):
                        active = True
                    else:
                        active = False

                if event.type == pygame.KEYDOWN:
                    if active == True:
                        if event.key == pygame.K_BACKSPACE:
                            angulo_usuario = angulo_usuario[:-1]
                        if event.key == pygame.K_SPACE: ###########
                            salir = 1
                        else:
                            angulo_usuario += event.unicode

                text_surface = fuente_base.render(angulo_usuario, True,(0,0,0))
                VENTANA.blit(text_surface,(Rect_izq_1.x + 3, Rect_izq_1.y + 3))
                Rect_izq_1.w = max(100, text_surface.get_width() + 10)

                pygame.display.update()
                clock.tick(60)

        return angulo_usuario

    def evento_velocidad():
        salir = 0
        velocidad_usuario = ''
        active = False
        while salir == 0:
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN: #VELOCIDAD
                    if Rect_izq_2.collidepoint(event.pos):
                        active = True
                    else:
                        active = False

                if event.type == pygame.KEYDOWN:
                    if active == True:
                        if event.key == pygame.K_BACKSPACE:
                            velocidad_usuario = velocidad_usuario[:-1]
                        if event.key == pygame.K_SPACE: ###############
                            salir = 1
                        else:
                            velocidad_usuario += event.unicode

                text_surface = fuente_base.render(velocidad_usuario, True,(0,0,0))
                VENTANA.blit(text_surface,(Rect_izq_2.x + 3, Rect_izq_2.y + 3))
                Rect_izq_2.w = max(100, text_surface.get_width() + 10)

                pygame.display.update()
                clock.tick(60)

        return velocidad_usuario

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
            Tanques.Tanques.p1(VENTANA, x1_1, y1_2,seleccion_mapa) #permanecia de tanques p1
            Tanques.Tanques.p2(VENTANA, x2_1,y2_2,seleccion_mapa)
            vida = Tanques.Tanques.vida(VENTANA, vida, 0, 0)

        vida = Tanques.Tanques.vida(VENTANA, vida, 0, 0)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()  #Actualizacion ventana       
        InterfazJuego.InterfazJuego.altura_distancia()         

        if turno == 1:
            InterfazJuego.InterfazJuego.turno_jugador(turno)
            
            print("\nJUGADOR 1")
            InterfazJuego.InterfazJuego.marcadorJugador(VENTANA, 1, x1_1, y1_2)
            listaProyectiles, opcProyectil = InterfazJuego.InterfazJuego.menuProyectiles(VENTANA, x1_1+10, y1_2-190, listaProyectiles)
            print(listaProyectiles[opcProyectil][2])

            angulo_usuario, velocidad_usuario = evento_angulo(), evento_velocidad()
            velocidad, angulo = validar_velocidad(int(velocidad_usuario)), validar_angulo(float(angulo_usuario)) 
            angulo = Proyectil.Proyectil.grad_a_rad(angulo)
            posX_tanque, posY_tanque = ((x1_1+25), y1_2) # tanque emisor
            col_posxT, col_posyT = x2_1, y2_2 # tanque destino
            
            turno += 5 #no entrada
            cont += 1 #Contador de turnos
            t = 0
            
            alt_max = Altura_maximo(velocidad , angulo)
            print("ALTURA MAXIMA", alt_max)        

        time.sleep(0.002)
        t = t+0.02*10 #velocidad *5
        x, y = proyectil(t, velocidad, angulo, posX_tanque, posY_tanque-3)
        dMax = Distancia_maximo(posX_tanque , posY_tanque , x , y)
        
        ''' COLSIONES '''

        colision = check_colision(x, y, col_posxT, col_posyT)              # col_posxT, col_posyT = tanque destino
        colision_suicidio = check_colision(x, y, posX_tanque, posY_tanque) # posX_tanque, posY_tanque = tanque emisor
        if(colision == False): # cambiar_1 , line 460-488             
            elem_inciales(seleccion_mapa)
            Opciones_izq()            
            if(cont % 2 != 0):
                #turno 1
                turno = 2
            else:
                #turno 2
                turno = 1

        if(colision == True):       
            elem_inciales(seleccion_mapa)
            Opciones_izq()
            if(cont % 2 != 0):
                turno = 2
            else:
                turno = 1
            vida = Tanques.Tanques.vida(VENTANA, vida, listaProyectiles[opcProyectil][1], turno)
            pygame.display.update()
            #print("a ganado el jugador ", turno)
            #fin_juego = InterfazJuego.pantalla_ganador(VENTANA, turno)

        vida = Tanques.Tanques.vida(VENTANA, vida, 0, 0)
        pygame.display.update()

        if(colision_suicidio == True):      
            elem_inciales(seleccion_mapa)
            Opciones_izq()
            if(cont % 2 != 0):
                turno = 2
                id = 1
            else:
                turno = 1
                id = 2
            vida = Tanques.Tanques.vida(VENTANA, vida, listaProyectiles[opcProyectil][1], id)
            pygame.display.update()
            #print("a ganado el jugador ", turno)
            #fin_juego = InterfazJuego.pantalla_ganador(VENTANA, turno)
        
        if(vida[0] <= 0):
            fin_juego = InterfazJuego.InterfazJuego.pantalla_ganador(VENTANA, 2)
        if(vida[1] <= 0):
            fin_juego = InterfazJuego.InterfazJuego.pantalla_ganador(VENTANA, 1)

        if(fin_juego == 1):
            break

        ''' FIN COLISIONES '''

        Tanques.Tanques.p1(VENTANA, x1_1, y1_2,seleccion_mapa) #permanecia de tanques p1
        Tanques.Tanques.p2(VENTANA, x2_1, y2_2,seleccion_mapa)

        if turno == 2:
            InterfazJuego.InterfazJuego.turno_jugador(turno)
            
            print("\nJUGADOR 2")
            InterfazJuego.InterfazJuego.marcadorJugador(VENTANA, 1, x2_1, y2_2)
            listaProyectilesB, opcProyectil = InterfazJuego.InterfazJuego.menuProyectiles(VENTANA, x2_1+10, y2_2-190, listaProyectilesB)
            print(listaProyectiles[opcProyectil][2])

            InterfazJuego.InterfazJuego.marcadorJugador(VENTANA, 2, x2_1, y2_2)
            angulo_usuario, velocidad_usuario = evento_angulo(), evento_velocidad()
            velocidad, angulo = validar_velocidad(int(velocidad_usuario)), validar_angulo(float(angulo_usuario))
            angulo = Proyectil.Proyectil.grad_a_rad(angulo)
            posX_tanque, posY_tanque = ((x2_1+25), y2_2)    # pos(x,y) tanque emisor / x+25 = mitad del tanque
            col_posxT, col_posyT = (x1_1, y1_2)
            
            turno += 5 #condicion de no entrada
            cont += 1
            t = 0

            alt_max = Altura_maximo(velocidad , angulo)
            print("ALTURA MAXIMA", alt_max)
        InterfazJuego.InterfazJuego.dibujar_altura(alt_max)
        InterfazJuego.InterfazJuego.dibujar_distancia(dMax)            
        clock.tick(60)
