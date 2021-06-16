import os
import csv

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux

valor = float(input('Digite o valor do ingresso: '))
linhas = int(input('Digite a quantidade de fileiras: '))
colunas = int(input('Digite a letra de assentos por fileira: '))
linhaDigitaLetra = ''

def carregarNomeArquivo():
    nomeArquivo = input('Informe o nome do arquivo: ')

    return nomeArquivo

def carregarDados():

    f = open(f"{cA}.csv", 'a')
    reader = csv.reader(f)

    if os.stat(f"{cA}.csv").st_size == 0:
        M = []
        for i in range(linhas):
            M.append([0] * colunas)
    else:
        fReader = open(f"{cA}.csv", 'r')
        readerExistente = csv.reader(fReader)
        tabela = list(readerExistente)
        M = []
        listaOcupados = []
        for x in tabela:
            if x == []:
                continue  
            else: 
                xzao = str(x)
                imprimir = xzao.replace("['", "").split(",")[0]
                imprimir = imprimir.replace(imprimir[-1], "")
                listaOcupados.append(imprimir)     

        for i in range(linhas):
            M.append([0] * linhas)

        for x in listaOcupados:
            linhaFor = int(x[1]) - 1 
            if x[0] == 'A': 
                M[0][linhaFor] = 'x'
            elif x[0] == 'B':
                M[1][linhaFor] = 'x'
            elif x[0] == 'C':
                M[2][linhaFor] = 'x'
            elif x[0] == 'D':
                M[3][linhaFor] = 'x'
            elif x[0] == 'E':
                M[4][linhaFor] = 'x'

    f.close()

    return M

def consultarAssento(M):

    print(M)
    
    linhaDigita = int(input('Digite uma linha: ')) - 1
    colunaDigita = int(input('Digite uma coluna: ')) - 1 

    if M[linhaDigita][colunaDigita] == 'x':
        print('Assento está ocupada!')
    else:
        print('Assento está vaga!')

    input('Digite enter para prosseguir: ')

def realizarReserva(M):

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
    colunaDigita = int(input('Digite uma coluna: ')) - 1 

    for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
        for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
            if M[linhaDigita][colunaDigita] == 'x':
                print('Digite uma cadeira válida!')
                break
            elif outro == linhaDigita and outroC == colunaDigita:
                sexo = str(input("Informe o seu gênero: "))
                idade = int(input("Informe a sua idade: "))
                fA = open(f"{cA}.csv", "a")
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
                listaInfos.append(f'{linhaDigitaLetra}' + f'{colunaDigita + 1}', sexo, idade)
                fA.close()
                M[linhaDigita][colunaDigita] = 'x'
                break
            
    input('Digite enter para prosseguir')

    return listaInfos

def liberarAssento(M):

    print('MAPA: ')
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
    colunaDigita = int(input('Digite uma coluna: ')) - 1 

    if M[linhaDigita][colunaDigita] == 0:
        print('O Assento já estava vago, por favor insira os dados novamente ')
    else:
        M[linhaDigita][colunaDigita] = 0
        # For para ler o arquivo e encontrar a posição solicitada pelo usuário
        fReader = open(f"{cA}.csv", 'r')
        readerExistente = csv.reader(fReader)
        tabela = list(readerExistente)
        for x in tabela:
            if x == []:
                continue  
            else: 
                print(x)
                # xzao = str(x)
                # imprimir = xzao.replace("['", "").split(",")[0]
                # imprimir = imprimir.replace(imprimir[-1], "")
                # print(imprimir)    
            
        print('Assento desocupado!')

    input('Digite enter para prosseguir: ')

def mostrarMapa():

    print('MAPA: ')
    for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
        print()
        for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
            if M[outro][outroC] == 0:
                print('.', end=" ")
            else:
                print('x', end=" ")
    print()
    input('Continue...')
    print(listaInfos)
    input('Continue...')
    
    # print('Posição - [{}][{}], valor: {}' .format(outro, outroC, M[outro][outroC])) 

def selecionarCadeira():
    input('Digite enter para prosseguir: ')
    
# Menu
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux
    # Menu Principal
    
    listaInfos = []

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
            cA = carregarNomeArquivo()
            M = carregarDados()

        elif item == 2:
            consultarAssento(M)

        elif item == 3:
            realizarReserva(M)

        elif item == 4:
            liberarAssento(M)

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



        # Tarefas

        # Visualmente a função liberarAssento() já está pronto, no entanto, é necessário remover do arquivo
        # .csv também

        # Analisar como iremos guardar as informações dos indíviduos no sistema.