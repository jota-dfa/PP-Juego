import pygame

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