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
        
    def caen(turno, seleccion_mapa, posx_tank, posy_tank):
        
        if seleccion_mapa == 1:
            
            color_terreno = (84,114,128)
            
            if(turno == 0):
                im = Image.open("imagenes/1600x900/16m1.png")
            if(turno != 0):
                im = Image.open("imagenes/1600x900/16m11.png")
            im = im.convert("RGBA")
            pixels = im.load()

            r, g, b, a = pixels[posx_tank, posy_tank]

            while(pixels[posx_tank+25, posy_tank+25] != (84,114,128,255)):
                posy_tank += 1
                
            """while(pixels[posx_tank][posy_tank+25+i] != (84,114,128) and pixels[posx_tank+50][posx_tank+25+i] != (84,114,128)):
                posy_tank += 1
                i += 1"""

            return posx_tank, posy_tank
            


    def p1(VENTANA, coordenada1_1, coordenada1_2): # b = random
        tanque_1 = pygame.image.load("imagenes/tanque_1.png")
        VENTANA.blit(tanque_1, (coordenada1_1, coordenada1_2)) 
        
    def p2(VENTANA, x, y): # a = random
        tanque_2 = pygame.image.load("imagenes/tanque_2.png")
        VENTANA.blit(tanque_2, (x, y))

    def p3(VENTANA, x, y): # a = random
        tanque_2 = pygame.image.load("imagenes/tanque_11.png")
        VENTANA.blit(tanque_2, (x, y))

    def p4(VENTANA, x, y): # a = random
        tanque_2 = pygame.image.load("imagenes/tanque_22.png")
        VENTANA.blit(tanque_2, (x, y))

    def p5(VENTANA, x, y): # a = random
        tanque_2 = pygame.image.load("imagenes/tanque_111.png")
        VENTANA.blit(tanque_2, (x, y))

    def p6(VENTANA, x, y): # a = random
        tanque_2 = pygame.image.load("imagenes/tanque_222.png")
        VENTANA.blit(tanque_2, (x, y))  

    def col_proyectil_tanque(x_proyect, y_proyect, tuplex, tupley, numTank):
        
        if numTank == 2:

            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True 
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True

        if numTank == 3:
        
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True

        if numTank == 4:
        
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True

        if numTank == 5:
        
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    print("Le pego al tank", tuplex, "," , tupley)
                    return True

        if numTank == 6:
        
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    return True
            if(x_proyect >= tuplex and x_proyect <= tuplex+60):
                if(y_proyect >= tupley and y_proyect <= tupley+35):
                    return True

        

    def aparecen(VENTANA, listPos, numTanques): 
        if numTanques == 2:
            Tanques.p1(VENTANA, listPos[0][0], listPos[0][1])
            Tanques.p2(VENTANA, listPos[1][0], listPos[1][1])
        if numTanques == 3:
            Tanques.p1(VENTANA, listPos[0][0], listPos[0][1])
            Tanques.p2(VENTANA, listPos[1][0], listPos[1][1])
            Tanques.p3(VENTANA, listPos[0][0], listPos[0][1])
        if numTanques == 4:
            Tanques.p1(VENTANA, listPos[0][0], listPos[0][1])
            Tanques.p2(VENTANA, listPos[1][0], listPos[1][1])
            Tanques.p3(VENTANA, listPos[2][0], listPos[2][1])
            Tanques.p4(VENTANA, listPos[3][0], listPos[3][1])
        if numTanques == 5:
            Tanques.p1(VENTANA, listPos[0][0], listPos[0][1])
            Tanques.p2(VENTANA, listPos[1][0], listPos[1][1])
            Tanques.p3(VENTANA, listPos[2][0], listPos[2][1])
            Tanques.p4(VENTANA, listPos[3][0], listPos[3][1])
            Tanques.p5(VENTANA, listPos[4][0], listPos[4][1])
        if numTanques == 6:
            Tanques.p1(VENTANA, listPos[0][0], listPos[0][1])
            Tanques.p2(VENTANA, listPos[1][0], listPos[1][1])
            Tanques.p3(VENTANA, listPos[2][0], listPos[2][1])
            Tanques.p4(VENTANA, listPos[3][0], listPos[3][1])
            Tanques.p5(VENTANA, listPos[4][0], listPos[4][1])
            Tanques.p6(VENTANA, listPos[5][0], listPos[5][1])

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