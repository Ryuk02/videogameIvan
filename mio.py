# videogameIvan
#-*- coding: utf-8 -*-
import pygame, sys
import random

from pygame.locals import *


pygame.init()
reloj = pygame.time.Clock()
fps = 30

pygame.key.set_repeat(1,24)
anchopantalla = 1160
altopantalla = 400
contadorreset = 0
activado = 1
desactivado = 0
distanciabala = 7

visor = pygame.display.set_mode((anchopantalla,altopantalla))

pygame.display.set_caption("Ivan")

pokemon1 = pygame.image.load('pokemon.png')
pokemon2 = pygame.image.load('pokemon2.png')
paisaje1 = pygame.image.load('paisaje1.png')
paisaje2 = pygame.image.load('paisaje2.png')
paisaje3 = pygame.image.load('paisaje3.png')
paisaje4 = pygame.image.load('paisaje4.png')
agua = pygame.image.load('agua.png')
tubo = pygame.image.load('tubo.png')
arbol = pygame.image.load('arbol.png')
fanama = pygame.image.load('fantasma1.png')
fanrojo = pygame.image.load('fantasma2.png')
fanazul = pygame.image.load('fantasma3.png')

paisaje=[paisaje1, paisaje2, paisaje3, paisaje4]
contadorpaisaje=0

fasemovpok1=0
fasemovpok2=0
faseagua=0

'''personaje1['posx']=0
personaje2['posx']=0'''
posagua=0





#pokemon1
movpoke1evo1der=[(0,40,39,60),(42,40,39,60),(83,40,39,60)]
movpoke1evo1izq=[(0,150,40,60),(42,150,40,60),(83,150,40,60)]
movpoke1evo2der=[(0,270,40,60),(42,270,40,60),(83,270,40,60)]
movpoke1evo2izq=[(0,400,40,60),(42,400,40,60),(85,400,40,60)]
movpoke1evo3der=[(0,506,41,60),(42,506,41,60),(84,506,41,60)]
movpoke1evo3izq=[(0,615,41,60),(42,615,41,60),(84,615,41,60)]

movpoke1evo1=[movpoke1evo1der,movpoke1evo1izq]
movpoke1evo2=[movpoke1evo2der,movpoke1evo2izq]
movpoke1evo3=[movpoke1evo3der,movpoke1evo3izq]
#pokemon2
movpoke2evo1der=[(0,40,39,60),(42,40,39,60),(83,40,39,60)]
movpoke2evo1izq=[(0,150,40,60),(42,150,40,60),(83,150,40,60)]
movpoke2evo2der=[(0,270,40,60),(42,270,40,60),(83,270,40,60)]
movpoke2evo2izq=[(0,400,40,60),(42,400,40,60),(85,400,40,60)]
movpoke2evo3der=[(0,506,41,60),(42,506,41,60),(84,506,41,60)]
movpoke2evo3izq=[(0,615,41,60),(42,615,41,60),(84,615,41,60)]

personaje1={"posx": 0, "posy": 300, "direccion":"right", 'distanciabala':distanciabala}
personaje2={"posx": 0, "posy": 300, "direccion":"right", 'distanciabala':distanciabala}

listapersonajes=[personaje1,personaje2]
listaimagfan=[pygame.image.load('fantasma1.png'),pygame.image.load('fantasma2.png'),pygame.image.load('fantasma3.png')]

#mecanismo de los fantasmas part 1/2
multiplo=1
listaaparicion=[]
listainterruptor=[]
for tete in listaimagfan:
    punto = multiplo*(anchopantalla/(len(listaimagfan)+1))
    listaaparicion.append(punto)
    multiplo+=1
    listainterruptor.append(0)
print listaaparicion
print listainterruptor

#tiene que haber los mismos huecos que fantasmas haya.
'''listaaparicion=[100,300,500]
listainterruptor=[0,0,0]'''
contadorlistas=0

movpoke2evo1=[movpoke2evo1der,movpoke2evo1izq]
movpoke2evo2=[movpoke2evo2der,movpoke2evo2izq]
movpoke2evo3=[movpoke2evo3der,movpoke2evo3izq]

t=0
f=0

listafantasma=[]

#disparo
listadisparo=[]
e = 0
c = 0
limitedisparo =40
#direccion = "derecha"
movagua=[(0,5,10,5),(11,5,10,5),(22,5,10,5),(0,9,10,4),(11,9,10,4),(22,9,10,4),(0,13,10,4),(11,13,10,4),(22,13,10,4),
(0,18,10,5),(11,18,10,5),(22,18,10,5)]

#salto pokemon1
subir=(range(0,90,3))
bajar=(range(90,-1,-3))
salto = subir + bajar
personaje1['posy'] = 300
contadorsaltopok1 = 0
posinicialpok1 = 300
interruptorpok1 = 0

