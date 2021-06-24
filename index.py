import os
import csv

def carregarNomeArquivo():
    nomeArquivo = input('Informe o nome do arquivo: ') # Função (nome do arquivo)

    return nomeArquivo

def carregarDados():

    # Lê o arquivo CSV
    f = open(f"{cA}.csv", 'r') # cA = retorno Função carregarNomeArquivo()
    reader = csv.reader(f)

    # Comparação para verificar se possui dados no arquivo
    if os.stat(f"{cA}.csv").st_size == 0: # Caso não tiver
        M = []
        for i in range(linhas): # Cria a Matriz com zeros
            M.append([0] * colunas)
    else: # Caso tiver
        fReader = open(f"{cA}.csv", 'r')
        readerExistente = csv.reader(fReader)
        tabela = list(readerExistente)
        M = []
        listaOcupados = []
        for x in tabela: # Lê as informações no csv
            if x == []: # Pula linhas em branco
                continue  
            else: # Formatação do conteúdo que está dentro do arquivo csv
                xzao = str(x)
                imprimir = xzao.replace("['", "").split(",")[0]
                imprimir = imprimir.replace(imprimir[-1], "")
                listaOcupados.append(imprimir)     

        # Cria a Matriz
        for i in range(linhas):
            M.append([0] * linhas)

        # Substitui na matriz com 'x' os lugares ocupados 
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
            elif x[0] == 'F':
                M[5][linhaFor] = 'x'
            elif x[0] == 'G':
                M[6][linhaFor] = 'x'
            elif x[0] == 'H':
                M[7][linhaFor] = 'x'
            elif x[0] == 'I':
                M[8][linhaFor] = 'x'
            elif x[0] == 'J':
                M[9][linhaFor] = 'x'
            elif x[0] == 'K':
                M[10][linhaFor] = 'x'

    f.close()

    return M # Retorna a Matriz

def consultarAssento(M):
    
    # Pede as informações ao usuário
    linhaDigita = int(input('Digite uma linha: ')) - 1
    colunaDigita = int(input('Digite uma coluna: ')) - 1

    # Comparação para verificar se o local está ocupado
    if M[linhaDigita][colunaDigita] == 'x':
        # Converte Números para letras EX: [0][0] = A1
        if linhaDigita == 0:
            linhaDigitaOutro = 'A'
        elif linhaDigita == 1:
            linhaDigitaOutro = 'B'
        elif linhaDigita == 2:
            linhaDigitaOutro = 'C'
        elif linhaDigita == 3:
            linhaDigitaOutro = 'D'
        elif linhaDigita == 4:
            linhaDigitaOutro = 'E'
        elif linhaDigita == 5:
            linhaDigitaOutro = 'F'
        elif linhaDigita == 6:
            linhaDigitaOutro = 'G'
        elif linhaDigita == 7:
            linhaDigitaOutro = 'H'
        elif linhaDigita == 8:
            linhaDigitaOutro = 'I'
        elif linhaDigita == 9:
            linhaDigitaOutro = 'J'
        elif linhaDigita == 10:
            linhaDigitaOutro = 'K'
        # Lê o arquivo
        fReader = open(f"{cA}.csv", 'r')
        readerExistente = csv.reader(fReader)
        tabela = list(readerExistente)
        for x in tabela:
            if x == []:
                continue  
            else: 
                # Comparação de Assentos
                if x[0] == (linhaDigitaOutro + str(colunaDigita + 1)): # A1 == A + 1
                    print(f'Assento Ocupado: Sexo:{x[1]}, Idade:{x[2]}Anos')
                    break
        fReader.close()
    else:
        print('Assento está vago!')
    input('Digite enter para prosseguir: ')

