import random
from os import name, system  


def limpaTela():

    #windows
    if name == 'nt':
        _ = system('cls')

    #mac/linux
    else:
        _ = system('clear')

def desenhaBoneco(chances):
    desenho = [
        
        '''
        -----------
        |         |
        |         O
        |        \\|/              
        |         | 
        |        / \\ 
        | 
        ''',
        '''
        -----------
        |         |
        |         O
        |        \\|/              
        |         | 
        |        /  
        | 
        ''',
        '''
        -----------
        |         |
        |         O
        |        \\|/              
        |         | 
        |          
        | 
        ''',
        '''
        -----------
        |         |
        |         O
        |        \\|              
        |         | 
        |        
        | 
        ''',
        '''
        -----------
        |         |
        |         O
        |         |             
        |         | 
        |         
        | 
        ''',
        '''
        -----------
        |         |
        |         O
        |                     
        |          
        |         
        | 
        ''',
        '''
        -----------
        |         |
        |         
        |                   
        |         
        |         
        | 
        '''


    ]

    return desenho[chances]

def game():
    
    limpaTela()

    print('Bem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:')

    listaPalavras = ['melão','abacaxi','pera','maçã']

    palavra = random.choice(listaPalavras)

    chances = 6

    letrasCorretas = ['_' for letra in palavra]

    letrasErradas = []

    while chances > 0:
        

        print(desenhaBoneco(chances))
        print('\n Chances restantes: ', chances)
        print('Letras erradas: ', ' '.join(letrasErradas))
        

        letraDigitada = input('\n Digite uma letra: ').lower()

        if letraDigitada in letrasCorretas or letrasErradas:
            print("Você ja digitou essa letra")
            continue 


        if letraDigitada in palavra:
            index = 0

            for letra in palavra:
                if letra == letraDigitada:
                    letrasCorretas[index] = letra
                index +=1

        else:
            chances -= 1
            letrasErradas.append(letraDigitada)

        
        if '_' not in letrasCorretas:
            print('\nParabéns você venceu, a palavra era: ', palavra)
            break
          
    
    if '_' in letrasCorretas:
        print('Você perdeu. A palavra era: ', palavra)
            
   
game()