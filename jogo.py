import random
from os import name, system  

#função para limpar tela ao iniciar novo jogo
def limpaTela():

        #windows
        if name == 'nt':
            _ = system('cls')

        #mac/linux
        else:
            _ = system('clear')

    

#lista de niveis do boneco
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

#escolhendo palavra randomicamete do banco de palavras
def escolhePalavra():
    listaPalavras = ['melão','uva','figo','mamão','amora','caju','laranja','cupuaçu','morango','cereja','abacaxi','marmelo','jaca','banana','framboesa','açaí','pera','pitanga','coco','acerola','manga','maçã']

    palavra = random.choice(listaPalavras)

    return palavra


class Forca():

    #construtor iniciando listas vazias
    def __init__(self, palavra):
         self.palavra = palavra
         self.letrasErradas = []
         self.letrasCorretas = []

    #inserindo '-' na lista de corretas para apresentar na tela
    def escondeLetra(self):
        rtn = ''

        for letra in self.palavra:
            if letra not in self.letrasCorretas:
                rtn += '_'
            else:
                rtn += letra
        return rtn


    #verifica se a letra digitada pertence a palavra escolhida, 
    #caso sim adiciona a lista de letra corretas, caso não insere na lista de letras erradas
    def advinhaLetra(self,letra):
        
        if letra in self.palavra:
            for carac in self.palavra: 
                if carac == letra:
                    self.letrasCorretas.append(carac) 
            return self.letrasCorretas

        else:
            self.letrasErradas.append(letra)
            return  self.letrasErradas
        
    #mostra todas interações com usuario e o desenho do boneco
    def statusJogo(self):

        print('Bem-vindo(a) ao jogo da forca!')
        print('Adivinhe a palavra abaixo:')

        print(desenhaBoneco[len(self.letrasErradas)])

        print(' '.join(self.escondeLetra()))
        print('Letras erradas: ', ' '.join(self.letrasErradas)) 
         
    
    #verifica se o '-' está na lista de palavra corretas para e retorna true para declarar vitória
    def verificaVitoria(self):
        if '_' not in self.escondeLetra():
            return True
        return False
    
    #informa para o jogador a derrota   
    def verificaDerrota(self):
        print('\nVocê perdeu. A palavra era: ', self.palavra)

    #verifica o fim do jogo caso a vitoria seja true ou o limite de letras erradas seja atingido
    def fimJogo(self):
        return self.verificaVitoria() or (len(self.letrasErradas) == 6)


#metodo para executar o programa   
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
 