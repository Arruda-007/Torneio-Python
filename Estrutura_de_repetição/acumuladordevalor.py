soma_total = 0

while True:
    numero = float(input('Digite um numero (0 para sair):'))
    if numero == 0:
        break
    soma_total += numero
print('Resultao da soma total:', soma_total)