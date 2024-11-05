import pygame
from scripts.obstaculo import Obstaculo
from scripts.jogador import Jogador
from scripts.interfaces import Texto, Botao

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, tela.get_width() // 2, tela.get_height() - 70)  # Carro posicionado no fundo, centro
        self.obstaculo = Obstaculo(tela)  # Obstáculo (cone) que se moverá de cima para baixo
        self.estado = "partida"  # Estado inicial da partida
        self.pontosValor = 0
        self.contador = 0
        self.pontosTexto = Texto(tela, str(self.pontosValor), 10, 10, (255, 255, 255), 30)
        self.calçada_esquerda = pygame.Rect(0, 0, 35, tela.get_height())  # Calçada esquerda
        self.calçada_direita = pygame.Rect(315, 0, 35, tela.get_height()) 
        
    def atualizar(self):
        self.estado = "partida"
        self.jogador.atualizar()
        self.obstaculo.atualizar()


        # Incrementa a pontuação com o tempo
        self.contador += 1
        if self.contador > 60:
            self.pontosValor += 1
            self.contador = 0
            self.pontosTexto.atualizarTexto(str(self.pontosValor))

        self.pontosTexto.desenhar()
        
        # Verifica se o jogador colidiu com o obstáculo
        if self.obstaculo.detectarColisao(self.jogador.getRect()):
            # Retorna ao menu e redefine posições em caso de colisão
            self.estado = "menu"
            self.jogador.posicao = (self.tela.get_width() // 2, self.tela.get_height() - 70)
            self.obstaculo.y = -self.obstaculo.imagem.get_height()  # Reinicia o obstáculo no topo
            self.pontosValor = 0

        if self.jogador.getRect().colliderect(self.calçada_esquerda) or self.jogador.getRect().colliderect(self.calçada_direita):
            self.estado = "menu"  # Muda para o menu em caso de colisão
            self.jogador.posicao = [175, 400]  # Reseta posição do jogador

        self.jogador.desenhar()
        self.obstaculo.desenhar()
        
        return self.estado
    
class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "CarGame", 100, 20, (255, 255, 255), 50)
        self.estado = "menu"
        self.botao_jogar = Botao(tela, "jogar", 100, 100, 50, (200, 0, 0), (255, 255, 255))

    def atualizar(self):
        self.estado = "menu"
        self.titulo.desenhar()
        self.botao_jogar.desenhar()
       
        if self.botao_jogar.get_click():
            self.estado = "partida"
        
        return self.estado
