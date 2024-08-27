class Movimentavel:
    def mover(self, direcao):
        pass

class Desenhavel:
    def desenhar(self):
        pass

class Personagem(Movimentavel, Desenhavel):
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
       

    def mover(self, direcao):
        x, y = self.posicao
        if direcao == 'cima':
            y += 1
        elif direcao == 'baixo':
            y -= 1
        elif direcao == 'direita':
            x += 1
        elif direcao == 'esquerda':
            x -= 1
        self.posicao = (x,y)
        print(f"{self.nome} movido para a posição ({self.posicao})")

    def desenhar(self):
        print(f"Desenhando {self.nome} na posição ({self.posicao})")


personagem = Personagem("Deadpool", (0,0) )

personagem.mover('cima')  
personagem.desenhar()  

personagem.mover('direita') 
personagem.desenhar() 