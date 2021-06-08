import os 
import csv

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux
cinema = []
quantidadeFileiras = int(input("Informe a quantidade de fileiras: "))
quantidadeAssentos = int(input("Informe a quantidade de assentos por fileira: "))

for i in range(quantidadeFileiras):
    cinema.append([0] * quantidadeAssentos)
print(cinema)

def selecionarCadeira():
    selecioneFileira = int(input('Digite a Fileira que você deseja: '))
    selecioneAssento = int(input('Digite o assento que você deseja: '))

selecionarCadeira()