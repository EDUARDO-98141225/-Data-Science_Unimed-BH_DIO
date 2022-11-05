Correção do desafio de codigo da DIO 
Desenvolvedor Eduardo Pereira Nogueira


entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])


cal_icm = distancia / (diametro1 + diametro2)

  
print ('%.2f'%(cal_icm))
