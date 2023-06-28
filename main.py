import pygame
from tkinter import simpledialog 
import csv
import time
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
icone="icone.jpg"
pygame.display.set_icon(pygame.image.load(icone))
coordenadas=[]
texto=[]
raio=10
fonte=pygame.font.SysFont("arial",15,True,False)
pontos=0
pygame.init()
display.fill(vermelho)
display.blit(fundo, (0,100))
pygame.mixer.Sound.play(som)
item=[]
textoForma=fonte.render("Aperte [F9] para salvar as marcações",True, branco)
display.blit(textoForma, (15, 5)) 
textoForma=fonte.render("Aperte [F10] para carregar marcações salvas",True, branco)
display.blit(textoForma, (15, 25))
textoForma=fonte.render("Aperte [F11] para excluir todas as marcações",True, branco)
display.blit(textoForma, (15, 45))
textoForma=fonte.render("Aperte [F12] para fechar o programa",True, branco)
display.blit(textoForma, (15, 65)) 



#Jogo:
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            item=simpledialog.askstring("Space", "Qual o nome dessa estrela?")
            fonte=pygame.font.SysFont("arial",30,True,False)
            textoForma=fonte.render(item,True, branco)
            coordenadas.append(pos)
            texto.append(item)
            print(item)
            if item==None:
                item="Estrela desconhecida"+str(pos)
                print(item)
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_F12:
                running=False
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_F9:
                try:
                    with open("coordenadas.csv", "w", newline=" ") as arquivo:
                        escritor=csv.writer(arquivo)
                        for localizacao in coordenadas:
                            escritor.writerow(localizacao)
                except:
                    textoForma=fonte.render("Não há marcações salvas",True, branco)
                    display.blit(textoForma, (440, 45)) 
                    time.sleep(5)
                    textoForma=fonte.render(" ",True, branco)
                    continue
    coordenadas_copy=coordenadas.copy()
    for item in coordenadas_copy:
        pygame.draw.circle(display, preto,  item, raio+4)
        pygame.draw.circle(display, branco, item, raio)
        texto_surface = fonte.render("oi", True, branco)
        display.blit(textoForma, (pos)) 
    pygame.display.flip()
pygame.quit()