import csv 

# Escreve

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

# lê
    
# nomeArquivo = input('Informe o nome do arquivo: ')

# f = open(f"{nomeArquivo}.csv")
# writer = csv.reader(f)
# print()

# for x in tabela:
#     print(x)

# f.close()