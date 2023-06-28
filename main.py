import pygame
from tkinter import simpledialog 
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()

#cores:
branco=(255,255,255)
preto=(0,0,0)
azul=(143, 174, 171)
roxo=(139,0,139)
vermelho=(51,0,0)

#configurações:
tamanho=(800,550)
display=pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
fundo=pygame.image.load('fundo.jpeg')
som=pygame.mixer.Sound("som.mp3")
coordenadas=[]
texto=[]
raio=10
fonte=pygame.font.SysFont("arial",40,True,False)
pontos=0
pygame.init()
pygame.font.init()



display.fill(vermelho)
display.blit(fundo, (0,100))
pygame.mixer.Sound.play(som)
item=[]
    





#Jogo:
running=True
while running:


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            item=simpledialog.askstring("Space", "Qual o nome dessa estrela?")
            textoForma=fonte.render(item,True, branco)
            coordenadas.append(pos)
            texto.append(item)
            print(item)
            
            if item==None:
                item="Estrela desconhecida"+str(pos)
                print(item)

    coordenadas_copy=coordenadas.copy()
    for item in coordenadas_copy:
        pygame.draw.circle(display, preto,  item, raio+4)
        pygame.draw.circle(display, branco, item, raio)
        texto_surface = fonte.render("oi", True, branco)

        display.blit(textoForma, (pos)) 
        
    pygame.display.flip()
pygame.quit()