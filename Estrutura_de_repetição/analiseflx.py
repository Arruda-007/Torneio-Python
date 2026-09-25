#CODIGO 1 - Saida: 1 2 3 4 5
#for i in range(1, 6):
#   print(i) 

#CODIGO 2 - while imprimiu 3 vez até o contador virar 3, ou seja ele repetiu o codigo até virar 3
#contador = 0
#while contador < 3:
#    print('processando...')
#    contador = contador + 1

#CODIGO 3 - saida 0 1 3 4, pois continue serve para pular uma repetição do for, tudo que vem abaixo dela, então se n é 2, logo ele não aparecera na sequencia 
for n in range(5):
    if n == 2:
        continue
    print(n)
