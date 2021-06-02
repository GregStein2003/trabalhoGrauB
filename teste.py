import os

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux
linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))
numberL = int(input('Digite o número da linha que você quer percorrer: '))
numberC = int(input('Digite o número da coluna que você quer percorrer: '))
M = []

for i in range(linhas):
    M.append(list(range(colunas * i, colunas * (i + 1))))

for l in M:
    print(l)

print('########')

print('Linha:')
for outroL in M[numberL - 1]: # Caso queira saber uma linha específica é só pesquisar Matriz[linha - 1]
    print('x', end=" ")

print('\nColuna:')
for outro in range(len(M)): # range(Número de linhas)
    print(M[outro][numberC - 1], end=" ")
    # [0][Número da coluna]
    # [1][Número da coluna]
    # [2][Número da coluna]