def realizarReserva(M):

    # Mostra visualmente o mapa de Assentos
    mostrarMapa()
                
    # Pede ao usuário a informações
    linhaDigita = int(input('Digite uma linha: ')) - 1
    colunaDigita = int(input('Digite uma coluna: ')) - 1 

    for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
        for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
            if M[linhaDigita][colunaDigita] != 'x':
                sexo = str(input("Informe o seu gênero: "))
                idade = int(input("Informe a sua idade: "))
                # Comparação para saber qual segmento de idade se encontra
                if idade > 0 and idade <= 17:
                    print(f'Meia-Entrada (Infantil)\n')
                elif idade >= 18 and idade <= 59:
                    print(f'Ingresso inteiro\n')
                else:
                    print(f'Meia-Entrada (Idoso)\n')
                # Abre o arquivo
                fA = open(f"{cA}.csv", "a")
                writer = csv.writer(fA)
                # Realiza a conversão de Letras para Número: [1][1] = B2    
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
                elif linhaDigita == 5:
                    linhaDigitaLetra = 'F'
                elif linhaDigita == 6:
                    linhaDigitaLetra = 'G'
                elif linhaDigita == 7:
                    linhaDigitaLetra = 'H'
                elif linhaDigita == 8:
                    linhaDigitaLetra = 'I'
                elif linhaDigita == 9:
                    linhaDigitaLetra = 'J'
                elif linhaDigita == 10:
                    linhaDigitaLetra = 'K'
                # Adiciona as informações no arquivo .CSV
                writer.writerow([f'{linhaDigitaLetra}' + f'{colunaDigita + 1}', sexo, idade])
                fA.close()
                # Retrata que o assento está ocupado na Matriz
                M[linhaDigita][colunaDigita] = 'x'
                break
            else:
                # Caso a cadeira já está ocupada
                if outro == len(M) - 1 and M[linhaDigita][colunaDigita] == 'x':
                    break
            
    input('Digite enter para prosseguir')

def liberarAssento(M):

    # Mostra Visualmente o mapa de assentos
    mostrarMapa()

    # Pede ao usuário o assento desejado
    linhaDigita = int(input('Digite uma linha: ')) - 1
    colunaDigita = int(input('Digite uma coluna: ')) - 1 

    # Comparação, para obter a informação se o assento está ocupado ou não
    if M[linhaDigita][colunaDigita] == 0:
        print('O Assento já estava vago, por favor insira os dados novamente ')
    else:
        # Altera somente na Matriz(Interna)
        M[linhaDigita][colunaDigita] = 0
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
    print()
    input('Continue...')    

# Relatório

def listagemInfos():
    # Lê o arquivo
    fReader = open(f"{cA}.csv", 'r')
    readerExistente = csv.reader(fReader)
    tabela = list(readerExistente)
    # For para ler as informações do .csv
    for x in tabela:
        if x == []:
            continue  
        else: 
            # Comparação para saber qual o valor do ingresso
            # X[0] = Assento; X[1] = Sexo; X[2] = Idade
            if int(x[2]) > 0 and int(x[2]) <= 17:
                print(f'{x[0]}, {x[1]}, {x[2]} Anos, R${(valor/2)}\n') 
            elif int(x[2]) >= 18 and int(x[2]) <= 59:
                print(f'{x[0]}, {x[1]}, {x[2]} Anos, R${valor}\n')
            else:
                print(f'{x[0]}, {x[1]}, {x[2]} Anos, R${(valor/2)}\n')
    input('Digite enter para prosseguir: ')

def quantidadeAssento():

    qTotal = len(M) * len(M) # Cálcula a quantidade total de assentos
    qReservados = 0 # Variável Contadora
    qLiberados = 0 # Variável Contadora

    for outro in range(len(M)): # Lê a matriz || 0 - Número de linhas
        for outroC in range(len(M[0])): # Lê cada valor da Matria || 0 - Número de colunas
            if M[outro][outroC] == 0:
                qLiberados += 1 # Todas vez que o laço tiver vago(0), irá acrescentar +1 na variável
            else:
                qReservados += 1 # Todas vez que o laço tiver ocupado(x), irá acrescentar +1 na variável
            
    print(f'\nQuantidade total de assentos: {qTotal} \n')
    print(f'Quantidade de assentos reservados: {qReservados} \n')
    print(f'Quantidade de assentos liberados: {qLiberados} \n')
    input('Digite enter para prosseguir: ')

