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
            if M[linhaDigita][colunaDigita] != 'x':
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
                # listaInfos.append(f'{linhaDigitaLetra}' + f'{colunaDigita + 1}', sexo, idade)
                fA.close()
                M[linhaDigita][colunaDigita] = 'x'
                break
            else:
                if outro == len(M) - 1: 
                    print('Cadeira inválida')
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
                if str(x[0]).startswith("A1"):
                    print()
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
    # print('Posição - [{}][{}], valor: {}' .format(outro, outroC, M[outro][outroC])) 

def selecionarCadeira():
    input('Digite enter para prosseguir: ')

# Relatório

def listagemInfos():
    fReader = open(f"{cA}.csv", 'r')
    readerExistente = csv.reader(fReader)
    tabela = list(readerExistente)
    for x in tabela:
        if x == []:
            continue  
        else: 
            if int(x[2]) > 0 and int(x[2]) <= 17:
                print(f'{x[0]}, {x[1]}, {x[2]}, R${(valor/2)}\n')
            elif int(x[2]) >= 18 and int(x[2]) <= 59:
                print(f'{x[0]}, {x[1]}, {x[2]}, R${valor}\n')
            else:
                print(f'{x[0]}, {x[1]}, {x[2]}, R${(valor/2)}\n')
    input('Digite enter para prosseguir: ')

def quantidadeAssento():

    qTotal = len(M) * len(M)
    qReservados = 0
    qLiberados = 0

    for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
        for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
            if M[outro][outroC] == 0:
                qLiberados += 1
            else:
                qReservados += 1
                
    print(f'\nQuantidade total de assentos: {qTotal} \n')
    print(f'Quantidade de assentos reservados: {qReservados} \n')
    print(f'Quantidade de assentos liberados: {qLiberados} \n')
    input('Digite enter para prosseguir: ')

def quantidadeReserva():
        assentoMasculino = 0
        assentoFeminino = 0
        fReader = open(f"{cA}.csv", 'r')
        readerExistente = csv.reader(fReader)
        tabela = list(readerExistente)
        for x in tabela:
            if x == []:
                continue  
            else: 
                if x[1] == "M":
                    assentoMasculino += 1
                else:
                    assentoFeminino += 1
        fReader.close()

        print(f'\nQuantidade de reservas realizada por mulheres: {assentoFeminino}\n')
        print(f'Quantidade de reservas realizada por homens: {assentoMasculino}\n')
        input('Digite enter para prosseguir: ')

def grafico():

    meiaEntrada = 0
    inteiraEntrada = 0
    meiaIdoso = 0
    fReader = open(f"{cA}.csv", 'r')
    readerExistente = csv.reader(fReader)
    tabela = list(readerExistente)
    for x in tabela:
        if x == []:
            continue  
        else: 
            if int(x[2]) > 0 and int(x[2]) <= 17:
                meiaEntrada += 1
            elif int(x[2]) >= 18 and int(x[2]) <= 59:
                inteiraEntrada += 1
            else:
                meiaIdoso += 1
                
    fReader.close()

    # Variáveis para o gráfico
    valorMeiaEntrada = (valor/2) * meiaEntrada
    valorInteiraEntrada = valor * inteiraEntrada
    valorMeiaIdoso = (valor/2) * meiaIdoso
    total = meiaEntrada + inteiraEntrada + meiaIdoso

    # Porcentagem
    porcentagemMeiaEntrada = (meiaEntrada/total) * 100
    porcentagemEntradaInteira = (inteiraEntrada/total) * 100
    porcentagemMeiaIdoso = (meiaIdoso/total) * 100



    print(f"\nMeia menor: {meiaEntrada} – {porcentagemMeiaEntrada}% |=====---------------| R$ {valorMeiaEntrada}\n")
    print(f"Inteira : {inteiraEntrada} – {porcentagemEntradaInteira}% |===========---------| R$ {valorInteiraEntrada}\n")
    print(f"Meia idoso: {meiaIdoso} – {porcentagemMeiaIdoso}% |====----------------| R$ {valorMeiaIdoso}\n")
    print("|====================================================|\n")
    print(f"Total : {total} – 100,0% |====================| R$ {valorMeiaEntrada + valorInteiraEntrada + valorMeiaIdoso}\n")
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
        print('6 - Relatórios:\n')
        print('7 - Sair\n')
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
            while True:
                print('\n..:: Menu - Relatórios ::..\n')
                print('1 - Listagem de informações: ')
                print('2 - Quantidade total de assentos: ')
                print('3 - Quantidade de Reservas dividido por sexo:')
                print('4 - Gráfico:')
                print('5 - Sair:\n')
                itemSubMenu = int(input("Digite uma opção: "))

                if itemSubMenu == 1:
                    listagemInfos()
                elif itemSubMenu == 2:
                    quantidadeAssento()
                elif itemSubMenu == 3:
                    quantidadeReserva()
                elif itemSubMenu == 4:
                    grafico()
                elif itemSubMenu == 5:
                    break
                else:
                    print('Opção não encontrada!')
                    break
        elif item == 7:
            print("Programa encerrado")
            break
        else:
            print("Opção não encontrada")
            break



        # Tarefas

        # Visualmente a função liberarAssento() já está pronto, no entanto, é necessário remover do arquivo
        # .csv também

        # Analisar como iremos guardar as informações dos indíviduos no sistema.