#salto pokemon2
personaje2['posy'] = 295
contadorsaltopok2 = 0
posinicialpok2 = 295
interruptorpok2 = 0

#movimiento tubo
derecha=(range(0,20,2))
izquierda=(range(20,-2,-2))
lista_tubo = derecha + izquierda
contadortubo = 0
postubo_inicial = 1086
postubo = 1086
interruptortubo = 0

#def disparo1():
    #direccion = "derecha"
    #if direccion == "derecha":
        #disparo={'x': 0, 'y': 300, 'bala': pygame.image.load('llama1.png'), 'imagbala':[(0,0,33,33),(33,0,33,33),(0,33,33,33),(33,33,33,33)]}
        #disparo['x'] = personaje2['posx']
        #listadisparo.append(disparo)
    #else:
        #disparo={'x': 0, 'y': 300, 'bala': pygame.image.load('llama1.png'), 'imagbala':[(0,66,33,33),(33,66,33,33),(0,99,33,33),(33,99,33,33)]}
        #disparo['x'] = personaje2['posx']
        #listadisparo.append(disparo)
'''def salirfan(contadorlistas, listainterruptor, listapersonajes):
    for o in listainterruptor:
        for diccionario in listapersonajes:
            if contadorlistas > len(listainterruptor):
                contadorlistas = 0
            if diccionario["posx"] > listaaparicion[contadorlistas]:
                if listainterruptor[contadorlistas] == 0:
                    listainterruptor[contadorlistas] = 1
                    fantasma={"fanavance":0, "direccion":(0,0,32,30), 'sumatoriofan': 5, "imagenfan": listaimagfan[contadorlistas]}
                    contadorlistas += 1

                    return fantasma, contadorlistas'''

