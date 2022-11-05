Correção do desafio de codigo da DIO 
Desenvolvedor Eduardo Pereira Nogueira


letra = input() 

num = 0
soma = 0

num = ord(letra)
for i in range(65,91):
 soma = soma + 1
 if i == num:
  print(soma)
  break