import os
import csv

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux

# Escreve as informações no .csv
nomeArquivo = input('Informe o nome do arquivo: ')

f = open(f"{nomeArquivo}.csv", "w")
writer = csv.writer(f)
writer.writerows([['Assento', 'Sexo', 'Idade']])

for letra in range(ord('A'), ord('D') + 1):
    for numero in range(1, 4):
        print(chr(letra) + str(numero)) #CHR(Converte para letra)
        writer.writerow([chr(letra) + str(numero)])
    print() #Quebra de linha

f.close()

print('LEITURA DE ARQUIVOS')

# Lê as informações 
f = open(f"{nomeArquivo}.csv", 'r')
reader = csv.reader(f)
tabela = list(reader)
for x in tabela:
    if x == []:
        continue # Utilizei esse if para pular as linhas em branco da tabela
    else:
        print(x[0]) # Gostaria de pegar somente o elemento A(1x), pois ele está na coluna[0] e linha[0]  
        
f.close()
