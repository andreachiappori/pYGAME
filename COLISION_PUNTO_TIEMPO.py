#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importación de los módulos
import pygame
import random
import sys
#from pygame.locals import *
ancho=640
alto= 480
red = (0,200,200)
azul=(100,100,100)
blanco=(255,255,255)


def main():
    puntaje=0
    pygame.init()  # inicializa pygame
    
    miventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("crear una ventana")
    
    personaje = pygame.image.load("RECURSOS/codi.png")
    personaje = pygame.transform.scale(personaje,(90,90))
    personaje_rect = personaje.get_rect()
    personaje_rect.center = (ancho//2, alto//2)
    personaje_mask =pygame.mask.from_surface(personaje)
    x_random = random.randint(0,ancho)
    y_random = random.randint(0,alto)
    muro = pygame.image.load("RECURSOS/cuadro.png")
    muro_rect= muro.get_rect()
    muro_rect.center = (x_random,y_random)
    muro_mask =pygame.mask.from_surface(muro)
    font = pygame.font.Font(None, 48)
    punto = font.render("Puntaje:" +str(puntaje), True, red) 
    punto_rect = punto.get_rect()
    punto_rect.center = (500, 20)
    
    font1 = pygame.font.Font(None, 48)
    tiempo = font1.render("TIEMPO: 0", True, blanco) 
    tiempo_rect = tiempo.get_rect()
    tiempo_rect.center = (85, 20)
    
    font2=  pygame.font.Font(None, 90)
    game = font2.render("GAME OVER", True, blanco) 
    game_rect = game.get_rect()
    game_rect.center = (ancho//2,alto//2)

    while True:
        segundos = pygame.time.get_ticks() // 1000
        # Posibles entradas del teclado y mouse
        tiempo = font.render("TIEMPO: "  + str(segundos), True, blanco) 
        tiempo_rect = tiempo.get_rect()
        tiempo_rect.center = (85, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
  
        tecla_p = pygame.key.get_pressed()
        if tecla_p[pygame.K_w] or tecla_p[pygame.K_UP]:
           personaje_rect.y -=5
        if tecla_p[pygame.K_s] or tecla_p[pygame.K_DOWN]:
           personaje_rect.y +=5
        if tecla_p[pygame.K_d] or tecla_p[pygame.K_RIGHT]:
           personaje_rect.x +=5
        if tecla_p[pygame.K_a]or tecla_p[pygame.K_LEFT]:
           personaje_rect.x -=5    
        #Validación para que no se valla de la pantalla
        if  personaje_rect.bottom > alto:
            personaje_rect.bottom =alto
        if  personaje_rect.top < 0:
            personaje_rect.top =0
        if  personaje_rect.left <0:
            personaje_rect.left =0
        if  personaje_rect.right > ancho:
            personaje_rect.right =ancho
            
      #  if personaje_rect.colliderect(muro_rect):
       #     print("colisi,,")
        #else:
         #   print("  no   ---")
        
        offset = ( personaje_rect.x - muro_rect.x , personaje_rect.y - muro_rect.y)
        if personaje_mask.overlap(muro_mask, offset):
           print( 'Existe una colisión')
           x_random = random.randint(0,ancho)
           y_random = random.randint(0,alto)
           muro_rect.center = (x_random,y_random)
           muro_mask =pygame.mask.from_surface(muro)
           print("x,y",muro_rect.center)
           puntaje +=1
           punto = font.render("Puntaje:" +str(puntaje), True, red) 
           punto_rect = punto.get_rect()
           punto_rect.center = (500, 20)
       # if puntaje ==5:
       #     muro = pygame.image.load("RECURSOS/descarga.png").convert_alpha()
       #     muro= pygame.transform.scale(muro,(40,40))
       #     muro_rect= muro.get_rect()
       #     muro_rect.center = (x_random,y_random)
       #     muro_mask =pygame.mask.from_surface(muro)
        if segundos == 5:
            miventana.fill((255,0,0))
            miventana.blit(game, game_rect)
            punto_rect.center= (ancho//2,(alto//2)+100)
            miventana.blit(punto,punto_rect)
            pygame.display.update()
            #segundos = pygame.time.get_ticks() // 1000
            pygapme.time.wait(3*1000)
            sys.exit()
        
        miventana.fill((255,0,0))
        miventana.blit(personaje, personaje_rect)
        miventana.blit(muro,muro_rect)
        miventana.blit(punto,punto_rect)
        miventana.blit(tiempo,tiempo_rect)
        pygame.display.flip()
        
        pygame.display.update()
        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    main()



