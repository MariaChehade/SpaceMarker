import pygame
import csv
import time
coordenadas=[]
texto=[]
def salvar():
    with open("marcacoes.csv", "w", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        for i in range(len(coordenadas)):
            escritor.writerow([texto[i], coordenadas[i][0], coordenadas[i][1]])
def excluir():
    coordenadas.clear()
    texto.clear()

