import pygame
from tkinter import simpledialog
pygame.init()

#configurações:
tamanho=(800,550)
display=pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
fundo=pygame.image.load('fundo.jpeg')



#cores:
branco=(255,255,255)
preto=(0,0,0)
azul=(143, 174, 171)
roxo=(139,0,139)

coordenadas=[]

#Jogo:
running=True
while running:
    display.fill(branco)
    display.blit(fundo, (0,100))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            item=simpledialog.askstring("Space", "Qual o nome dessa estrela?")
            coordenadas.append(pos)
            print(item)
            raio=10
            if item==None:
                item="Estrela desconhecida"+str(pos)
                print(item)
    for item in coordenadas:
        pygame.draw.circle(display, roxo, item, raio)

    

    
    pygame.display.update()
pygame.quit()