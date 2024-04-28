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


def escolhePalavra():
    listaPalavras = ['melão','abacaxi','pera','maçã']

    palavra = random.choice(listaPalavras)

    return palavra


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
                rtn += letra
        return rtn


    
    def advinhaLetra(self,letra):
        
        if letra in self.palavra:
            for carac in self.palavra: 
                if carac == letra:
                    self.letrasCorretas.append(carac) 
            return self.letrasCorretas

        else:
            self.letrasErradas.append(letra)
            return  self.letrasErradas

    def statusJogo(self):

        print('Bem-vindo(a) ao jogo da forca!')
        print('Adivinhe a palavra abaixo:')

        print(desenhaBoneco[len(self.letrasErradas)])

        print(' '.join(self.escondeLetra()))
       # print('\n Chances restantes: ', chances)
        print('Letras erradas: ', ' '.join(self.letrasErradas)) 
         
    
    
    def verificaVitoria(self):
        if '_' not in self.escondeLetra():
            return True
        return False
            
    def verificaDerrota(self):
        print('\nVocê perdeu. A palavra era: ', self.palavra)
    
    def fimJogo(self):
        return self.verificaVitoria() or (len(self.letrasErradas) == 6)


    
def main():

    limpaTela()

    jogo = Forca(escolhePalavra())

    while not jogo.fimJogo():

        jogo.statusJogo()

        letraDigitada = input('\n Digite uma letra: ').lower()
        

        if letraDigitada in jogo.letrasCorretas:
            print("Você ja digitou essa letra")
            continue
        if letraDigitada in jogo.letrasErradas:
            print("Você ja digitou essa letra")
            continue

        jogo.advinhaLetra(letraDigitada)

        
        if jogo.verificaVitoria():
            print('\nParabéns você venceu, a palavra era: ', jogo.palavra)
            break

    jogo.verificaDerrota()



   
main()


#ler uma palava aleatoria do banco de palavras
#nao mostrar a letra no momento do jogo
#advinha letra
#checar o status do jogo e imprimir o desenho
#verificar se o  jogador venceu
#verifica se o jogo terminou
#main - para executar o jogo
 