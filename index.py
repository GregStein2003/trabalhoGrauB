import os
import csv
# import pandas as pd

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux

valor = float(input('Digite o valor do ingresso: '))
linhas = int(input('Digite a quantidade de fileiras: '))
colunas = int(input('Digite a letra de assentos por fileira: '))
linhaDigitaLetra = ''

# def carregarNomeArquivo():
#     nomeArquivo = input('Informe o nome do arquivo: ')

#     return nomeArquivo

def carregarDados():

    # carregarNomeArquivo() # Função para pedir o nome do arquivo

    nomeArquivo = input('Informe o nome do arquivo: ')

    f = open(f"{nomeArquivo}.csv", 'a')
    reader = csv.reader(f)

    if os.stat(f"{nomeArquivo}.csv").st_size == 0:
        M = []
        for i in range(linhas):
            M.append([0] * colunas)

    f.close()

    return M

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
    
def realizarReserva(M):

    nomeArquivo = input('Informe o nome do arquivo: ')
    
    print('Lugares Vagos: ')
    for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
        print()
        for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
            if M[outro][outroC] == 0:
                print('.', end=" ")
            else:
                print('x', end=" ")
    print()
    print()
                
    linhaDigita = int(input('Digite uma linha: ')) - 1
    colunaDigita = int(input('Digite uma coluna: ')) -1 

    for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
        for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
            if linhaDigita >= linhas and colunaDigita >= colunas:
                print('Digite uma cadeira válida!')
                break
            if outro == linhaDigita and outroC == colunaDigita:
                sexo = str(input("Informe o seu gênero: "))
                idade = int(input("Informe a sua idade: "))
                fA = open(f"{nomeArquivo}.csv", "a")
                writer = csv.writer(fA)
                if linhaDigita == 0:
                    linhaDigitaLetra = 'A'
                elif linhaDigita == 1:
                    linhaDigitaLetra = 'B'
                elif linhaDigita == 2:
                    linhaDigitaLetra = 'C'
                elif linhaDigita == 3:
                    linhaDigitaLetra = 'D'
                elif linhaDigita == 4:
                    linhaDigitaLetra = 'E'
                writer.writerow([f'{linhaDigitaLetra}' + f'{colunaDigita + 1}', sexo, idade])
                fA.close()
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
            M = carregarDados()

        elif item == 2:
            print('2 - Consultar Situação de um Assento:')
            input('Digite enter para prosseguir')

        elif item == 3:
            realizarReserva(M)

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