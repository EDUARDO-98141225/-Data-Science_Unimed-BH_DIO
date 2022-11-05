Correção do desafio de codigo da DIO 
Desenvolvedor Eduardo Pereira Nogueira



while True: 
    try: 
               
     perna = input() 
     if (perna == 'esquerda'):
        print('ingles')
     elif (perna == 'direita'):
        print('frances')
     elif (perna == 'nenhuma'):
        print('portugues')
     else:
        print('caiu')
    
    except EOFError: 
        break