while True:

    teclasPulsadas = pygame.key.get_pressed()
    if interruptorpok1 == 1:
        contadorsaltopok1 += 1
        personaje1['posy'] = posinicialpok1 - salto[contadorsaltopok1]
        if contadorsaltopok1 == len(salto)-1:
            interruptorpok1 = desactivado
            contadorsaltopok1 = contadorreset

    if interruptorpok2 ==1:
        contadorsaltopok2 += 1
        personaje2['posy'] = posinicialpok2 - salto[contadorsaltopok2]
        if contadorsaltopok2 == len(salto)-1:
            interruptorpok2 = desactivado
            contadorsaltopok2 = contadorreset

    if interruptortubo == 1:
        contadortubo += 1
        postubo = postubo_inicial + lista_tubo[contadortubo]
        if contadortubo == len(lista_tubo)-1:
            contadortubo = contadorreset
            interruptortubo = desactivado

    aleatoriox=random.randrange(10,17)
    aleatorioy=random.randrange(10,17)

    #mecanismo de los fantasmas part 2/2
    for o in listainterruptor:
        for diccionario in listapersonajes:
            if contadorlistas > len(listainterruptor)-1:
                contadorlistas = 0
            if diccionario["posx"] > listaaparicion[contadorlistas]:
                if listainterruptor[contadorlistas] == 0:
                    listainterruptor[contadorlistas] = 1
                    fantasma={"fanavance":0, "direccion":(0,0,32,30), 'sumatoriofan': 5, "imagenfan": listaimagfan[contadorlistas]}
                    contadorlistas += 1
                    listafantasma.append(fantasma)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #pokemon1
        if teclasPulsadas[K_LEFT]:
            personaje1["direccion"]="left"
            personaje1['posx']-=3
            personaje1["posx"] -= 3
            t=1
            fasemovpok1 += 1
            if fasemovpok1 > 2:
                fasemovpok1 = 0
            if personaje1['posx'] > 1086:
                personaje1['posx'] += 1
        if teclasPulsadas[K_RIGHT]:
            t=0
            personaje1["direccion"]="right"
            personaje1['posx']+=3
            personaje1["posx"] += 3
            fasemovpok1 += 1
            if fasemovpok1 > 2:
                fasemovpok1 = 0
        if teclasPulsadas[K_p]:
            personaje1['distanciabala'] += 1
            if personaje1['distanciabala'] == distanciabala:
                personaje1['distanciabala'] = 0
                if len(listadisparo) < limitedisparo:
                    if personaje1["direccion"]=="right":
                        disparo={'bala': pygame.image.load('agua.png'), 'imagbala':[(0,5,10,5),(11,5,10,5),(22,5,10,5),(0,9,10,4)], "direcright":0,}
                        disparo['x'] = personaje1['posx']+ 10
                        disparo['y'] = personaje1['posy']+ 30
                        listadisparo.append(disparo)
                    else:
                        disparo={'bala': pygame.image.load('agua.png'), 'imagbala':[(0,13,10,4),(11,13,10,4),(22,13,10,4),(0,18,10,5)], "direcleft":0}
                        disparo['x'] = personaje1['posx']+ 10
                        disparo['y'] = personaje1['posy']+ 30
                        listadisparo.append(disparo)

        # salto
        if teclasPulsadas[K_UP]:
            interruptorpok1 = activado

        # evoluciones
        if teclasPulsadas[K_l]:
            movpoke1evo1=movpoke1evo2
        if teclasPulsadas[K_l]:
            movpoke1evo2=movpoke1evo3

        #pokemon2
        if teclasPulsadas[K_a]:
            f=1
            personaje2['posx']-=3
            personaje2["direccion"]="left"
            personaje2["posx"] -= 3
            fasemovpok2 += 1
            if fasemovpok2 >2:
                fasemovpok2 = 0
            if personaje2['posx'] > 1086:
                personaje2['posx'] +=1
        if teclasPulsadas[K_d]:
            f=0
            personaje2['posx']+=3
            personaje2["direccion"]="right"
            personaje2["posx"] += 3
            fasemovpok2 += 1
            if fasemovpok2 > 2:
                fasemovpok2 = 0

        if teclasPulsadas[K_SPACE]:
            personaje2['distanciabala'] += 1
            if personaje2['distanciabala'] == distanciabala:
                personaje2['distanciabala'] = 0
                if limitedisparo > len(listadisparo):
                    if personaje2["direccion"]=="right":
                        disparo={'bala': pygame.image.load('llama1.png'), 'imagbala':[(0,0,33,33),(33,0,33,33),(0,33,33,33),(33,33,33,33)], "direcright":0}
                        disparo['x'] = personaje2['posx']
                        disparo['y'] = personaje2['posy']+ 10
                        listadisparo.append(disparo)
                    else:
                        disparo={'bala': pygame.image.load('llama1.png'), 'imagbala':[(0,66,33,33),(33,66,33,33),(0,99,33,33),(33,99,33,33)],"direcleft":0}
                        disparo['x'] = personaje2['posx']
                        disparo['y'] = personaje2['posy']+ 10
                        listadisparo.append(disparo)

        #salto
        if teclasPulsadas[K_w]:
            interruptorpok2 = activado

        #evoluciones
        if teclasPulsadas[K_e]:
            movpoke2evo1=movpoke2evo2
        if teclasPulsadas[K_e]:
            movpoke2evo2=movpoke2evo3

        # limites
        if personaje1['posx'] > 1120:
            personaje1['posx'] = 1119
        if personaje1['posx'] < 0:
            personaje1['posx'] = 0

        #paso de pantalla
        if personaje1['posx'] == 1101:
            interruptortubo = activado
        if personaje2['posx'] == 1101:
            interruptortubo = activado
        if personaje1['posx'] > 1102 and personaje2['posx'] > 1102 and interruptortubo == desactivado:
            contadorpaisaje +=1
            personaje1['posx'] = 0
            personaje2['posx'] = 0

    for u in listadisparo:
        if u['x'] > anchopantalla:
            listadisparo.remove(u)
        if u['x'] < 0:
            listadisparo.remove(u)
    for u in listadisparo:
        if u.has_key("direcright"):
            u['x'] += 10
        else:
            u['x'] -= 10

    for b in listafantasma:
        if b["fanavance"] > anchopantalla - 32:
            b["sumatoriofan"] = -5
            b["direccion"]=(32,0,32,30)
        if b["fanavance"] < 0:
            b["sumatoriofan"] = 5
            b["direccion"]=(0,0,32,30)
        b["fanavance"] += b['sumatoriofan']

    if teclasPulsadas[K_SPACE] == 0:
        personaje2['distanciabala'] = distanciabala-1
        #print personaje2['distanciabala']

    if teclasPulsadas[K_p] == 0:
        personaje1['distanciabala'] = distanciabala-1
        #print personaje1['distanciabala']
    visor.fill((255,255,255))
    visor.blit(paisaje[contadorpaisaje],(0,0))
    visor.blit(arbol,(250,271))
    for b in listafantasma:
        visor.blit(b["imagenfan"],(aleatoriox + b["fanavance"], aleatorioy), b["direccion"])
    for u in listadisparo:
        if e > len(disparo['imagbala'])-1:
            e = 0
        visor.blit(u['bala'],(u['x'],u['y']), u['imagbala'][e])
        if c > len(listadisparo)-1:
            e += 1
            c = 0
        c += 1


    visor.blit(pokemon1,(personaje1['posx'], personaje1['posy']),movpoke1evo1[t][fasemovpok1])
    visor.blit(pokemon2,(personaje2['posx'], personaje2['posy']),movpoke2evo1[f][fasemovpok2])
    visor.blit(tubo,(postubo,298))
    visor.blit(arbol,(500,271))

    reloj.tick(30)
    pygame.display.update()
