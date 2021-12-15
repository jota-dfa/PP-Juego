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
seleccion_mapa = random.randint(1,3)

def Juego(g, viento_activo, Lista_proyectiles):
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
        # MAPA
        Mapa.Mapa.terreno(VENTANA,seleccion_mapa)
    
    def elem_iniciales2(seleccion_mapa):
        Mapa.Mapa.terreno2(VENTANA, seleccion_mapa)


    elem_inciales(seleccion_mapa)
    Opciones_izq()

    ''' Fin elementos iniciales '''

    #PROYECTILES
    def proyectil(t, v, angl, posX, posY): # a,b posTanques
        tr_x, tr_y = Proyectil.Proyectil.pr_trayectoria(v,g, t, angl, posX, posY)
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
        if(Proyectil.Proyectil.colision_terreno(x, y) == False): # Lim. laterales e inferior
            return False
        if(Mapa.Mapa.colisionBala_terreno(x,y , seleccion_mapa, cont) == False): 
            print("DISTANCIA MAXIMA",dMax)
            return False
        if(Tanques.Tanques.col_proyectil_tanque(x,y, a,b) == True):
            return True


    def spawn_tanques(mov_y,seleccion_mapa): #animacion , escalar con un arreglo de randoms
        if(seleccion_mapa==1):
            a = random.randint(1,4)
            b = random.randint(1,4)
            
            xl1_1=random.randint(70,100)
            yl1_1=((0.01*xl1_1)-122)*-1
            xl2_1=random.randint(100,150)     
            yl2_1=((-0.4*xl2_1)-89)*-1 
                              
            ##xl3_1=random.randint(150,118)##rara
            ##yl3_1=((1.7*xl3_1)-413)*-1
               
            xl3_1=random.randint(118,170)
            yl3_1=((-0.2*xl3_1)-162)*-1

            xl4_1=random.randint(180,228)
            yl4_1=((-0.5*xl4_1)-113)*-1

            #xl5_1=random.randint(228,248)
            #yl5_1=((-3.5*xl5_1)+551)*-1

            xl6_1=random.randint(248,300)
            yl6_1=((1.4*xl6_1)-666)*-1

            if(a==1):
                coordenada1_1 = xl1_1
                coordenada1_2 = yl1_1
            if(a==2):
                coordenada1_1 = xl2_1
                coordenada1_2 = yl2_1
            if(a==3):
                coordenada1_1 = xl3_1
                coordenada1_2 = yl3_1
            if(a==4):
                coordenada1_1 = xl4_1
                coordenada1_2 = yl4_1
            
     
        ########
            ##xl8_1=random.randint(300,366)
            ##yl8_1=((0.7*xl8_1)-461)*-1
            
            ##xl9_1=random.randint(366,401)
            ##yl9_1=((1.1*xl9_1)-608)*-1

            ##xl10_1=random.randint(401,449)
            ##yl10_1=((0.1*xl10_1)-211)*-1

            ##xl11_1=random.randint(449,504)
            ##yl11_1=((-1.1*xl11_1)+338)*-1

            xl1_2=random.randint(504,593)
            yl1_2=((-0.6*xl1_2)+90)*-1

            xl2_2=random.randint(593,653)
            yl2_2=((0.8*xl2_2)-701)*-1

            ##xl2_2=random.randint(663,610)##########rara
            ##yl2_2=((-1.0*xl2_2)+507)*-1

            xl3_2=random.randint(610,701)
            yl3_2=((0.2*xl3_2)-251)*-1

            xl4_2=random.randint(701,770)
            yl4_2=((-0.009*xl4_2)-105)*-1
            
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

            
            return coordenada1_1, coordenada1_2, coordenada2_1,coordenada2_2
        if(seleccion_mapa==2):
            a = random.randint(1,4)
            b = random.randint(1,4)
            
            xl1_1 = random.randint(0,74)
            yl1_1 = (1.3*xl1_1-250)*-1
            
            xl2_1 =random.randint(74,150)
            yl2_1=((-1.3*xl2_1)-54)*-1

            xl3_1 = random.randint(150,250)
            yl3_1 = 250

            xl4_1 = random.randint(250,300)
            yl4_1 = xl4_1

            ##xl5_1 = random.randint(300,350)
            ##yl5_1 = (xl5_1 - 600)*-1

            ##xl6_1 = random.randint(350,390)
            ##yl6_1 = 250

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
           
            #################
            

            ##xl1_2 = random.randint(400,450)
            ##yl1_2 = 250

            ##xl2_2 = random.randint(450,500)
            ##yl2_2 = (-xl2_2 + 200)*-1   

            xl1_2 = random.randint(500,550)
            yl1_2 = (xl1_2 -800)*-1
            
            xl2_2 = random.randint(550,650)
            yl2_2 = 250
            
            xl3_2 = random.randint(650,725)
            yl3_2 = ((1.3*xl3_2)-1090)*-1
        
            xl4_2 = random.randint(725,800)
            yl4_2 = ((-1.3*xl4_2)+800)*-1

             
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
            return coordenada1_1, coordenada1_2, coordenada2_1,coordenada2_2
        if(seleccion_mapa==3):
            a = random.randint(1,5)
            b = random.randint(1,4)

            xl1_1 = random.randint(10,24)
            yl1_1 = ((0.3*xl1_1)-186)*-1

            xl2_1 = random.randint(48,49)
            yl2_1 = ((-5.4*xl2_1)+47)*-1

            xl3_1 = random.randint(49,90)
            yl3_1 = ((-0.5*xl3_1)-200)*-1

            xl4_1 = random.randint(100,119)
            yl4_1 = ((-1.9*xl4_1)-69)*-1

            xl5_1 = random.randint(179,190)
            yl5_1 = ((2.6*xl5_1)-745)*-1

            xl6_1 = random.randint(190,253)
            yl6_1 = ((0.6*xl6_1)-349)*-1

            #xl7_1 = random.randint(253,283)
            #yl7_1 = ((1.5*xl7_1)-581)*-1

            ##xl8_1 = random.randint(283,339)
            ##yl8_1 = ((-1.5*xl8_1)+289)*-1

            if(a==1):
                coordenada1_1 = xl1_1
                coordenada1_2 = yl1_1-20
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
            
            ##xl9_1 = random.randint(339,408)
            ##yl9_1 = ((-0.06*xl9_1)-209)*-1

            ##xl10_1 = random.randint(408,469)
            ##yl10_1 = ((-1.3*xl10_1)+326)*-1

            ##xl11_1 = random.randint(469,520)
            ##yl11_1 = ((2.1*xl11_1)-1305)*-1


            xl1_2 = random.randint(520,560)
            yl1_2 = ((0.9*xl1_2)-672)*-1

            xl2_2 = random.randint(566,650)
            yl2_2 = ((-0.2*xl2_2)-58)*-1

            xl3_2 = random.randint(650,700)
            yl3_2 = ((0.7*xl3_2)-640)*-1

            xl4_2 = random.randint(700,736)
            yl4_2 = ((-0.3*xl4_2)+46)*-1

            ##xl5_2 = random.randint(756,760)
            ##yl5_2 = ((0.6*xl5_2)+643)*-1
            
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
          
            print(coordenada2_1,coordenada2_2,b)
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
                                angulo_usuario = angulo_usuario[0:-1]
                            else:
                                angulo_usuario += event.unicode

                        if active2 == True:
                            if event.key == pygame.K_BACKSPACE:
                                velocidad_usuario = velocidad_usuario[0:-1]
                            else:
                                velocidad_usuario += event.unicode

                    if previo == 'i':
                        listaProyectiles, opcProyectil = InterfazJuego.InterfazJuego.menuProyectiles(VENTANA, xEmisor, yEmisor, listaProyectiles)
                        elem_iniciales2(seleccion_mapa)
                        Opciones_izq()
                        if turno == 1:
                            Tanques.Tanques.p1(VENTANA, posxEmisor, posyEmisor,seleccion_mapa) #permanecia de tanques p1
                            Tanques.Tanques.p2(VENTANA, posxDestino, posyDestino,seleccion_mapa)
                        if turno == 2:
                            Tanques.Tanques.p2(VENTANA, posxEmisor, posyEmisor,seleccion_mapa) #permanecia de tanques p1
                            Tanques.Tanques.p1(VENTANA, posxDestino, posyDestino,seleccion_mapa)
                        InterfazJuego.InterfazJuego.marcadorJugador(VENTANA, turno, posxEmisor, posyEmisor)
                        Tanques.Tanques.vida(VENTANA, vida, 0, 0)
                        InterfazJuego.InterfazJuego.turno_jugador(turno)
                        InterfazJuego.InterfazJuego.altura_distancia()

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
        return 0, angulo_usuario, velocidad_usuario, posxEmisor, posyEmisor, posxDestino, posyDestino, listaProyectiles, opcProyectil
                 

    turno = 1
    cont = 0
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
    vida = [100, 100]

   

    while turno != 0: #PRINCIPAL

        if cont == 0:
            x1_1, y1_2, x2_1, y2_2 = spawn_tanques(0,seleccion_mapa)
            Tanques.Tanques.p1(VENTANA, x1_1, y1_2,seleccion_mapa) #permanecia de tanques p1
            Tanques.Tanques.p2(VENTANA, x2_1,y2_2,seleccion_mapa)
            vida = Tanques.Tanques.vida(VENTANA, vida, 0, 0)

        vida = Tanques.Tanques.vida(VENTANA, vida, 0, 0)
        pygame.display.update()

        pygame.display.update()  #Actualizacion ventana       
        InterfazJuego.InterfazJuego.altura_distancia()         
        #InterfazJuego.InterfazJuego.botonSalir() ##################

        if turno == 1:
            print("\nJUGADOR 1")
            #fin_juego, angulo_usuario, velocidad_usuario, posxEmisor, posyEmisor, posxDestino, posyDestino
            InterfazJuego.InterfazJuego.marcadorJugador(VENTANA, 1, x1_1, y1_2)
            fin_juego, angulo, velocidad, posX_tanque, posY_tanque, col_posxT, col_posyT, listaProyectiles, opcProyectil = turno_1(x1_1, y1_2, x2_1, y2_2, listaProyectiles, 1)
            
            t = 0
            alt_max = Altura_maximo(velocidad , angulo)
            turno += 5 #no entrada
            cont += 1 #Contador de turnos
            
        time.sleep(0.002)
        t = t+0.02*10 #velocidad *5
        x, y = proyectil(t, velocidad, angulo, posX_tanque, posY_tanque-3)
        dMax = Distancia_maximo(posX_tanque , posY_tanque , x , y)
        InterfazJuego.InterfazJuego.dibujar_altura(alt_max)
        InterfazJuego.InterfazJuego.dibujar_distancia(dMax)
        
        
        ''' COLSIONES '''

        colision = check_colision(x, y, col_posxT, col_posyT)              # col_posxT, col_posyT = tanque destino
        colision_suicidio = check_colision(x, y, posX_tanque, posY_tanque) # posX_tanque, posY_tanque = tanque emisor
        if(colision == False): # cambiar_1 , line 460-488   ## == false , toco terreno         
                     
            if(cont % 2 != 0): # opcProyectil
                #turno 1
                Mapa.Mapa.destruccionMapa(VENTANA, x, y, seleccion_mapa, cont)
                turno = 2
            else:
                #turno 2
                Mapa.Mapa.destruccionMapa(VENTANA, x, y, seleccion_mapa, cont)
                turno = 1
            elem_iniciales2(seleccion_mapa)
            Opciones_izq()   

        if(colision == True):     # == false , toco tanque   
            elem_iniciales2(seleccion_mapa)
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
            elem_iniciales2(seleccion_mapa)
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

        InterfazJuego.InterfazJuego.turno_jugador(turno)
        InterfazJuego.InterfazJuego.altura_distancia()

        if turno == 2:
            print("\nJUGADOR 2")
            InterfazJuego.InterfazJuego.marcadorJugador(VENTANA, 2, x2_1, y2_2)
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
