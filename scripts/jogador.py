import pygame  # Importa a biblioteca pygame para gráficos, eventos e manipulação de janelas

class Jogador:  # Define a classe Jogador, que representa o carro no jogo
    def __init__(self, tela, x, y):  # Método construtor para inicializar o carro
        # Inicializa a posição do carro como uma lista [x, y]
        self.posicao = [x, y]
        
        # Define o tamanho do carro (largura e altura)
        self.tamanho = (64, 100)  # Redimensionado para ficar mais como um carro
        
        # Cria um retângulo (rect) com base na posição e no tamanho, para detectar colisões
        self.rect = pygame.Rect(self.posicao, self.tamanho)
        
        # Inicializa o contador de frames, para controlar a troca de imagens da animação
        self.contador = 0
        
        # Define o índice da imagem atual, usada na lista de imagens para animação
        self.imagemAtual = 0
        
        # Armazena a tela em que o jogador será desenhado
        self.tela = tela
        
        # Cria uma lista para armazenar a imagem do carro (uma só imagem neste caso)
        self.listaImagens = []
        
        # Carrega a imagem do carro e redimensiona
        imagem = pygame.image.load('assets/carro.png')  # Certifique-se de ter a imagem do carro
        imagem = pygame.transform.scale(imagem, self.tamanho)
        self.listaImagens.append(imagem)

        # Define a velocidade de movimento do carro
        self.velocidade = 5  # Velocidade fixa para movimento horizontal e vertical

    def desenhar(self):  # Método para desenhar o carro na tela
        # Desenha a imagem do carro na posição atual
        self.tela.blit(self.listaImagens[self.imagemAtual], self.posicao)

    def atualizar(self):  # Método para atualizar a posição do carro com base nas teclas pressionadas
        # Obtém o estado das teclas pressionadas
        self.teclas = pygame.key.get_pressed()
        
        # Movimento para a esquerda
        if self.teclas[pygame.K_LEFT]:
            self.posicao[0] -= self.velocidade  # Move o carro para a esquerda

        # Movimento para a direita
        if self.teclas[pygame.K_RIGHT]:
            self.posicao[0] += self.velocidade  # Move o carro para a direita

        # Movimento para frente (para cima)
        if self.teclas[pygame.K_UP]:
            self.posicao[1] -= self.velocidade  # Move o carro para cima (frente)

        # Movimento para trás (para baixo)
        if self.teclas[pygame.K_DOWN]:
            self.posicao[1] += self.velocidade  # Move o carro para baixo (trás)

        # Atualiza o retângulo (rect) com a nova posição para detecção de colisão
        self.rect = pygame.Rect(self.posicao, self.tamanho)

    def getRect(self):  # Método para obter o retângulo do carro, útil para detectar colisões
        return pygame.Rect(self.posicao, self.tamanho)
