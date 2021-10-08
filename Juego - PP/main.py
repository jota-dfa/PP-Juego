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
GRIS =  (131,139,139)

fuente_base = pygame.font.Font(None,30)
texto_angulo = 'Angulo'
texto_velocidad = 'Velocidad'
seleccion_mapa = 1 #random.randint(1,3)
 
class Mapa():

    def __init__(self) -> None:
        pass
        
    def terreno(VENTANA,seleccion_mapa):
            
            if(seleccion_mapa==1):
                piso = pygame.image.load("imagenes/piso.png")
                VENTANA.blit(piso, (0, 0))

            if(seleccion_mapa==2):
                piso = pygame.image.load("imagenes/piso_2.png")
                VENTANA.blit(piso, (0, 20))

            if(seleccion_mapa==3):
                piso = pygame.image.load("imagenes/piso_3.png")
                VENTANA.blit(piso, (0, 20))

    def colisionBala_terreno(x, y, seleccion_mapa):
        if seleccion_mapa == 1:
            if x > 0 and x < 100:   #Recta 1
                a = ((-0.5*x-190)*-1)-y
                if a<-60:         
                    print("RECT 1")
                    return False            
            if x > 100 and x < 200: #Recta 2
                b = ((-240)*-1)-y
                if b<-60:         
                    print("RECT 2")
                    return False            
            if x > 200 and x < 300: #Recta 3
                c = ((0.9*x-420)*-1)-y
                if c<-60:         
                    print("RECT 3")
                    return False
            if x > 300 and x < 500: #Recta 4
                d = ((-0.3*x-60)*-1)-y
                if d<-60:         
                    print("RECT 4")
                    return False
            if x >550 and x < 800:  #Recta 5
                f = ((0.16*x-318)*-1)-y
                if f<-60:         
                    print("RECT 5")
                    return False

     
class Tanques():

    def __init__(self, coordenada1_1,coordenada1_2, x_proyect,y_proyect,a_posT,b_posT,seleccion_mapa):
        self.coordenada1_1 = coordenada1_1
        self.coordenada1_2 = coordenada1_2

        self.x_proyect = x_proyect
        self.y_proyect = y_proyect
        self.a_posT = a_posT
        self.b_posT = b_posT
        self.seleccion_mapa = seleccion_mapa
        

    def p1(VENTANA, coordenada1_1, coordenada1_2,seleccion_mapa): # b = random
        if(seleccion_mapa==1):
            tanque_1 = pygame.image.load("imagenes/tanque_1.png")
            VENTANA.blit(tanque_1, (coordenada1_1, coordenada1_2)) 

        if(seleccion_mapa==2):
            tanque_1 = pygame.image.load("imagenes/tanque_11.png")
            VENTANA.blit(tanque_1, (coordenada1_1, coordenada1_2))
        
        if(seleccion_mapa==3):
            tanque_1 = pygame.image.load("imagenes/tanque_111.png")
            VENTANA.blit(tanque_1, (coordenada1_1, coordenada1_2))
        

    def p2(VENTANA, b, y,seleccion_mapa): # a = random
        if(seleccion_mapa==1):
            tanque_2 = pygame.image.load("imagenes/tanque_2.png")
            VENTANA.blit(tanque_2, (b, y))
        if(seleccion_mapa==2):
            tanque_2 = pygame.image.load("imagenes/tanque_22.png")
            VENTANA.blit(tanque_2, (b, y))   
        if(seleccion_mapa==3):
            tanque_2 = pygame.image.load("imagenes/tanque_222.png")
            VENTANA.blit(tanque_2, (b, y))  

    def col_proyectil_tanque(x_proyect, y_proyect, a_posT, b_posT):
        if(x_proyect >= a_posT and x_proyect <= a_posT+60):
            if(y_proyect >= b_posT and y_proyect <= b_posT+35):
                #print("Ok_colison_proyectil_tanque")
                return True      

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

