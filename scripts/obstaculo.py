import pygame
import random  # Importa a biblioteca random para gerar posições de obstáculos aleatórias

# Classe Obstáculo para representar os obstáculos na estrada
class Obstaculo:
    def __init__(self, tela):  # Construtor da classe
        # Carrega a imagem do obstáculo (cone de trânsito)
        self.imagem = pygame.image.load('assets/cone.png')
        
        novo_tamanho = (64, 64)  # Defina o novo tamanho (largura, altura)
        self.imagem = pygame.transform.scale(self.imagem, novo_tamanho)
        
        # Define a tela onde o obstáculo será exibido
        self.tela = tela
        
        # Define a posição inicial do obstáculo, começando em uma posição aleatória no topo da tela
        self.x = random.randint(50, 300 - self.imagem.get_width())  # Gera posição x apenas na pista
        self.y = -self.imagem.get_height()  # Começa fora da tela, no topo

        
        # Define a velocidade de movimento do obstáculo (movimento vertical para baixo)
        self.velocidade = 5

    def atualizar(self):  # Método para atualizar a posição do obstáculo
        self.y += self.velocidade  # Move o obstáculo para baixo
        
        # Verifica se o obstáculo saiu totalmente da tela pela parte inferior
        if self.y >= self.tela.get_height():
            # Reposiciona o obstáculo no topo da tela e gera uma nova posição horizontal aleatória
            self.y = -self.imagem.get_height()  # Reinicia a posição vertical para o topo
            self.x = random.randint(50, 300 - self.imagem.get_width())  # Nova posição horizontal apenas na pista


    def desenhar(self):  # Método para desenhar o obstáculo na tela
        # Desenha o obstáculo na tela na posição atual
        self.tela.blit(self.imagem, (self.x, self.y))

    def detectarColisao(self, rectCarro):  # Método para detectar colisão com o carro
        # Cria o retângulo de colisão do obstáculo
        rectObstaculo = pygame.Rect((self.x, self.y), self.imagem.get_size())
        
        # Verifica se o retângulo do carro colide com o do obstáculo
        return rectCarro.colliderect(rectObstaculo)

