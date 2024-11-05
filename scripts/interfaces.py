import pygame

class Texto:
    def __init__(self, tela, texto, x, y, cor, tamanho):
        self.tela = tela
        self.texto = texto
        self.posicao = (x, y)
        self.cor = cor
        self.tamanho = tamanho

        pygame.font.init()  # Inicializa o sistema de fontes
        self.fonte = pygame.font.Font(None, self.tamanho)  # Cria uma fonte para ser utilizada
        self.atualizarTexto(self.texto)  # Atualiza a imagem com o texto inicial

    def desenhar(self):  # Função que exibe o texto na tela
        self.tela.blit(self.imagemTexto, self.posicao)

    def atualizarTexto(self, novoTexto):  # Função para atualizar o texto
        self.texto = novoTexto  # Atualiza o texto armazenado
        self.imagemTexto = self.fonte.render(novoTexto, True, self.cor)  # Atualiza a imagem com o novo texto
    
    
class Botao:
    def __init__(self, tela, texto, x, y, tamanho, corFundo, CorTexto):
        self.tela = tela
        self.texto = Texto(tela,texto,x,y,CorTexto,tamanho)
        self.posicao = (x,y)
        self.corFundo = corFundo

    def desenhar(self):
        rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())
        pygame.draw.rect(self.tela, self.corFundo, rect)
        # Desenha o texto dentro do retângulo
        self.texto.desenhar()

    def get_click(self):
        posicaoMouse = pygame.mouse.get_pos()
        rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())
        if rect.collidepoint(posicaoMouse) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False


