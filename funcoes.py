import pygame
import csv
import time
nomes=[]
coordenadas=[]
som=[]
branco=[]
textoForma=[]
fonte=[]
display=[]
def salvar():
    with open("marcacoes.csv", "w", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        for i in range(len(coordenadas)):
            escritor.writerow([nomes[i], coordenadas[i][0], coordenadas[i][1]])
def carregar():
    try:
        with open("marcacoes.csv", "r", newline="") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                nome=linha[0]
                x=int(linha[1])
                y=int(linha[2])
                coordenadas.append((x, y))
                nomes.append(nome)
    except FileNotFoundError:
        pass
def excluir():
    coordenadas.clear()
    nomes.clear()

