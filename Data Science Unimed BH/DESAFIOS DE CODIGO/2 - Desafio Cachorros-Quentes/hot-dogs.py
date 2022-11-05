Correção do desafio de codigo da DIO 
Desenvolvedor Eduardo Pereira Nogueira

valores = input().split() 

hot_dogs = int(valores[0])
participantes = int(valores[1])

media =  hot_dogs / participantes

print('%.2f'%(media))