import csv

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

# Lê as informações 
# with open('grauB.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     # Número de linhas
#     for row in spamreader:
#         for x in row:
#             print(', '.join(x[0]))

#     # Número de colunas
#     for column in spamreader:
#         for y in column:
#             print(', '.join(y[1]))