def quantidadeReserva():
        assentoMasculino = 0 # Variável Contadora
        assentoFeminino = 0 # Variável Contadora
        # Lê o arquivo
        fReader = open(f"{cA}.csv", 'r')
        readerExistente = csv.reader(fReader)
        tabela = list(readerExistente)
        # Laço para ler as informações na Tabela
        for x in tabela:
            if x == []:
                continue  
            else: 
                if x[1] == "M":
                    assentoMasculino += 1 # Caso coluna Sexo for Masculino, acrescentar +1 na variável
                else:
                    assentoFeminino += 1 # Caso coluna Sexo for Feminino, acrescentar +1 na variável
        fReader.close()

        print(f'\nQuantidade de reservas realizada por mulheres: {assentoFeminino}\n')
        print(f'Quantidade de reservas realizada por homens: {assentoMasculino}\n')
        input('Digite enter para prosseguir: ')

def grafico():

    meiaEntrada = 0 # Variável Contadora
    inteiraEntrada = 0 # Variável Contadora
    meiaIdoso = 0 # Variável Contadora
    # Lê o arquivo
    fReader = open(f"{cA}.csv", 'r')
    readerExistente = csv.reader(fReader)
    tabela = list(readerExistente)
    # Laço para ler todas as informações no arquivo .csv
    for x in tabela:
        if x == []:
            continue  
        else: 
            if int(x[2]) > 0 and int(x[2]) <= 17: # Comparação para saber o tipo de entrada (Meia-entrada (Infantil))
                meiaEntrada += 1 # Caso o indivíduo tenha entre 0-17 anos, acrescentar +1 na variável
            elif int(x[2]) >= 18 and int(x[2]) <= 59: # Comparação para saber o tipo de entrada (Entrada Inteira)
                inteiraEntrada += 1 # Caso o indivíduo tenha entre 18-59 anos, acrescentar +1 na variável
            else: # Meia entrada (Idoso)
                meiaIdoso += 1 # Caso o indivíduo tenha 58++ anos, acrescentar +1 na variável
                
    fReader.close()

    # Variáveis para o gráfico - Cálculo de valores
    valorMeiaEntrada = (valor/2) * meiaEntrada
    valorInteiraEntrada = valor * inteiraEntrada
    valorMeiaIdoso = (valor/2) * meiaIdoso
    total = meiaEntrada + inteiraEntrada + meiaIdoso

    # Porcentagem
    porcentagemMeiaEntrada = (meiaEntrada/total) * 100
    porcentagemEntradaInteira = (inteiraEntrada/total) * 100
    porcentagemMeiaIdoso = (meiaIdoso/total) * 100

    # Escreve na tela
    print(f"\nMeia menor: {meiaEntrada} – {porcentagemMeiaEntrada}% |=====---------------| R$ {valorMeiaEntrada}\n")
    print(f"Inteira : {inteiraEntrada} – {porcentagemEntradaInteira}% |===========---------| R$ {valorInteiraEntrada}\n")
    print(f"Meia idoso: {meiaIdoso} – {porcentagemMeiaIdoso}% |====----------------| R$ {valorMeiaIdoso}\n")
    print("|====================================================|\n")
    print(f"Total : {total} – 100,0% |====================| R$ {valorMeiaEntrada + valorInteiraEntrada + valorMeiaIdoso}\n")
    input('Digite enter para prosseguir: ')

# Menu
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux

    # Informações básicas e variáveis
    valor = float(input('Digite o valor do ingresso: '))
    linhas = int(input('Digite a quantidade de fileiras: '))
    colunas = int(input('Digite a letra de assentos por fileira: '))
    linhaDigitaLetra = ''
    linhaDigitaOutro = ''

    # Menu Principal
    
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
                # SUBMENU
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