class InterfazJuego():
    
    def __init__(self) -> None:
        pass

    def pantalla_ganador(VENTANA, a):
        fondo = pygame.image.load("imagenes/fondo_ganador.jpg")
        VENTANA.blit(fondo, (0, 0))
        while a == 1:
            for event in pygame.event.get():
                pygame.draw.rect(VENTANA, GRIS, [295, 400 , 200, 250])   #P1
                Tanques.p1(VENTANA, 360, 365, seleccion_mapa)
                
                texto_ganador = fuente_base.render('Ganador - P1 ',True,(255,255,255))
                VENTANA.blit(texto_ganador,(330 , 440))

                if event.type == pygame.MOUSEBUTTONDOWN: #ANGULO
                    active = True
                else:
                    active = False

                if(active == True):
                    a += 10

                pygame.display.update()
        
        while a == 2:
            for event in pygame.event.get():
                pygame.draw.rect(VENTANA, GRIS, [295, 400 , 200, 250])   #P2
                Tanques.p2(VENTANA, 360, 365, seleccion_mapa)

                texto_ganador = fuente_base.render('Ganador - P2 ',True,(255,255,255))
                VENTANA.blit(texto_ganador,(330 , 440))
                
                if event.type == pygame.MOUSEBUTTONDOWN: #ANGULO
                    active = True
                else:
                    active = False

                if(active == True):
                    a += 10
                
                pygame.display.update()
        
        return 1

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
        Mapa.terreno(VENTANA,seleccion_mapa)
        #TANQUES
        #Tanques.p1(VENTANA)
        #Tanques.p2(VENTANA)

    elem_inciales(seleccion_mapa)
    Opciones_izq()

    ''' Fin elementos iniciales '''

    #PROYECTILES
    def proyectil(t, v, angl, posX, posY): # a,b posTanques
        tr_x, tr_y = Proyectil.pr_trayectoria(v, 9.8, t, angl, posX, posY)
        #colision_terreno = True
        colision_terreno = Proyectil.colision_terreno(tr_x, tr_y)
        Proyectil.dibu_proyectil(tr_x, tr_y, VENTANA)
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
        if(Proyectil.colision_terreno(x, y) == False):
            return False
        if(Mapa.colisionBala_terreno(x,y , seleccion_mapa) == False):
            print("DISTANCIA MAXIMA",dMax)
            return False
        if(Tanques.col_proyectil_tanque(x,y, a,b) == True):
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
    while turno != 0: #PRINCIPAL
        
        if cont == 0:
            x1_1, y1_2, x2_1, y2_2 = spawn_tanques(0,seleccion_mapa)
            Tanques.p1(VENTANA, x1_1, y1_2,seleccion_mapa) #permanecia de tanques p1
            Tanques.p2(VENTANA, x2_1,y2_2,seleccion_mapa)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()  #Actualizacion ventana

        if turno == 1:
            print("\nJUGADOR 1")
            angulo_usuario = evento_angulo()
            velocidad_usuario = evento_velocidad()
            velocidad = validar_velocidad(int(velocidad_usuario))
            angulo = validar_angulo(float(angulo_usuario)) 
            angulo = Proyectil.grad_a_rad(angulo)
            turno += 5 #no entrada
            cont += 1 #Contador de turnos
            t = 0
            posX_tanque = x1_1+25 # 2 pos tanques 1 def de proyectil
            posY_tanque = y1_2
            col_posxT, col_posyT = x2_1, y2_2 #tanque destino
            alt_max = Altura_maximo(velocidad , angulo)
            print("ALTURA MAXIMA", alt_max)        
        #t = pygame.time.get_ticks()/1000 #en segundos
        #t = t #5 veces mas rapido

        time.sleep(0.002)
        t = t+0.02*10 #velocidad *5
        x, y = proyectil(t, velocidad, angulo, posX_tanque, posY_tanque-3)
        dMax = Distancia_maximo(posX_tanque , posY_tanque , x , y)
        ''' COLSIONES '''

        colision = check_colision(x, y, col_posxT, col_posyT)              # col_posxT, col_posyT = tanque destino
        colision_suicidio = check_colision(x, y, posX_tanque, posY_tanque) # posX_tanque, posY_tanque = tanque emisor
        if(colision == False):
            turno = 0
            elem_inciales(seleccion_mapa)
            Opciones_izq()            
            if(cont % 2 != 0):
                turno += 2
            else:
                turno += 1
        if(colision == True):
            turno = 0         
            if(cont % 2 != 0):
                turno += 1
            else:
                turno += 2
            print("a ganado el jugador ", turno)
            fin_juego = InterfazJuego.pantalla_ganador(VENTANA, turno)
        if(colision_suicidio == True):
            turno = 0         
            if(cont % 2 != 0):
                turno += 2
            else:
                turno += 1
            print("a ganado el jugador ", turno)
            fin_juego = InterfazJuego.pantalla_ganador(VENTANA, turno)
        
        if(fin_juego == 1):
            break
        
        ''' FIN COLISIONES '''

        Tanques.p1(VENTANA, x1_1, y1_2,seleccion_mapa) #permanecia de tanques p1
        Tanques.p2(VENTANA, x2_1, y2_2,seleccion_mapa)

        if turno == 2:
            print("\nJUGADOR 2")
            angulo_usuario = evento_angulo()
            velocidad_usuario = evento_velocidad()
            velocidad = validar_velocidad(int(velocidad_usuario))
            angulo = validar_angulo(float(angulo_usuario))
            angulo = Proyectil.grad_a_rad(angulo)
            turno += 5 #condicion de no entrada
            cont += 1
            t = 0
            posX_tanque = x2_1+25 # 2 pos tanques 1 def de proyectil
            posY_tanque = y2_2
            col_posxT = x1_1
            col_posyT = y1_2
            alt_max = Altura_maximo(velocidad , angulo)
            print("ALTURA MAXIMA", alt_max)
        clock.tick(60)
