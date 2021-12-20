import pygame, sys
import main
import main_2


Reloj = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Scorched World')
texto_usuario_jugadores = '9.8'
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
    def jugadores():
        texto_ventana = 'Introduzca la cantidad de jugadores'
        texto_usuario_jugadores = ''
        int_jugadores = 0
        Boton_jugadores = pygame.Rect(300, 200, 200, 50)
        correr = True
        while correr:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_BACKSPACE:
                        texto_usuario_jugadores = texto_usuario_jugadores[0:-1]

                    else:    
                        texto_usuario_jugadores += event.unicode
                    
                    if event.key == pygame.K_SPACE:
                        int_jugadores = int(texto_usuario_jugadores)
                        correr = False


            VENTANA.fill((0,0,0)) 
            pygame.draw.rect(VENTANA, (255, 255,255), Boton_jugadores,1)           
            texto_jugadores = FUENTE.render(texto_usuario_jugadores,True,(255,255,255))
            texto_ventana_inter = FUENTE.render(texto_ventana,True,(255,255,255))
            VENTANA.blit(texto_ventana_inter,(250,100))
            VENTANA.blit(texto_jugadores,Boton_jugadores)
            pygame.display.update()
            Reloj.tick(60)

        return int_jugadores 

    def municiones(): 
        bala_int_60mm = 3
        bala_int_105mm = 6
        bala_int_perfor = 5 
        lista_proyectil = [bala_int_60mm,bala_int_perfor,bala_int_105mm]
        click = False
        correr = True
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
                    ejecutar = True
                    texto_bala_60mm = ''
                    bala_int_60mm =0
                    while ejecutar:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                previo = event.unicode
                                if previo != ' ':

                                    if event.key == pygame.K_BACKSPACE:
                                        texto_bala_60mm = texto_bala_60mm[0:-1]

                                    else:    
                                        texto_bala_60mm += event.unicode 
                                    
                                else:
                                    bala_int_60mm = int(texto_bala_60mm)
                                    ejecutar = False


                
                        texto_bala1 = FUENTE.render(texto_bala_60mm,True,(255,255,255))
                        VENTANA.blit(texto_bala1,bala_1)
                        pygame.display.update()
                        Reloj.tick(60)
                    print("60mm: ", bala_int_60mm)
                    

            if bala_2.collidepoint((mx, my)):
                if click:
                    texto_bala_perfor = ''
                    bala_int_perfor =0
                    ejecutar2= True
                    while ejecutar2:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                previo = event.unicode
                                if previo != ' ':

                                    if event.key == pygame.K_BACKSPACE:
                                        texto_bala_perfor = texto_bala_perfor[0:-1]

                                    else:    
                                        texto_bala_perfor += event.unicode 
                                    
                                else:
                                    bala_int_perfor = int(texto_bala_perfor)
                                    ejecutar2 = False


                
                        texto_bala2 = FUENTE.render(texto_bala_perfor,True,(255,255,255))
                        VENTANA.blit(texto_bala2,bala_2)
                        pygame.display.update()
                        Reloj.tick(60)                
                    print("Proyectil perforante: ", bala_int_perfor)

            if bala_3.collidepoint((mx, my)):
                if click:
                    texto_bala_105mm = ''
                    bala_int_105mm =0
                    ejecutar2= True
                    while ejecutar2:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                previo = event.unicode
                                if previo != ' ':

                                    if event.key == pygame.K_BACKSPACE:
                                        texto_bala_105mm = texto_bala_105mm[0:-1]

                                    else:    
                                        texto_bala_105mm += event.unicode 
                                    
                                else:
                                    bala_int_105mm = int(texto_bala_105mm)
                                    ejecutar2 = False


                
                        texto_bala3 = FUENTE.render(texto_bala_105mm,True,(255,255,255))
                        VENTANA.blit(texto_bala3,bala_3)
                        pygame.display.update()
                        Reloj.tick(60)                
                    print("Proyectil 105mm: ", bala_int_105mm)

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        correr = False
                        return lista_proyectil   
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            lista_proyectil = [bala_int_60mm, bala_int_perfor, bala_int_105mm]
            pygame.display.update()
            Reloj.tick(60)
        return  lista_proyectil

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

    def viento_activo():
        click = False
        correr = True
        while correr:
            VENTANA.fill((0,0,0))
            Boton_viento_activo = pygame.Rect(150, 350, 200, 50)
            Boton_viento_desactivado = pygame.Rect(450, 350, 200, 50)
            mx, my = pygame.mouse.get_pos()
            Dibujar_texto('Activar', FUENTE, (255, 255, 255), VENTANA, 210, 360)
            Dibujar_texto('Desactivar', FUENTE, (255, 255, 255), VENTANA, 460, 360)
            if Boton_viento_activo.collidepoint((mx, my)):
                if click:
                    print("Viento: Activado--")
                    v = 1 

            if Boton_viento_desactivado.collidepoint((mx, my)):
                if click:
                    print("Viento: Desactivado--")
                    v = 0 

            pygame.draw.rect(VENTANA, (255, 255,255), Boton_viento_activo,1)
            pygame.draw.rect(VENTANA, (255, 255,255), Boton_viento_desactivado,1)   

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        correr = False

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True 
            
        
            pygame.display.update()
            Reloj.tick(60)
        return v

    def gravedad():
        texto_ventana = 'Introduzca la gravedad'
        texto_usuario_jugadores = ''
        float_gravedad = 0.0
        Boton_gravedad = pygame.Rect(300, 200, 200, 50)
        correr = True
        while correr:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_BACKSPACE:
                        texto_usuario_jugadores = texto_usuario_jugadores[0:-1]

                    else:    
                        texto_usuario_jugadores += event.unicode
                    
                    if event.key == pygame.K_SPACE:
                        float_gravedad = float(texto_usuario_jugadores)
                        correr = False
                    if event.key == K_ESCAPE:
                        Opciones()

            VENTANA.fill((0,0,0)) 
            pygame.draw.rect(VENTANA, (255, 255,255), Boton_gravedad,1)           
            texto_gravedad = FUENTE.render(texto_usuario_jugadores,True,(255,255,255))
            texto_ventana_inter = FUENTE.render(texto_ventana,True,(255,255,255))
            VENTANA.blit(texto_ventana_inter,(270,100))
            VENTANA.blit(texto_gravedad,Boton_gravedad)
            pygame.display.update()
            Reloj.tick(60)

        return float_gravedad


    lista_elementos=[0,3,5,3,9.8,0,2]
    click = False
    correr = True
    while correr:
        VENTANA.fill((0,0,0))
        Boton_gravedad = pygame.Rect(300, 350, 200, 50) 
        Boton_viento = pygame.Rect(300, 450, 200, 50) 
        Boton_pantalla = pygame.Rect(300, 50, 200, 50)
        Boton_municiones = pygame.Rect(300, 150, 200, 50)
        Boton_jug = pygame.Rect(300, 250, 200, 50)
        mx, my = pygame.mouse.get_pos()
        Dibujar_texto('Opciones', FUENTE, (255, 255, 255), VENTANA, 20, 20)
        Dibujar_texto('Pantalla', FUENTE, (255, 255, 255), VENTANA, 310, 60) 
        Dibujar_texto('Municiones', FUENTE, (255,255,255),VENTANA, 310, 160)
        Dibujar_texto('Jugadores', FUENTE, (255, 255, 255), VENTANA, 310, 260) 
        Dibujar_texto('Gravedad', FUENTE, (255,255,255),VENTANA, 310, 360)
        Dibujar_texto('Viento', FUENTE, (255, 255, 255), VENTANA, 310, 460) 

        if Boton_pantalla.collidepoint((mx, my)):
            if click:
                ventana = pantalla()
                lista_elementos[0] = ventana
        if Boton_municiones.collidepoint((mx, my)):
            if click:
                lista_proyectiles1 = municiones()
                lista_elementos[1] = lista_proyectiles1[0]
                lista_elementos[2] = lista_proyectiles1[1]
                lista_elementos[3] = lista_proyectiles1[2]

        if Boton_jug.collidepoint((mx, my)):
            if click:
               lista_elementos[6] = jugadores()
                
        if Boton_gravedad.collidepoint((mx,my)):
            if click:
                gravedad_inter = gravedad()
                lista_elementos[4] =gravedad_inter
        if Boton_viento.collidepoint((mx,my)):
            if click:
                viento_inter = viento_activo()
                lista_elementos[5] = viento_inter

        pygame.draw.rect(VENTANA, (255, 255,255), Boton_pantalla,1)
        pygame.draw.rect(VENTANA, (255, 255,255), Boton_municiones,1)
        pygame.draw.rect(VENTANA, (255, 255,255), Boton_jug,1)
        pygame.draw.rect(VENTANA, (255, 255,255), Boton_gravedad,1)
        pygame.draw.rect(VENTANA, (255, 255,255), Boton_viento,1)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    Menu_principal(lista_elementos)

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 
        pygame.display.update()
        Reloj.tick(60) 


