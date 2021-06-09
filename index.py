import os
import csv
# import pandas as pd

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux

valor = float(input('Digite o valor do ingresso: '))
linhas = int(input('Digite a quantidade de fileiras: '))
colunas = int(input('Digite a letra de assentos por fileira: '))
M = []

for i in range(linhas):
    M.append([0] * colunas)

f = open("grauB.csv", "w")
writer = csv.writer(f)
writer.writerows([['Assento', 'Sexo', 'Idade']])

def carregarDados():

    print()

    nomeArquivo = input('Informe o nome do arquivo: ')

    # with open(f"D:\\Informações Pessoais\\Unisinos\\Análise e Desenovimento de Sistemas\\1° Semestre\\Fundamentos da Programação\\Visual\\{nomeArquivo}.csv", "r") as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print(row)
    f = open(f"{nomeArquivo}.csv", "w")
    writer = csv.writer(f)
    writer.writerows([['Assento', 'Sexo', 'Idade']])

    for letra in range(ord('A'), ord(f'{colunas}') + 1):
        for numero in range(1, linhas + 1):
            print(chr(letra) + str(numero)) #CHR(Converte para letra)
            writer.writerow([chr(letra) + str(numero), 'abacaxi', 12])
            break
        print() #Quebra de linha

    f.close()

def mostrarMapa():

    print(M)

    # for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
    #     print()
    #     for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
    #         if M[outro][outroC] == 0:
    #             print('.', end=" ")
    #         else:
    #             print('x', end=" ")
    # print()
    input('Digite enter para prosseguir')
    
    # print('Posição - [{}][{}], valor: {}' .format(outro, outroC, M[outro][outroC])) 

def selecionarCadeira():
    input('Digite enter para prosseguir: ')
    
def realizarReserva():

    print()
    
    print('Lugares Vagos: ')
    for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
        print()
        for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
            if M[outro][outroC] == 0:
                print('.', end=" ")
            else:
                print('x', end=" ")
    print()
                
    linhaDigita = int(input('Digite uma linha: '))
    colunaDigita = int(input('Digite uma coluna: '))

    for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
            for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
                if linhaDigita >= linhas and colunaDigita >= colunas:
                    print('Digite uma cadeira válida!')
                    break
                if outro == linhaDigita and outroC == colunaDigita:
                    sexo = str(input("Informe o seu gênero: "))
                    idade = int(input("Informe a sua idade: "))
                    fA = open("grauB.csv", "a")
                    writer = csv.writer(fA)
                    writer.writerow([f'[{linhaDigita}][{colunaDigita}]', sexo, idade])
                    f.close()
                    M[linhaDigita][colunaDigita] = 'x'
                    break
                
    input('Digite enter para prosseguir')
    
def testeLerDados():
    # for l in M:
    #     print(l)
    print(M)

# Menu
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux
    # Menu Principal
    while True:
        print('\n..:: Sistema para Gerenciamento de Cinema ::..\n')
        print('1 - Carregar Dados:')
        print('2 - Consultar Situação de um Assento:')
        print('3 - Realizar Reserva:')
        print('4 - Liberar Reserva:')
        print('5 - Visualizar Mapa do Cinema:')
        print('6 - Salvar Dados:\n')
        print('7 - Sair\n')
        print('8 - Seleciona Cadeira\n')
        item = int(input("Digite uma opção: "))

        if item == 1:
            carregarDados()

        elif item == 2:
            print('2 - Consultar Situação de um Assento:')
            input('Digite enter para prosseguir')

        elif item == 3:
            realizarReserva()

        elif item == 4:
            testeLerDados()

        elif item == 5:
            mostrarMapa()

        elif item == 6:
            print('6 - Salvar Dados:')
            input('Digite enter para prosseguir')

        elif item == 7:
            print("Programa encerrado")
            break

        elif item == 8:
            selecionarCadeira()
            

        else:
            print("Opção não encontrada")
            break