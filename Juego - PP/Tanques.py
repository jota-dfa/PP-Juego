import pygame
from PIL import Image

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

    def caen(turno, seleccion_mapa, posx_tank, posy_tank):
        
        contCaida = 0

        if seleccion_mapa == 1:
            
            color_terreno = (84,114,128)
            
            if(turno == 0):
                im = Image.open("imagenes/800x500/m1.png")
            if(turno != 0):
                im = Image.open("imagenes/800x500/m11.png")
            im = im.convert("RGBA")
            pixels = im.load()

            r, g, b, a = pixels[posx_tank, posy_tank]

            while(pixels[posx_tank+25, posy_tank+25] != (84,114,128,255)):
                posy_tank += 1
                contCaida += 1
                
            """while(pixels[posx_tank][posy_tank+25+i] != (84,114,128) and pixels[posx_tank+50][posx_tank+25+i] != (84,114,128)):
                posy_tank += 1
                i += 1"""

            return (posx_tank, posy_tank) , contCaida

    def vida(VENTANA, lista, da??o, id):
    
        vida_1, vida_2 = lista[0], lista[1]

        pygame.draw.rect(VENTANA, 'black', [0, 425, 100, 25])
        pygame.draw.rect(VENTANA, 'black', [700, 425, 100, 25])

        #pygame.draw.rect(VENTANA, 'green', [0, 420, vida_1, 30])
        #pygame.draw.rect(VENTANA, 'green', [700, 420, vida_2, 30])

        if id == 1:
            vida_1 = vida_1 - da??o
            lista[0] = vida_1
        
        if id == 2:
            vida_2 = vida_2 - da??o
            lista[1] = vida_2


        pygame.draw.rect(VENTANA, 'green', [0, 425, vida_1, 25])
        pygame.draw.rect(VENTANA, 'green', [700, 425, vida_2, 25])

        return lista