def Menu_principal(lista_elementos):

    click = False
    while True:
        ventana = lista_elementos[0]
        Lista_proyect = [lista_elementos[1],lista_elementos[2],lista_elementos[3]]
        g = lista_elementos[4]
        v = lista_elementos[5]
        jugadores = lista_elementos[6]

        VENTANA.fill((0,0,0))
        Dibujar_texto('Jugar', FUENTE, (255, 255, 255), VENTANA, 360, 160) 
        Dibujar_texto('Opciones', FUENTE, (255,255,255),VENTANA, 345, 260)
        mx, my = pygame.mouse.get_pos()
 
        Boton_1 = pygame.Rect(300, 150, 200, 50)
        Boton_2 = pygame.Rect(300, 250, 200, 50)
 
        if Boton_2.collidepoint((mx, my)):
            if click:
                Opciones()

        if Boton_1.collidepoint((mx, my)):
            if click:
                if ventana == 0:
                    print("Viento final: ",v)
                    print("Gravedad final: ",g)
                    salirTodo = main.Juego(g, v ,Lista_proyect)
                    if salirTodo == -1:
                        return -1000

                if ventana == 1:
                    print("Viento final: ",v)
                    print("Gravedad final: ",g)
                    salirTodo = main_2.Juego(g, v ,Lista_proyect, jugadores)
                    if salirTodo == -1:
                        exit()    
        
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


Menu_principal(lista_elementos=[0,3,5,3,9.8,0,0])
