import os

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux

print('\nLaços aninhados')
for letra in range(ord('A'), ord('D')):
    print(chr(letra), end=' ') #CHR(Converte para letra)
    print() #Quebra de linha

  