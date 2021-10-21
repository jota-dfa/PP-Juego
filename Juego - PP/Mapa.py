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
        if seleccion_mapa == 0:
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

        if(seleccion_mapa==1):
            if x > 0 and x < 100:  
                a = ((0.01*x-132)*-1)-y
                if a<-60:         
                    print("RECT 1")
                    return False            
            if x > 100 and x < 150:  
                b = ((-0.4*x-89)*-1)-y
                if b<-60:         
                    print("RECT 2")
                    return False
            if x > 150 and x < 118:   
                c = ((1.7*x-413)*-1)-y
                if c<-60:         
                    print("RECT 3")
                    return False
            if x > 118 and x < 228: 
                f = ((-0.5*x-123)*-1)-y
                if f<-60:         
                    print("RECT 4")
                    return False
            if x > 228 and x < 248:  
                g = ((-3.5*x+571)*-1)-y
                if g<-60:         
                    print("RECT 5")
                    return False
            if x > 248 and x < 300:  
                h = ((1.4*x-676)*-1)-y
                if h<-60:         
                    print("RECT 6")
                    return False
            if x > 300 and x < 366:   
                i = ((0.7*x-461)*-1)-y
                if i<-60:         
                    print("RECT 7")
                    return False
            if x > 366 and x < 401:  
                j = ((1.1*x-608)*-1)-y
                if j<-60:         
                    print("RECT 8")
                    return False
            if x > 401 and x < 449:  
                k = ((0.1*x-211)*-1)-y
                if k<-60:         
                    print("RECT 9")
                    return False
            if x > 449 and x < 504:   
                l = ((-1.1*x+338)*-1)-y
                if l<-60:         
                    print("RECT 10")
                    return False
            if x > 504 and x < 593:   
                m = ((-0.6*x+100)*-1)-y
                if m<-60:         
                    print("RECT 11")
                    return False
            if x > 593 and x < 663:  
                n = ((0.8*x-781)*-1)-y
                if n<-60:         
                    print("RECT 12")
                    return False
            if x > 663 and x < 610:
                o = ((-1.0*x+507)*-1)-y
                if o<-60:         
                    print("RECT 13")
                    return False
            if x > 610 and x < 701:   
                p = ((0.2*x-301)*-1)-y
                if p<-60:         
                    print("RECT 14")
                    return False
            if x > 701 and x < 800:   
                q = ((-0.009*x-128)*-1)-y
                if q<-60:         
                    print("RECT 15")
                    return False
           
        if (seleccion_mapa == 2):
            if x > 0 and x < 73.627:
                a = ((1.358*x-250)*-1)-y
                if a < - 30:
                    print("RECT 1")
                    return False

            if x > 73.627  and x < 150:
                b = ((-1.309*x-53.595)*-1)-y
                if b < - 30:
                    print("RECT 2")
                    return False

            if x > 150 and x < 250:
                c = (250)-y
                if c < - 30:
                    print("RECT 3")
                    return False    

            if x > 250 and x < 300:
                d = ((-x)*-1)-y
                if d < - 30:
                    print("RECT 4")
                    return False
                    
            if x > 300 and x < 350:
                e = ((x-600)*-1)-y
                if e < - 30:
                    print("RECT 5")
                    return False

            if x > 350 and x < 450:
                f = (250)-y
                if f < - 30:
                    print("RECT 6")
                    return False

            if x > 450 and x < 500:
                g = ((-x+200)*-1)-y
                if g < - 30:
                    print("RECT 7")
                    return False

            if x > 500 and x < 550:
                h = ((x-800)*-1)-y
                if h < - 30:
                    print("RECT 8")
                    return False
            if x > 550 and x < 650:
                i = (250)-y
                if i < - 30:
                    print("RECT 9")
                    return False
            if x > 650 and x < 724.538:
                j = ((1.341*x-1122.038)*-1)-y
                if j < -30 :
                    print("RECT 10")
                    return False

            if x > 724.538 and x < 800:
                k = ((-1.325*x+810.136)*-1)+y
                if k <  -10:
                    print("RECT 11")
                    return False

        if(seleccion_mapa==3):
            if x > 0 and x < 34:   
                a = ((0.3*x-176)*-1)-y
                if a<-60:         
                    print("RECT 1")
                    return False
            if x > 38 and x < 49:   
                b = ((-5.4*x+47)*-1)-y
                if b<-60:         
                    print("RECT 2")
                    return False
            if x > 49 and x < 100:  
                c = ((-0.5*x-195)*-1)-y
                if c<-60:         
                    print("RECT 3")
                    return False
            if x > 100 and x < 149:   
                f = ((-1.9*x-59)*-1)-y
                if f<-60:         
                    print("RECT 4")
                    return False
            if x > 149 and x < 190:  
                g = ((2.6*x-745)*-1)-y
                if g<-60:         
                    print("RECT 5")
                    return False
            if x > 190 and x < 253:  
                h = ((0.6*x-349)*-1)-y
                if h<-60:         
                    print("RECT 6")
                    return False
            if x > 253 and x < 283:   
                i = ((1.5*x-581)*-1)-y
                if i<-60:         
                    print("RECT 7")
                    return False
            if x > 283 and x < 339: 
                j = ((-1.5*x+289)*-1)-y
                if j<-60:         
                    print("RECT 8")
                    return False
            if x > 339 and x < 408:  
                k = ((-0.06*x-209)*-1)-y
                if k<-60:         
                    print("RECT 9")
                    return False
            if x > 408 and x < 469:  
                l = ((-1.3*x+326)*-1)-y
                if l<-60:         
                    print("RECT 10")
                    return False
            if x > 469 and x < 520:   
                m = ((2.1*x-1305)*-1)-y
                if m<-60:         
                    print("RECT 11")
                    return False
            if x > 520 and x < 566:   
                n = ((0.9*x-698)*-1)-y
                if n<-60:         
                    print("RECT 12")
                    return False
            if x > 566 and x < 650: 
                o = ((-0.2*x-48)*-1)-y
                if o<-60:         
                    print("RECT 13")
                    return False
            if x > 650 and x < 700:  
                p = ((0.7*x-670)*-1)-y
                if p<-60:         
                    print("RECT 14")
                    return False
            if x > 700 and x < 756:  
                q = ((-0.3*x+66)*-1)-y
                if q<-60:         
                    print("RECT 15")
                    return False
            if x > 756 and x < 800:  
                r = ((0.6*x+643)*-1)-y
                if r<-60:         
                    print("RECT 16")
                    return False