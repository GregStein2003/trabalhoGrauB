import os
import csv

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux

valor = float(input('Digite o valor do ingresso: '))
linhas = int(input('Digite a quantidade de fileiras: '))
colunas = int(input('Digite o número de assentos por fileira: '))
M = []

for i in range(linhas):
    M.append(list('0' * colunas))

def mostrarMapa():

    for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
        print()
        for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
            if M[outro][outroC] == '0':
                print('.', end=" ")
            else:
                print(M[outro][outroC])

    print()
    input('Digite enter para prosseguir')
    
    # print('Posição - [{}][{}], valor: {}' .format(outro, outroC, M[outro][outroC])) 

def selecionarCadeira():
    linhaDigita = int(input('Digite uma linha: '))
    colunaDigita = int(input('Digite uma coluna: '))

    for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
        for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
            if outro == linhaDigita and outroC == colunaDigita:
                if linhaDigita >= linhas and colunaDigita >= colunas:
                    print('Digite uma cadeira válida!')
                else:
                    idade = int(input('Informe a sua idade: '))
                    sexo = str(input('Informe o seu sexo: '))
                    M[linhaDigita][colunaDigita] = 'x'
                    break

    input('Digite enter para prosseguir')


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
            print('1 - Carregar Dados:')
            input('Digite enter para prosseguir')

        elif item == 2:
            print('2 - Consultar Situação de um Assento:')
            input('Digite enter para prosseguir')

        elif item == 3:
            print('3 - Realizar Reserva:')
            input('Digite enter para prosseguir')

        elif item == 4:
            print('4 - Liberar Reserva:')
            input('Digite enter para prosseguir')

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