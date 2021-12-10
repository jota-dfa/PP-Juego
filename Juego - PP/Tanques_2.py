import pygame

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

    def vida(VENTANA, lista, daño, id):
    
        vida_1, vida_2 = lista[0], lista[1]

        #pygame.draw.rect(VENTANA, 'black', [0, 425, 100, 25])
        #pygame.draw.rect(VENTANA, 'black', [700, 425, 100, 25])

        #pygame.draw.rect(VENTANA, 'green', [0, 420, vida_1, 30])
        #pygame.draw.rect(VENTANA, 'green', [700, 420, vida_2, 30])

        if id == 1:
            vida_1 = vida_1 - daño
            lista[0] = vida_1
        
        if id == 2:
            vida_2 = vida_2 - daño
            lista[1] = vida_2


        pygame.draw.rect(VENTANA, 'green', [0, 700, vida_1, 50])
        pygame.draw.rect(VENTANA, 'green', [1500, 700, vida_2, 50])

        return lista