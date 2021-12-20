import pygame
from PIL import Image, ImageDraw

class Mapa():

    def __init__(self) -> None:
        pass
        
    def terreno(VENTANA,seleccion_mapa):
            
            if(seleccion_mapa==1):
                piso = pygame.image.load("imagenes/800x500/m1.png")
                VENTANA.blit(piso, (0, 0))

            if(seleccion_mapa==2):
                piso = pygame.image.load("imagenes/800x500/m2.png")
                VENTANA.blit(piso, (0, 0))

            if(seleccion_mapa==3):
                piso = pygame.image.load("imagenes/800x500/m3.png")
                VENTANA.blit(piso, (0, 0))

    def terreno2(VENTANA,seleccion_mapa):
            
        if(seleccion_mapa==1):
            piso = pygame.image.load("imagenes/800x500/m11.png")
            VENTANA.blit(piso, (0, 0))

        if(seleccion_mapa==2):
            piso = pygame.image.load("imagenes/800x500/m22.png")
            VENTANA.blit(piso, (0, 0))

        if(seleccion_mapa==3):
            piso = pygame.image.load("imagenes/800x500/m33.png")
            VENTANA.blit(piso, (0, 0))

    def destruccionMapa(VENTANA, x,y, seleccion_mapa, cont, opcion_proyectil):
        print("ENTRA EN DESTRUCCION CON VALOR OPC : ", opcion_proyectil)
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
                with Image.open("imagenes/800x500/m1.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-a, y-a, x+a, y+a), fill=(152,204,255))
                    im.save("imagenes/800x500/m11.png")
            if(cont > 1):
                with Image.open("imagenes/800x500/m11.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-a, y-a, x+a, y+a), fill=(152,204,255))
                    im.save("imagenes/800x500/m11.png")

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
                with Image.open("imagenes/800x500/m2.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-b, y-b, x+b, y+b), fill=(237,253,253))
                    im.save("imagenes/800x500/m22.png")
            if(cont > 1):
                with Image.open("imagenes/800x500/m22.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-b, y-b, x+b, y+b), fill=(237,253,253))
                    im.save("imagenes/800x500/m22.png")

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
                with Image.open("imagenes/800x500/m3.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-c, y-c, x+c, y+c), fill=(207,207,207))
                    im.save("imagenes/800x500/m33.png")
            if(cont > 1):
                with Image.open("imagenes/800x500/m33.png") as im:
                    draw = ImageDraw.Draw(im)
                    draw.ellipse((x-c, y-c, x+c, y+c), fill=(207,207,207))
                    im.save("imagenes/800x500/m33.png")

    def colisionBala_terreno(x, y, seleccion_mapa, cont):
        if seleccion_mapa == 0:
            color_terreno = (84,114,128)
            color_cielo = (152,204,255)

        if(seleccion_mapa == 1):
            if(y > 0):
                color_terreno = (84,114,128)
                color_cielo = (152,204,255)

                if(cont == 1):
                    im = Image.open("imagenes/800x500/m1.png")
                if(cont > 1):
                    im = Image.open("imagenes/800x500/m11.png")
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
                color_terreno = (114,93,23)
                color_cielo = (237,253,253)

                if(cont == 1):
                    im = Image.open("imagenes/800x500/m2.png")
                if(cont > 1):
                    im = Image.open("imagenes/800x500/m22.png")
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
                color_terreno = (117,10,51)
                color_cielo = (207,207,207)

                if(cont == 1):
                    im = Image.open("imagenes/800x500/m3.png")
                if(cont > 1):
                    im = Image.open("imagenes/800x500/m33.png")
                im = im.convert("RGBA")
                
                pixels = im.load()
                
                r, g, b, a = pixels[x, y]
                
                if (r, g, b) == color_terreno:
                    #print(r,g,b)
                    #pixels[x, y] = (color_terreno[0], color_terreno[1], color_terreno[2], a)
                    print("colision terreno")
                    return False

    