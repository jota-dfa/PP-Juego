import pygame
from pygame import event
from pygame.constants import MOUSEBUTTONDOWN
import Tanques

ALTO = 500
ANCHO = 800

pygame.font.init()

NEGRO = (0, 0, 0)
GRIS =  (131,139,139)
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
SALIR_IMAGEN = pygame.image.load("imagenes/salir.png").convert_alpha
seleccion_mapa = 1 #random.randint(1,3)
fuente_base = pygame.font.Font(None,30)

class InterfazJuego():

    def __init__(self) -> None:
        pass
    
    def botonReinicio():
        seguir = 1
        string = ''
        boton = pygame.image.load("imagenes/button_reset_n.png")
        VENTANA.blit(boton, (0, 0))
        boton_rectangulo = pygame.Rect([0, 0, 40, 40])
        pygame.display.update()
        while seguir == 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: #VELOCIDAD
                    if boton_rectangulo.collidepoint(event.pos):
                        boton = pygame.image.load("imagenes/button_reset_r.png")
                        VENTANA.blit(boton, (0, 0))
                        return 1
                    else:
                        boton = pygame.image.load("imagenes/button_reset_n.png")
                        VENTANA.blit(boton, (0, 0))
                if event.type == pygame.KEYDOWN: #cierra menu
                    string += event.unicode 
                    seguir = 0
                pygame.display.update()

    def botonSalir():
        seguir = 1
        string = ''
        boton_salir = 'salir'
        texto_B_salir = fuente_base.render(boton_salir,True,(0,0,0))
        boton_rect = pygame.Rect(740,10, 50,25)
        pygame.draw.rect(VENTANA,(255,255,255), boton_rect)
        VENTANA.blit(texto_B_salir, boton_rect)
        pygame.display.update()
        while seguir == 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: #VELOCIDAD
                    if boton_rect.collidepoint(event.pos):
                        pygame.quit()
                        return 1

                if event.type == pygame.KEYDOWN: #cierra menu
                    string += event.unicode 
                    seguir = 0
                pygame.display.update()  

    def marcadorJugador(VENTANA, a, posXT, posYT):
        if a == 1:
            marcadorP1 = pygame.image.load("imagenes/p1.png")
            VENTANA.blit(marcadorP1, (posXT+27, posYT-40))
        if a == 2:
            marcadorP2 = pygame.image.load("imagenes/p2.png")
            VENTANA.blit(marcadorP2, (posXT+27, posYT-40))

    def menuProyectiles(VENTANA, posXTanque, posYTanque, listaProyectiles):
        
        fuente = pygame.font.SysFont("century gothic", 15)
        
        """Rect1 =  pygame.Rect( posXTanque+30, posYTanque, 600, 25)
        Rect2 =  pygame.Rect( posXTanque+30, posYTanque+40, 600, 25)
        Rect3 =  pygame.Rect( posXTanque+30, posYTanque+80, 600, 25)
        
        texto1 = fuente.render("Proyectil: ", True,(255,255,255))
        texto2 = fuente.render("Cantidad: ", True,(255,255,255))
        texto3 = fuente.render("Daño: ", True,(255,255,255))

        VENTANA.blit(texto1,(Rect1.x + 100 , Rect1.y + 0))
        VENTANA.blit(texto2,(Rect2.x + 100 , Rect2.y + 0))
        VENTANA.blit(texto3,(Rect3.x + 100 , Rect3.y + 0))"""
        
        #img_mp = pygame.image.load("imagenes/menu_proyectiles.png")
        #VENTANA.blit(img_mp, (50, 100))
        pygame.draw.rect(VENTANA, NEGRO, [posXTanque, posYTanque, 40, 120],2)
        #pygame.draw.rect(VENTANA, GRIS, [((posXTanque)+5), posYTanque+5, 30, 110])
        
        #pygame.draw.rect(VENTANA, BLANCO, [posXTanque+5, posYTanque+5, 30, 35])
        #pygame.draw.rect(VENTANA, CELESTE, [posXTanque+5, posYTanque+40, 30, 40])
        #pygame.draw.rect(VENTANA, CAFE, [posXTanque+5, posYTanque+80, 30, 35])

        m1 = pygame.image.load("imagenes/1_menuProyectiles.png")
        VENTANA.blit(m1, (posXTanque+5, posYTanque+5))
        m2 = pygame.image.load("imagenes/2_menuProyectiles.png")
        VENTANA.blit(m2, (posXTanque+5, posYTanque+40))
        m3 = pygame.image.load("imagenes/3_menuProyectiles.png")
        VENTANA.blit(m3, (posXTanque+5, posYTanque+80))

        opc_a = pygame.Rect([posXTanque, posYTanque, 40, 40])
        opc_b = pygame.Rect([posXTanque, posYTanque+40, 40, 40])
        opc_c = pygame.Rect([posXTanque, posYTanque+80, 40, 40])

        previo = ''
        seguir = 1
        mouseX, mouseY = pygame.mouse.get_pos()
        opc = 0
        while seguir == 1:
        
            for event in pygame.event.get():
               
                if event.type == pygame.MOUSEBUTTONDOWN: #VELOCIDAD
                    if opc_a.collidepoint(event.pos): 
                        
                        active = True
                        opc = 1
                        if listaProyectiles[opc][2] > 0:
                        #print("Proyectil: ",listaProyectiles[opc][0], "\nCantidad: ", listaProyectiles[opc][2], "\nDaño: ", listaProyectiles[opc][1])
                        
                            m1 = pygame.image.load("imagenes/1_menuProyectiles_2.png")
                            VENTANA.blit(m1, (posXTanque+5, posYTanque+5))
                            m2 = pygame.image.load("imagenes/2_menuProyectiles.png")
                            VENTANA.blit(m2, (posXTanque+5, posYTanque+40))
                            m3 = pygame.image.load("imagenes/3_menuProyectiles.png")
                            VENTANA.blit(m3, (posXTanque+5, posYTanque+80))

                            Rect1 =  pygame.Rect( posXTanque+30, posYTanque, 600, 25)
                            Rect2 =  pygame.Rect( posXTanque+30, posYTanque+40, 600, 25)
                            Rect3 =  pygame.Rect( posXTanque+30, posYTanque+80, 600, 25)
                            
                            texto1 = fuente.render("Proyectil: "+ str(listaProyectiles[opc][0]), True,(255,255,255),0)
                            texto2 = fuente.render("Cantidad: "+ str(listaProyectiles[opc][2]), True,(255,255,255),0)
                            texto3 = fuente.render("Daño: "+ str(listaProyectiles[opc][1]),True,(255,255,255),0)

                            VENTANA.blit(texto1,(Rect1.x + 25 , Rect1.y + 10))
                            VENTANA.blit(texto2,(Rect2.x + 25 , Rect2.y + 10))
                            VENTANA.blit(texto3,(Rect3.x + 25 , Rect3.y + 10))

                            pygame.display.update()
                        else:

                            Rect1 =  pygame.Rect( posXTanque+30, posYTanque, 600, 25)
                            Rect2 =  pygame.Rect( posXTanque+30, posYTanque+40, 600, 25)
                            Rect3 =  pygame.Rect( posXTanque+30, posYTanque+80, 600, 25)
                            
                            texto1 = fuente.render("Proyectil: "+ str(listaProyectiles[opc][0]), True,(255,255,255),0)
                            texto2 = fuente.render("Cantidad: "+ str(listaProyectiles[opc][2]), True,(255,0,0),0)
                            texto3 = fuente.render("Daño: "+ str(listaProyectiles[opc][1]),True,(255,255,255),0)

                            VENTANA.blit(texto1,(Rect1.x + 25 , Rect1.y + 10))
                            VENTANA.blit(texto2,(Rect2.x + 25 , Rect2.y + 10))
                            VENTANA.blit(texto3,(Rect3.x + 25 , Rect3.y + 10))

                            opc = 0
                        
                    if opc_b.collidepoint(event.pos): 
                        active = True
                        opc = 2
                        if listaProyectiles[opc][2] > 0:
                        #print("Proyectil: ",listaProyectiles[opc][0], "\nCantidad: ", listaProyectiles[opc][2], "\nDaño: ", listaProyectiles[opc][1])
                        
                            m2 = pygame.image.load("imagenes/2_menuProyectiles_2.png")
                            VENTANA.blit(m2, (posXTanque+5, posYTanque+40))
                            m1 = pygame.image.load("imagenes/1_menuProyectiles.png")
                            VENTANA.blit(m1, (posXTanque+5, posYTanque+5))
                            m3 = pygame.image.load("imagenes/3_menuProyectiles.png")
                            VENTANA.blit(m3, (posXTanque+5, posYTanque+80))

                            Rect1 =  pygame.Rect( posXTanque+30, posYTanque, 600, 25)
                            Rect2 =  pygame.Rect( posXTanque+30, posYTanque+40, 600, 25)
                            Rect3 =  pygame.Rect( posXTanque+30, posYTanque+80, 600, 25)
                            
                            texto1 = fuente.render("Proyectil: "+ str(listaProyectiles[opc][0]), True,(255,255,255),0)
                            texto2 = fuente.render("Cantidad: "+ str(listaProyectiles[opc][2]), True,(255,255,255),0)
                            texto3 = fuente.render("Daño: "+ str(listaProyectiles[opc][1]),True,(255,255,255),0)

                            VENTANA.blit(texto1,(Rect1.x + 25 , Rect1.y + 10))
                            VENTANA.blit(texto2,(Rect2.x + 25 , Rect2.y + 10))
                            VENTANA.blit(texto3,(Rect3.x + 25 , Rect3.y + 10))

                            pygame.display.update()
                        else:

                            Rect1 =  pygame.Rect( posXTanque+30, posYTanque, 600, 25)
                            Rect2 =  pygame.Rect( posXTanque+30, posYTanque+40, 600, 25)
                            Rect3 =  pygame.Rect( posXTanque+30, posYTanque+80, 600, 25)
                            
                            texto1 = fuente.render("Proyectil: "+ str(listaProyectiles[opc][0]), True,(255,255,255),0)
                            texto2 = fuente.render("Cantidad: "+ str(listaProyectiles[opc][2]), True,(255,0,0),0)
                            texto3 = fuente.render("Daño: "+ str(listaProyectiles[opc][1]),True,(255,255,255),0)

                            VENTANA.blit(texto1,(Rect1.x + 25 , Rect1.y + 10))
                            VENTANA.blit(texto2,(Rect2.x + 25 , Rect2.y + 10))
                            VENTANA.blit(texto3,(Rect3.x + 25 , Rect3.y + 10))

                            opc = 0
                    
                    if opc_c.collidepoint(event.pos): 

                        active = True
                        opc = 3
                        if listaProyectiles[opc][2] > 0:
                        #print("Proyectil: ",listaProyectiles[opc][0], "\nCantidad: ", listaProyectiles[opc][2], "\nDaño: ", listaProyectiles[opc][1])
                        
                            m3 = pygame.image.load("imagenes/3_menuProyectiles_2.png")
                            VENTANA.blit(m3, (posXTanque+5, posYTanque+80))
                            m1 = pygame.image.load("imagenes/1_menuProyectiles.png")
                            VENTANA.blit(m1, (posXTanque+5, posYTanque+5))
                            m2 = pygame.image.load("imagenes/2_menuProyectiles.png")
                            VENTANA.blit(m2, (posXTanque+5, posYTanque+40))

                            Rect1 =  pygame.Rect( posXTanque+30, posYTanque, 600, 25)
                            Rect2 =  pygame.Rect( posXTanque+30, posYTanque+40, 600, 25)
                            Rect3 =  pygame.Rect( posXTanque+30, posYTanque+80, 600, 25)
                            
                            texto1 = fuente.render("Proyectil: "+ str(listaProyectiles[opc][0]), True,(255,255,255),0)
                            texto2 = fuente.render("Cantidad: "+ str(listaProyectiles[opc][2]), True,(255,255,255),0)
                            texto3 = fuente.render("Daño: "+ str(listaProyectiles[opc][1]),True,(255,255,255),0)

                            VENTANA.blit(texto1,(Rect1.x + 25 , Rect1.y + 10))
                            VENTANA.blit(texto2,(Rect2.x + 25 , Rect2.y + 10))
                            VENTANA.blit(texto3,(Rect3.x + 25 , Rect3.y + 10))

                            pygame.display.update()
                        else:

                            Rect1 =  pygame.Rect( posXTanque+30, posYTanque, 600, 25)
                            Rect2 =  pygame.Rect( posXTanque+30, posYTanque+40, 600, 25)
                            Rect3 =  pygame.Rect( posXTanque+30, posYTanque+80, 600, 25)
                            
                            texto1 = fuente.render("Proyectil: "+ str(listaProyectiles[opc][0]), True,(255,255,255),0)
                            texto2 = fuente.render("Cantidad: "+ str(listaProyectiles[opc][2]), True,(255,0,0),0)
                            texto3 = fuente.render("Daño: "+ str(listaProyectiles[opc][1]),True,(255,255,255),0)

                            VENTANA.blit(texto1,(Rect1.x + 25 , Rect1.y + 10))
                            VENTANA.blit(texto2,(Rect2.x + 25 , Rect2.y + 10))
                            VENTANA.blit(texto3,(Rect3.x + 25 , Rect3.y + 10))

                            opc = 0

                    else:
                        active = False
                            
                #if event.type == pygame.KEYUP:
                if event.type == pygame.KEYDOWN: #cierra menu
                    previo = event.unicode 
                    active = True
                else:
                    active = False

                if(previo == 'i' and active == True): # Resta 1 a total c/ proyectil
                    print("se cierra menu")
                    pygame.display.update()
                    seguir += 10
                    
                pygame.display.update()

        return listaProyectiles, opc

    def pantalla_ganador(VENTANA, a):
        
        fondo = pygame.image.load("imagenes/fondo_ganador.jpg")
        VENTANA.blit(fondo, (0, 0))
        while a == 1:
            for event in pygame.event.get():
                pygame.draw.rect(VENTANA, GRIS, [295, 400 , 200, 250])   #P1
                Tanques.Tanques.p1(VENTANA, 360, 365, seleccion_mapa)
                
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
                Tanques.Tanques.p2(VENTANA, 360, 365, seleccion_mapa)

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

    def altura_distancia():
        Fuente = pygame.font.Font(None,30)
        altura = 'Altura:                m '
        distancia = 'Distancia:                m'
        texto_altura = Fuente.render(altura,True,(0,0,0))
        texto_distancia = Fuente.render(distancia,True,(0,0,0))
        Rect =  pygame.Rect( 100, 425, 600, 25)
        pygame.draw.rect(VENTANA, (255,255,255),( 100, 425, 600, 25))
        VENTANA.blit(texto_altura,(Rect.x + 10 , Rect.y + 0))
        VENTANA.blit(texto_distancia,(Rect.x + 350,Rect.y + 0))

    def dibujar_altura(altura_maxima):
        Rect =  pygame.Rect( 100, 425, 600, 25)
        x = int(altura_maxima)
        altura = str(x)
        txt_altura = fuente_base.render(altura,True,(0,0,0))
        VENTANA.blit(txt_altura,(Rect.x + 100 , Rect.y + 0))

    def dibujar_distancia(distancia_maxima):
        Rect =  pygame.Rect( 100, 425, 600, 25)
        x = int(distancia_maxima)
        distancia = str(x)
        txt_distancia = fuente_base.render(distancia,True,(0,0,0))
        VENTANA.blit(txt_distancia,(Rect.x + 500 , Rect.y + 0))

    def turno_jugador(jugador):
        Rect =  pygame.Rect(0,460, 50,25)
        jugador = str(jugador)
        txt_jugadores_general = 'Jugador'
        jugadores = fuente_base.render(txt_jugadores_general,True,(0,0,0))
        txt_jugador = fuente_base.render(jugador,True,(0,0,0))
        VENTANA.blit(txt_jugador,(Rect.x + 410 , Rect.y + 0))
        VENTANA.blit(jugadores,(Rect.x + 300 , Rect.y + 0))


        