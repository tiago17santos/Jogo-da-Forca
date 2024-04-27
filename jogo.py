import random
from os import name, system  

def limpaTela():

        #windows
        if name == 'nt':
            _ = system('cls')

        #mac/linux
        else:
            _ = system('clear')

    


desenhaBoneco = [

'''
-----------
|         |
|         
|                   
|         
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
|        \\|              
|         | 
|        
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
|        / \\ 
| 
'''

]





class Forca():

    def __init__(self, palavra):
         self.palavra = palavra
         self.letrasErradas = []
         self.letrasCorretas = []

    
    def escondeLetra(self):
        rtn = ''

        for letra in self.palavra:
            if letra not in self.letrasCorretas:
                rtn += '_'
            else:
                #self.advinhaLetra(letra)
                rtn += letra
        return rtn

    def array(self):
        for letra in self.palavra:
            if '_' not in self.letrasCorretas:
                self.letrasCorretas.append('_')
    
    def advinhaLetra(self,letra):
        
        if letra in self.palavra:
            index = 0
            
            for carac in self.palavra:
                self.array()
                if carac == letra:
                    self.letrasCorretas[index] = carac
                index +=1
            return self.letrasCorretas

        else:
            self.letrasErradas.append(letra)
            return  self.letrasErradas

    def statusJogo(self):

        tamanhoErrada = len(self.letrasErradas)
        tamanhoDesenho = len(desenhaBoneco)

        if tamanhoErrada >= tamanhoDesenho:
            return 'Você perdeu. A palavra era: ', self.palavra
            
        else:
            return desenhaBoneco[len(self.letrasErradas)]
         
    
    
    def veificaVitoria(self):
        if '_' not in self.letrasCorretas:
            return '\nParabéns você venceu, a palavra era: ', self.palavra 
            

    
    def regraGame(chances):

        print('Bem-vindo(a) ao jogo da forca!')
        print('Adivinhe a palavra abaixo:')

        listaPalavras = ['melão','abacaxi','pera','maçã']

        palavra = random.choice(listaPalavras)

        chances = 6

        letrasCorretas = ['_' for letra in palavra]

        letrasErradas = []


        while chances > 0:
            
            game = Forca

            print(desenhaBoneco(chances))
            print(' '.join(letrasCorretas))
            print('\n Chances restantes: ', chances)
            print('Letras erradas: ', ' '.join(letrasErradas))
            

            letraDigitada = input('\n Digite uma letra: ').lower()

            if letraDigitada in letrasCorretas:
                print("Você ja digitou essa letra")
                continue
            if letraDigitada in letrasErradas:
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

    
    def main(self):
        print(self.palavra)
        
        chances = len(desenhaBoneco)
        print('Bem-vindo(a) ao jogo da forca!')
        print('Adivinhe a palavra abaixo:')
        
        
        while chances > 0:
            print(self.letrasCorretas)
            print(self.statusJogo())
            print(' '.join(self.escondeLetra()))
            print('\n Chances restantes: ', chances)
            print('Letras erradas: ', ' '.join(self.letrasErradas))


            letraDigitada = input('\n Digite uma letra: ').lower()
            
            self.advinhaLetra(letraDigitada)
            self.veificaVitoria()


            chances -= 1
            

           
           # self.lerPalavra()

        
        
        


    
    
    def game():
        listaPalavras = ['melão','abacaxi','pera','maçã']

        palavra = random.choice(listaPalavras)
        game = Forca(palavra)

        limpaTela()

        game.main()




   
Forca.game()


#ler uma palava aleatoria do banco de palavras
#nao mostrar a letra no momento do jogo
#advinha letra
#checar o status do jogo e imprimir o desenho
#verificar se o  jogador venceu
#verifica se o jogo terminou
#main - para executar o jogo
 