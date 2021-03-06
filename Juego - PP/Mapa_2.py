import pygame
from PIL import Image, ImageDraw
import math

class Mapa():

    def __init__(self) -> None:
        pass
        
    def terreno(VENTANA,seleccion_mapa):
            
        if(seleccion_mapa==1):
            piso = pygame.image.load("imagenes/1600x900/16m1.png")
            VENTANA.blit(piso, (0, 0))

        if(seleccion_mapa==2):
            piso = pygame.image.load("imagenes/1600x900/16m2.png")
            VENTANA.blit(piso, (0, 0))

        if(seleccion_mapa==3):
            piso = pygame.image.load("imagenes/1600x900/16m3.png")
            VENTANA.blit(piso, (0, 0))

    def terreno2(VENTANA,seleccion_mapa):

        if(seleccion_mapa==1):
            piso = pygame.image.load("imagenes/1600x900/16m11.png")
            VENTANA.blit(piso, (0, 0))

        if(seleccion_mapa==2):
            piso = pygame.image.load("imagenes/1600x900/16m22.png")
            VENTANA.blit(piso, (0, 0))

        if(seleccion_mapa==3):
            piso = pygame.image.load("imagenes/1600x900/16m33.png")
            VENTANA.blit(piso, (0, 0))


    def destruccionMapa(VENTANA, x,y, seleccion_mapa, cont, opcion_proyectil):
        a = 0
        b = 0
        c = 0
        if(seleccion_mapa == 1):
            if opcion_proyectil == 0:
                a = 25
            if opcion_proyectil == 1: #daño 50
                a = 100
            if opcion_proyectil == 2: #daño 40
                a = 70  
            if opcion_proyectil == 3: #daño 30
                a = 40

            if(cont == 1):
                with Image.open("imagenes/1600x900/16m1.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-a, y-a, x+a, y+a), fill=(152,204,255))
                    im.save("imagenes/1600x900/16m11.png")
            if(cont > 1):
                with Image.open("imagenes/1600x900/16m11.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-a, y-a, x+a, y+a), fill=(152,204,255))
                    im.save("imagenes/1600x900/16m11.png")
        
        if(seleccion_mapa == 2):
            if opcion_proyectil == 0:
                b = 25
            if opcion_proyectil == 1: #daño 50
                b = 100
            if opcion_proyectil == 2: #daño 40
                b = 70  
            if opcion_proyectil == 3: #daño 30
                b = 40
                                  
            if(cont == 1):
                with Image.open("imagenes/1600x900/16m2.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-b, y-b, x+b, y+b), fill=(237,253,253))
                    im.save("imagenes/1600x900/16m22.png")
            if(cont > 1):
                with Image.open("imagenes/1600x900/16m22.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-b, y-b, x+b, y+b), fill=(237,253,253))
                    im.save("imagenes/1600x900/16m22.png")

        if(seleccion_mapa == 3):
            if opcion_proyectil == 0:
                c = 25
            if opcion_proyectil == 1: #daño 50
                c = 100
            if opcion_proyectil == 2: #daño 40
                c = 70  
            if opcion_proyectil == 3: #daño 30
                c = 40 

            if(cont == 1):
                with Image.open("imagenes/1600x900/16m3.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-c, y-c, x+c, y+c), fill=(207,207,207))
                    im.save("imagenes/1600x900/16m33.png")
            if(cont > 1):
                with Image.open("imagenes/1600x900/16m33.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-c, y-c, x+c, y+c), fill=(207,207,207))
                    im.save("imagenes/1600x900/16m33.png")
    
    def colisionBala_terreno(x, y, seleccion_mapa, cont):
        if seleccion_mapa == 0:
            color_terreno = (84,114,128)
            color_cielo = (152,204,255)

        if(seleccion_mapa == 1):
            if(y > 0): # Permite salir del rango superior sin crashear.
                if(y > 900): # Si sobrepasa el lim inferior colsiona directamente sin crashear
                    return False
                color_terreno = (84,114,128)
                color_cielo = (152,204,255)

                if(cont == 1):
                    im = Image.open("imagenes/1600x900/16m1.png")
                if(cont > 1):
                    im = Image.open("imagenes/1600x900/16m11.png")
                im = im.convert("RGBA")
                
                pixels = im.load()
                
                r, g, b, a = pixels[x, y]
                
                if (r, g, b) == color_terreno:
                    #print(r,g,b)
                    #pixels[x, y] = (color_terreno[0], color_terreno[1], color_terreno[2], a)
                    print("colision terreno")
                    return False

        if (seleccion_mapa == 2):
            if(y > 0):
                if(y > 900): # Si sobrepasa el lim inferior colsiona directamente sin crashear
                    return False
                color_terreno = (114,93,23)
                color_cielo = (237,253,253)

                if(cont == 1):
                    im = Image.open("imagenes/1600x900/16m2.png")
                if(cont > 1):
                    im = Image.open("imagenes/1600x900/16m22.png")
                im = im.convert("RGBA")
                
                pixels = im.load()
                
                r, g, b, a = pixels[x, y]
                
                if (r, g, b) == color_terreno:
                    #print(r,g,b)
                    #pixels[x, y] = (color_terreno[0], color_terreno[1], color_terreno[2], a)
                    print("colision terreno")
                    return False

        if(seleccion_mapa==3):
            if(y > 0):
                if(y > 900): # Si sobrepasa el lim inferior colsiona directamente sin crashear
                    return False
                color_terreno = (117,10,51)
                color_cielo = (207,207,207)

                if(cont == 1):
                    im = Image.open("imagenes/1600x900/16m3.png")
                if(cont > 1):
                    im = Image.open("imagenes/1600x900/16m33.png")
                im = im.convert("RGBA")
                
                pixels = im.load()
                
                r, g, b, a = pixels[x, y]
                
                if (r, g, b) == color_terreno:
                    #print(r,g,b)
                    #pixels[x, y] = (color_terreno[0], color_terreno[1], color_terreno[2], a)
                    print("colision terreno")
                    return False
    
    '''Colisiones proyectil'''
    def colision_terreno(x,y):   #lim laterales     
        if(x<=0 or x>=1600):
            return False
        
        '''if(y>=400): ####colision terreno planoooooooooooooooooooo
            return False'''

    def dañoRadio(x,y , numTanks, vida, indexListPos, opcProyectil, listaPos):
        
        print("Tanque", indexListPos)
        print("proyectil", opcProyectil)


        if opcProyectil == 0: # Daño 10
            for i in range(numTanks):
                x1 = listaPos[i][0]
                y1 = listaPos[i][1]

                print("radio", math.sqrt( math.pow(x1 - x, 2) + (math.pow(y1 -y, 2))))
                
                if(math.sqrt( math.pow((x1 - x), 2) + (math.pow((y1 -y), 2))) <= 32):
                    vida[i] = vida[i]-10
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1+60 - x), 2) + (math.pow((y1 -y), 2))) <= 32):
                    vida[i] = vida[i]-10
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1 - x), 2) + (math.pow((y1+30 -y), 2))) <= 32):
                    vida[i] = vida[i]-10
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1+60 - x), 2) + (math.pow((y1+30 -y), 2))) <= 32):
                    vida[i] = vida[i]-10
                    print("daño por explosion")
                    return vida

        if opcProyectil == 1: # Daño 50
            for i in range(numTanks):
                
                x1 = listaPos[i][0]
                y1 = listaPos[i][1]

                #print(math.sqrt( math.pow(x1 - x, 2) + (math.pow(y1 -y, 2))))
                
                if(math.sqrt( math.pow((x1 - x), 2) + (math.pow((y1 -y), 2))) <= 50):
                    vida[i] = vida[i]-50
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1+60 - x), 2) + (math.pow((y1 -y), 2))) <= 50):
                    vida[i] = vida[i]-50
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1 - x), 2) + (math.pow((y1+30 -y), 2))) <= 50):
                    vida[i] = vida[i]-50
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1+60 - x), 2) + (math.pow((y1+30 -y), 2))) <= 50):
                    vida[i] = vida[i]-50
                    print("daño por explosion")
                    return vida

        if opcProyectil == 2: # Daño 40
            for i in range(numTanks):
                x1 = listaPos[i][0]
                y1 = listaPos[i][1]

                #print(math.sqrt( math.pow(x1 - x, 2) + (math.pow(y1 -y, 2))))
                
                if(math.sqrt( math.pow((x1 - x), 2) + (math.pow((y1 -y), 2))) <= 35):
                    vida[i] = vida[i]-40
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1+60 - x), 2) + (math.pow((y1 -y), 2))) <= 35):
                    vida[i] = vida[i]-40
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1 - x), 2) + (math.pow((y1+30 -y), 2))) <= 35):
                    vida[i] = vida[i]-40
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1+60 - x), 2) + (math.pow((y1+30 -y), 2))) <= 35):
                    vida[i] = vida[i]-40
                    print("daño por explosion")
                    return vida

        if opcProyectil == 3: # Daño 30
            for i in range(numTanks):
                x1 = listaPos[i][0]
                y1 = listaPos[i][1]

                #print(math.sqrt( math.pow(x1 - x, 2) + (math.pow(y1 -y, 2))))
                
                if(math.sqrt( math.pow((x1 - x), 2) + (math.pow((y1 -y), 2))) <= 20):
                    vida[i] = vida[i]-30
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1+60 - x), 2) + (math.pow((y1 -y), 2))) <= 20):
                    vida[i] = vida[i]-30
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1 - x), 2) + (math.pow((y1+30 -y), 2))) <= 20):
                    vida[i] = vida[i]-30
                    print("daño por explosion")
                    return vida
                if(math.sqrt( math.pow((x1+60 - x), 2) + (math.pow((y1+30 -y), 2))) <= 20):
                    vida[i] = vida[i]-30
                    print("daño por explosion")
                    return vida

        return vida


        